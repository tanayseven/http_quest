FROM python:3.8 as build
ENV APP_ENVIRONMENT=test
WORKDIR /app
ADD . /app
RUN pip install 'poetry==1.0.0b8'
RUN poetry install
RUN pytest -k test/unit

FROM build as db-migrate
WORKDIR /app
RUN pip install 'poetry==1.0.0b8'
RUN poetry install
CMD ["flask", "db", "upgrade"]

FROM build as integration-tests
WORKDIR /app
ENV APP_ENVIRONMENT=test
RUN pip install 'poetry==1.0.0b8'
RUN poetry install
CMD ["pytest"]

FROM build as prod
ENV APP_ENVIRONMENT=prod
WORKDIR /app
ENV UWSGI_INI /app/http_quest/uwsgi.ini
COPY --from=build /app/http_quest /app/http_quest
COPY --from=build /app/Pipfile.lock /app/Pipfile.lock
RUN pip install 'poetry==1.0.0b8'
RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-dev
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "-w", "3"]
