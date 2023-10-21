FROM python:3.10

# 作業ディレクトリを設定
WORKDIR /app

# ホストのファイルをコンテナの作業ディレクトリにコピー
COPY ./flet /app

# 依存関係をインストール
RUN pip install flet

# コンテナを起動したときに実行されるコマンドを設定
# CMD ["python"]