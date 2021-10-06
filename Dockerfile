FROM python:3.8.0-slim
LABEL org.opencontainers.image.source=addyourlabelhere
ENV TYPE=PROD
ADD . /code
WORKDIR /code
COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install libpq-dev -y \
    && apt-get clean
    
RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
