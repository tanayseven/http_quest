FROM python:3.7 as build
ENV APP_ENVIRONMENT=test
WORKDIR /app
ADD . /app
RUN pip install pipenv && pipenv install --system --dev
RUN pytest -k test/unit

FROM build as db_migrate
WORKDIR /app
CMD ["flask", "db", "upgrade"]

FROM build as api_tests
WORKDIR /app
ENV APP_ENVIRONMENT=test
CMD ["pytest"]

FROM build as prod
ENV APP_ENVIRONMENT=prod
WORKDIR /app
ENV UWSGI_INI /app/http_quest/uwsgi.ini
COPY --from=build /app/http_quest /app/http_quest
COPY --from=build /app/Pipfile /app/Pipfile
COPY --from=build /app/Pipfile.lock /app/Pipfile.lock
RUN pip install pipenv && pipenv install --system
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "-w", "3"]
