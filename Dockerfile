FROM python:3.10-slim-buster

WORKDIR /django_app

COPY requirements.txt requirements.txt
RUN pip3 install --default-timeout=100 -r requirements.txt

COPY . .

CMD [ "python3", "DjangoPractice/manage.py" , "runserver" ]