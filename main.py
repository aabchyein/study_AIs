# 터미널 창에서 실행 : conda install -c conda-forge fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()   #인스턴스화


@app.get("/")   # 주소
async def root():
    return {"message": "Hello World"}


# app.post('/api_v1/mlmodel')   # 통상적으로 uri 뒤에 version을 넣어줌
def mlmodel(data:dict) :  # web에서 서비스하는 것이기 때문에 json형식으로 넘어옴
    return {} # dictionary 형태로 return