# python3.11 のイメージをダウンロード
FROM python:3.11-buster
# python の出力表示を Docker用に調整
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# pip を使って poetry をインストール
RUN pip install poetry

# poetry の定義ファイルをコピー（存在する場合）
COPY pyproject.toml* poetry.lock* ./

# poetry でライブラリをインストール(pyproject.toml が既にある場合)
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ];then poetry install --no-root; fi

# uvicorn のサーバーを立ち上げる
ENTRYPOINT ["poetry","run","uvicorn","api.main:app","--host","0.0.0.0","--reload"]
