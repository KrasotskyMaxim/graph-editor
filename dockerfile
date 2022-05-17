FROM python:3

USER root

COPY . /

RUN pip install wheel

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]