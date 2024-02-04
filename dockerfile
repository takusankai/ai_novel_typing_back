# Dockerfileの例
FROM python:3.11

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

# アプリケーションのコピー
COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# アプリケーションの実行
CMD ["flask", "run"]
