# 사용자에게 입력받은 설명변수 값 3개를 변수에 담기
# 체중, 수숡시간의 D.type이 float 형식
# input() return str() -> float()
height = int(input('신장'))
weight = float(input('체중'))
ot = float(input('수술시간'))

import pickle

with open('datasets/RecurrenceOfSurgery_regression_quest.pkl', 'rb') as regression_file :
    loaded_model = pickle.load(regression_file)
    input_labels = [[height, weight, ot]]
    result_predict = loaded_model.predict(input_labels)
    print('Predict 연령 Result : {}'.format(result_predict))
    pass