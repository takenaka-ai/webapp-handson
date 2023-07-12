# バックエンド(FastAPI)
Webアプリケーションハンズオン用のバックエンドです.
四則演算および同期・非同期確認用のパスを用意しています.

## 動作環境
python v3.11.4

## インストール
pipで必要なライブラリをインストール 

```shell
pip install -r requirements.txt
```

## サーバーの起動
uvicornで起動する場合は下記
```shell
uvicorn src.main:app
```
 
開発モードで起動する場合は下記
```shell
uvicorn src.main:app --reload
```


ホストおよびポートを指定する場合は下記
```shell
uvicorn src.main:app --host 0.0.0.0 --port  8000
```

gunicornで起動する場合は下記
```shell
gunicorn src.main:app -w 2 -k uvicorn.workers.UvicornWorker
```
