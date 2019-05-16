FROM python:3.7 as build
WORKDIR /app
ADD . /app
RUN pip install -e .
CMD ["APP_ENVIRONMENT=test","pytest"]
CMD ["flask", "db", "upgrade"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]

FROM tiangolo/uwsgi-nginx:python3.7 as prod
ENV UWSGI_INI /app/http_quest/uwsgi.ini
COPY ./http_quest /app/http_quest
COPY ./setup.py /app/setup.py
RUN pip install -e .
