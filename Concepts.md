**※ 생활 코딩의 머신러닝1 강의를 참고하여 작성한 문서**

​	**(https://opentutorials.org/course/4548) **



1. ###### 머신러닝

   인간의 결정(비교 + 선택)을 도와주는 도구.

   인간은 선택지의 여러 속성을 수치화해서 뭐가 더 나은지 비교함. (=통계)

   수치적으로 비교하여 가장 나은 것을 선택하는 것이 결정.

   그러나 선택지 및 속성이 너무 많을 경우 결정이 어려움.

   머신러닝은 이러한 결정을 도와주는 도구.



2. ###### 모델과 학습

   ‘머신러닝’이란 판단력을 기계에게 부여하는 기술.

   머신러닝을 만든 사람들은 이런 ‘판단력’을 ‘모델(Model)’이라고 부름.

   이 모델을 만드는 ‘과정’은 ‘학습(Learning)’이라고 부름.

   학습이 잘 되어야 좋은 모델을 만들 수 있고, 모델이 좋아야 더 좋은 추측을 할 수 있다.

   추측이 정확해야 좋은 결정을 할 수 있다.
   
   <img src="C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\001.jpeg" style="zoom:100%;" />
   
   <img src="C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\002.jpeg" style="zoom:100%;" />
   
   

3. ###### 애플리케이션과 프로그램

   같은 것을 가리키는 두 가지 표현.

   애플리케이션(Application) : 어떤 기능을 부품으로 사용해서 만든 완제품.

   머신러닝 애플리케이션 : 머신러닝 모델을 부품을 응용하여 만든 SW.

   프로그램(Program) : 부품을 시간 순서에 따라 실행되도록 기계 언어로 작성.

   프로그래밍(Programing) : 프로그램을 만드는 일.

   프로그래머(Programmer) : 프로그램을 만드는 사람.



4. ###### 데이터 과학과 데이터 공학

   데이터 과학 : 데이터를 만들고, 만들어진 데이터를 이용하는 일

   데이터 공학 : 데이터를 다루는 도구를 만들고 도구를 관리하는 일

   구분되는 것처럼 보이지만 상호 보완적인 관계이다.



5. ###### 표(Table)

   데이터들의 모임. 데이터 세트(Data Set)라고도 부른다.

   행(row)과 열(column)로 이루어져 있다.

   행 : 개체(instance), 관측치(observed value), 기록(record), 사례(example), 경우(case)

   열 : 특성(feature), 속성(attribute), 변수(variable), 필드(field)

   ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\003.jpeg)



6. ###### 독립변수와 종속변수

   변수(variable) : 변할 수 있는 값. 표에서는 열을 의미.

   독립변수(Independent V.) : 원인이 되는 열.

   종속변수(Dependent V.) : 결과가 되는 열.

   상관관계 : 한쪽의 값이 바뀌었을 때, 다른 쪽의 값도 바뀌는 두 열의 관계.

   인과관계 : 상관관계의 일종으로 원인과 결과 관계.

   ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\004.jpeg)



7. ###### 머신러닝의 분류

   지도학습(Supervised L.) : 정답이 있는 문제를 해결하는 것. 

   ​	분류(classification), 회귀(regression)

   비지도학습(Unsepervied L.) : 관찰을 통해 새로운 의미나 관계를 밝혀내는 것.

   ​	군집화(clustering), 변환(transform), 연관(association rule)

   강화학습(Reinforcement L.) : 더 좋은 보상을 받기 위해 수련하는 것.

   ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\005.jpeg)



8. ###### 지도학습

   과거의 데이터를 독립변수와 종속변수로 구분하여 컴퓨터에게 학습.

   컴퓨터는 데이터를 학습하여 모델을 생성한다.

   ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\006.jpeg)

   분류 : 종속변수가 범주형 데이터(Categorical, 이름, 문자)일 경우 사용.

   ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\008.jpeg)

   회귀 : 종속변수가 양적 데이터(Quantitative, 수의 형태)일 때 사용.

   ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\007.jpeg)



9. ###### 비지도학습

   데이터의 성격을 파악하는 것이 목적. 독립변수, 종속변수 분석이 필요하지 않음.

   군집화 : 비슷한 관측치(행)들을 찾아서 그룹을 만드는 일. 클러스터의 개수 N을 입력으로 받아 관측치를 N개의 클러스터로 군집화.

   ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\009.jpeg)

   연관규칙학습 : 특성(열)의 연관성을 파악하여 그룹핑.

   ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\010.jpeg)

   변환 : 데이터를 새롭게 표현하여 사람이나 다른 머신러닝 알고리즘이 원래 데이터보다 쉽게 해석할 수 있도록 함. ex) 고차원 데이터의 특성 수를 줄이면서 꼭 필요한 특정을 포함한 데이터로 표현하는 차원 축소.



10. ###### 강화학습

    환경(environment)의 상태(state)를 관찰하고 더 많은 보상(reward)을 받을 수 있도록 에이전트(agent)가 해야하는 행동(action)을 판단하는 정책(policy)을 만드는 것.

    ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\011.jpeg)

    

11. ###### 머신러닝 기법 선택

    ![](C:\Users\A\Documents\GitHub\Machine-Learning-Study\.img\012.jpeg)