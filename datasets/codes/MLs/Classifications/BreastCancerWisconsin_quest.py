# 설명변수 값 입력받기 - float형식으로 바꿔주기
radius_worst = float(input('radius_worst'))
perimeter_worst = float(input('perimeter_worst'))
area_worst = float(input('area_worst'))

import pickle

with open('datasets/BreastCancerWisconsin_regression_quest.pkl', 'rb') as regression_file :
    loaded_model = pickle.load(regression_file)
    input_labels = [[radius_worst, perimeter_worst, area_worst]]
    result_predict = loaded_model.predict(input_labels)
    print('Predict Diagnosis Result : {}'.format(result_predict))
    pass

# 임의로 10번째 레코드의 값 넣기: radius_worst, perimeter_worst, area_worst
#                                 19.19, 123.8, 1150.0	
# Predict Diagnosis Result : [0]