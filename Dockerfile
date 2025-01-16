FROM python:slim
  
WORKDIR /code

COPY test.py /code/

COPY wallet.py /code/
