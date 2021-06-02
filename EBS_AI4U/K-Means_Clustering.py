import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

# Input : fifa2019.csv (from https://www.kaggle.com/karangadiya/fifa19/version/4)
# Output : 선수들을 체력과 드리블 능력에 따라 3개 팀으로 분류
# Algorithm : K-Means Clustering
#   1. 표본 공간에 K개의 중심(centroid) 설정
#   2. 각 표본을 가장 가까운 중심에 할당하여 군집(cluster) 생성
#   3. 각 군집의 중심 새롭게 계산
#   4. 군집의 중심과 해당 군집에 속한 데이터 간의 거리를 계산한 결과에 변화가 없을 때까지 2, 3단계 반복

file = 'fifa2019.csv'
xlabel = 'Stamina'
ylabel = 'Dribbling'

# 데이터 불러오기
def loadDataFromFile(filePath):
    return pd.read_csv(filePath)

# 필요한 데이터 200개만 추출
def extractEssentialData(allData):
    target_features = [xlabel, ylabel]
    return pd.DataFrame(allData, columns = target_features)[:200]

# 데이터를 시각화하여 표현
# color map 관련 참조 : https://frhyme.github.io/python-lib/matplotlib_extracting_color_from_cmap/
def drawScatterDiagram(title, centrods, cluster, data):
    data_array = np.array(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    c_lst = [plt.cm.rainbow(a) for a in np.linspace(0.0, 1.0, len(centrods))]
    for i in range(len(centrods)):
        plt.scatter(data_array[cluster == i, 0], data_array[cluster == i, 1], marker='o', color=c_lst[i], s=10, label='group ' + str(i+1), alpha=0.5)

    #plt.scatter(data_array[cluster == 0, 0], data_array[cluster == 0, 1], marker='^', c='red', s=10, label='A')
    #plt.scatter(data_array[cluster == 1, 0], data_array[cluster == 1, 1], marker='o', c='yellow', s=10, label='B')
    #plt.scatter(data_array[cluster == 2, 0], data_array[cluster == 2, 1], marker='x', c='blue', s=10, label='C')
    plt.scatter(centrods[:, 0], centrods[:, 1], marker='*', color='black', s=50, label='centroids')
    plt.legend(loc='best')
    plt.grid()
    plt.show()

# K-Means 알고리즘 적용
def kMeansAlgorithm(data, k, centrods):
    data_array = np.array(data)
    centrods_old = []
    #number = 1

    if centrods == []:
        # 1. 표본 공간에 K개의 중심(centroid) 설정
        centrods_x = np.random.choice(data[xlabel],k)
        centrods_y = np.random.choice(data[ylabel],k)
        centrods = np.array(list(zip(centrods_x, centrods_y)))
    # print('Centrods : ', centrods)

    # 4. 군집의 중심과 해당 군집에 속한 데이터 간의 거리를 계산한 결과에 변화가 없을 때까지 2, 3단계 반복
    while not np.array_equal(centrods_old, centrods):
        # 2. 각 표본을 가장 가까운 중심에 할당하여 군집(cluster) 생성
        cluster = np.zeros(len(data_array))
        for i in range(len(data_array)):
            distances = []
            for j in range(k):
                distances.append(distance(data_array[i], centrods[j]))
            cluster[i] = np.argmin(distances)
        # print('Cluster : ', cluster)

        # 3. 각 군집의 중심 새롭게 계산
        centrods_old = deepcopy(centrods)
        for i in range(k):
            points = [data_array[j] for j in range(len(data_array)) if cluster[j] == i]
            centrods[i] = np.mean(points)
        # print('Centrods : ', centrods)

        #drawScatterDiagram('scatter diagram ' + str(number), centrods, cluster, data)
        #number += 1

    return cluster, centrods

# 두 점의 유클리디안 거리 계산
def distance(A, B):
    return np.sqrt(np.sum(np.power((A-B),2)))

allData = loadDataFromFile(file)
# print(allData.head(2))
# print(allData.info())
# print(allData.describe())
essentialData = extractEssentialData(allData)
# print(essentialData.head(2))
cluster, centrods = kMeansAlgorithm(essentialData, 3, [])
drawScatterDiagram('my algorithm', centrods, cluster, essentialData)

# scikit-learn을 이용하여 K-Means 모델 적용
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3)
k_means.fit(essentialData)
centrods = k_means.cluster_centers_
cluster = k_means.predict(essentialData)
drawScatterDiagram('scikit-learn algorithm', centrods, cluster, essentialData)
