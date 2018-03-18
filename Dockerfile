FROM python:3

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install python3-pip  python-dev -y

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py

CMD ["python3", "app.py"]
