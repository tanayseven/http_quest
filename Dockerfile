FROM python:3.7 as build
WORKDIR /app
ADD . /app
RUN pip install pipenv && pipenv install
CMD ["APP_ENVIRONMENT=test","pytest"]
CMD ["flask", "db", "upgrade"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]

FROM tiangolo/uwsgi-nginx:python3.7 as prod
ENV UWSGI_INI /app/http_quest/uwsgi.ini
COPY ./http_quest /app/http_quest
COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
RUN pip install pipenv && pipenv install
