FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        mysql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY ../requirements.txt ./
RUN pip install -r requirements.txt
COPY ./app/ ./app/
COPY ./project/ ./project/
COPY ./tests/ ./tests/
COPY ./tests/setting.py ./project/setting.py
COPY ./conf.ini ./
COPY ./manage.py ./
COPY ./start ./

CMD ["./start"]
