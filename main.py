# 터미널 창에서 실행 : conda install -c conda-forge fastapi uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()   #인스턴스화

# No 'Access-Control-Allow-Origin'  : 해당 오류 해결해보기
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")   # 주소
async def root():
    return {"message": "Hello World"}

import pickle # 학습시킨 모델을 외부에서도 사용하기 위해 pickle로 저장해서 불러올 수 있게 만든다.

# 파라미터와 리턴값은 json의 dictionary형식이어야 함
# /api_v1/mlmodelwithregression with dict params
# method : 'post'를 사용
@app.post('/api_v1/mlmodelwithregression')   # 통상적으로 uri 뒤에 version을 넣어줌
def mlmodelwithregression(data:dict) :     # json   
    print('data with dict {}'.format(data))   # {'texture_mean':16.34, 'perimeter_mean':87.21} --> data로 대치됨
    # data dict to 변수 할당
    texture_mean = float(data['texture_mean'])
    perimeter_mean = float(data['perimeter_mean'])
    
    # pkl 파일 존재 확인 코드 필요(★방어코드★)- 직접 넣어볼 것

    result_predict = 0;
    # 학습 모델 불러와 예측
    with open('datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file:
        loaded_model = pickle.load(regression_file)
        input_labels = [[texture_mean, perimeter_mean]] # 학습했던 설명변수 형식 맞게 적용
        result_predict = loaded_model.predict(input_labels)
        print('Predict radius_mean Result : {}'.format(result_predict))
        pass

    # 예측값 리턴(dictionary형태로)
    result = {'radius_mean':result_predict[0]}
    return result