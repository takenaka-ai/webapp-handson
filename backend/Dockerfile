FROM python:3.11.4
WORKDIR /home/backend

# Note:
#   Dockerfile単体では ./requirements.txt というパスを参照するのが自然だが、
#   docker-compose.ymlで `context` が `.` に設定されているため、
#   ./backend/requirements.txt というパスで参照する必要がある
COPY ./backend/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt && \
  rm /tmp/requirements.txt

# デフォルトコマンドの設定
# docker-compose.ymlで `command` を指定すると上書きされる
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
