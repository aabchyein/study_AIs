### Machine learning
: 컴퓨터에게 데이터에서 학습하고 패턴을 인식하여 작업을 수행하도록 하는 인공 지능의 한 분야로, 명시적인 프로그래밍 없이 데이터로부터 학습하여 의사결정을 내리는 알고리즘을 개발하는 과정

: 머신러닝 파이프라인은 데이터를 가공하고 모델을 학습시키고, 그 결과를 평가하는 일련의 단계를 순서대로 연결한 과정입니다. <데이터 수집 및 전처리-특성 엔지니어링-데이터 분할-모델 선택 및 학습-하이퍼파라미터 튜닝-모델 평가-모델 배포> 단계로 구성됩니다.
#### 학습과정과 방식
|학습과정|방식|
|---|---|
|<img src="https://github.com/aabchyein/study_AIs/assets/132973368/4c11c931-ea18-40d7-aacf-628f09745d57" width="700" height="200">|<img src="https://github.com/aabchyein/study_AIs/assets/132973368/e36b64ae-505d-41de-82f9-04b42521c89a" width="650" height="200">|
## 📄데이터 분석 기초
#### 1. 지도학습
: 입력 데이터와 그에 대응하는 출력과의 관계를 학습하는 머신러닝의 한 분야
- Logistic Regression(로지스틱 회귀) : 이진 분류 문제에 주로 사용되며, 예를 들어 고객이 제품을 구매할지 여부, 이메일이 스팸인지 아닌지 등을 예측하는 데 사용

|주요내용|작성|
|---|---|
|GridSearchCV|[NSC_BND_M20_GridSearchCV](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Classifications/NSC_BND_M20_GridSearchCV.ipynb)|
|FeatureEngineering|[RecurrenceOfSurgery_FeatureEngineering_quest](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Classifications/RecurrenceOfSurgery_FeatureEngineering_quest.ipynb)|
|전처리-정형화-모델학습-예측-평가|[TitanicFromDisaster](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Classifications/TitanicFromDisaster.ipynb)|
|accuracy_score<br>classification_report<br>오차 행렬(confusion matrix)|[TitanicFromDisaster_evaluation](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Classifications/TitanicFromDisaster_evaluation.ipynb)|
|지도학습(다항분류), 트리 기반의 분류 모델|[TitanicFromDisaster_Tree](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Classifications/TitanicFromDisaster_Tree.ipynb)|
|OneHotEncoding<br>Scaling-MinMaxScaler|[scaling/encoding](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Classifications/TitanicFromDisaster_scaling_encoding.ipynb)|
|resampling|[recurrenceOfSurgery_MachineLearning_Normal](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Classifications/recurrenceOfSurgery_MachineLearning_Normal.ipynb)|
- Linear Regression(선형 회귀) : 연속형 값을 예측하는 데 사용. 예를 들어, 주택 가격, 온도, 판매량 등과 같은 연속형 값을 예측하는 데 효과적

|주요내용|작성|
|---|---|
|전처리-모델학습-평가|[BreastCancerWisconsin](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Regressions/BreastCancerWisconsin_Regression.ipynb)|
|전처리-정형화-모델학습-평가|[BreastCancerWisconsin_Regression_evaluations](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Regressions/BreastCancerWisconsin_Regression_evaluations.ipynb)|
|py에서 pickle파일 불러오기|[BreastCancerWisconsin_pickle_Regression.py](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Regressions/BreastCancerWisconsin_pickle_Regression.py)|
|퀘스트|[RecurrenceOfSurgery_regression_quest](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Regressions/RecurrenceOfSurgery_regression_quest.ipynb)|
|퀘스트|[RecurrenceOfSurgery_regression_quest.py](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Regressions/RecurrenceOfSurgery_regression_quest.py)|


#### 2. 비지도학습
: 비지도 학습에서는 출력(레이블)이 없는 데이터에서 숨겨진 구조나 패턴을 발견
- Clustering (클러스터링) : 유사한 특성을 가진 데이터 포인트들을 그룹화하여 서로 다른 클러스터로 나눔. 데이터 내에서 비슷한 패턴이나 특성을 공유하는 그룹을 식별하는 데 사용

|주요내용|작성|
|---|---|
|KMeans 클러스터링 알고리즘|[iris_KMeans](https://github.com/aabchyein/study_AIs/blob/main/datasets/codes/MLs/Clusterings/iris_KMeans.ipynb)|

#### 3. 모델 개발 및 향상(Development and Enhancement)
: 모델 개발 및 향상은 모델을 구축하고 성능을 향상시키기 위한 일련의 단계와 과정을 의미합니다.

|범주|기법들|설명|
|---|---|---|
|데이터 전처리(Data Preprocessing)|One-Hot Encoding|범주형 변수를 모델이 이해할 수 있는 형태로 변환하는 과정. 각 범주를 이진 형태로 나타내는 방법|
| |Scaling|입력 특성들의 범위를 조절하여 모델 학습을 개선하고 수렴 속도를 높이기 위한 과정. 주로 연속형 변수들 간의 크기 차이를 줄이기 위해 사용|
|모델 평가 및 개선(Model Evaluation and Improvement)|Evaluation|모델이 얼마나 효과적으로 작동하는지 평가하는 과정으로, 다양한 지표를 사용(정확도, 정밀도, 재현율, F1 점수 등)|
| |GridSearchCV|모델의 하이퍼파라미터를 튜닝하여 최적의 조합을 찾는 과정으로, 그리드 탐색을 수행|
| |Feature Engineering|모델 학습에 사용되는 특성들을 조작하거나 새로운 특성을 생성하여 모델의 성능을 향상시키는 과정|
| |Resampling|데이터를 재샘플링하여 데이터의 불균형을 조정하거나 모델을 평가할 때 사용되는 기술|
