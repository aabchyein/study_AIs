# 사용자에게 서비스를 하는 단게이기 때문에 사용자에게 값을 입력받음.(설명변수 2개의 값)
# 사용자에게 입력받은 값을 변수로 담기
# 예제 : [[16.34, 87.21]] -> 소수점이 있는 float 형식
# input() return str() -> float()
texture_mean = float(input('texture_mean : '))
perimeter_mean= float(input('perimeter_mean : '))

# 예측하기
import pickle

with open('datasets/BreastCancerWisconsin_Regression.pkl','rb') as regression_file : 
    loaded_model = pickle.load(regression_file)
    input_labels = [[texture_mean, perimeter_mean]]   # 학습했던 설명변수 형식
    result_predict = loaded_model.predict(input_labels)
    print('Predict radius_mean Result : {}'.format(result_predict))
    pass
    # datasets/BreastCancerWisconsin_Regression.pkl : vs code는 프로젝트에 종속. 경로를 설정할 때 root부터 시작됨. 앞에 슬래시를 넣으면 c드라이브로 가게 되므로 슬래시를 넣지 않음.
    # rb: binary(이진) 이진파일을 읽어오기
    # 1. pickle로 만들어 놓은 학습시킨 model 불러오기 -> loaded_model = pickle.load(regression_file)
    # 2. 모델을 교육시킬 때 dataframe형식으로 교육시켰기 때문에 형식을 맞춰줘야 함 -> input_labels = [[texture_mean, perimeter_mean]]