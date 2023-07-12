from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware # CORSエラーの回避に必要
from pydantic import BaseModel # POSTでの型定義に必要

app = FastAPI() # FastAPIインスタンスの生成

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
) # ヘッダーの追加（おまじない）


#JSONを返す
@app.get("/")
def root():
    return  {"message": "Hello world"}


#パスパラメータを受け取る
@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"value": a + b}


# クエリパラメータを受け取る
@app.get("/mul")
def mul(a: int, b: int):
    return {"value": a * b}


# POSTでbodyを受け取る
class Sub(BaseModel):
    a: int
    b: int


@app.post("/sub")
def sub(sub: Sub):
    return  {"value": sub.a - sub.b}

# 同期・非同期の比較
import time
import datetime
import asyncio
import os

@app.get("/sync1")
def synchronous1():
    start = datetime.datetime.now()
    time.sleep(10) # 重い処理
    end = datetime.datetime.now()
    return {
        "start": str(start),
        "end": str(end)
    }

@app.get("/sync2")
def synchronous2():
    start = datetime.datetime.now()
    time.sleep(10) # 重い処理
    end = datetime.datetime.now()
    return {
        "start": str(start),
        "end": str(end)
    }

# 非同期通信
@app.get("/async1")
async def asynchronous1():
    print(os.getpid())
    start = datetime.datetime.now()
    await asyncio.sleep(10) # 重い処理
    end = datetime.datetime.now()
    return {
        "start": str(start),
        "end": str(end)
    }

# 非同期通信
@app.get("/async2")
async def asynchronous2():
    print(os.getpid())
    start = datetime.datetime.now()
    await asyncio.sleep(10) # 重い処理
    end = datetime.datetime.now()
    return {
        "start": str(start),
        "end": str(end)
    }
