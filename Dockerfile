FROM python:3.8 as build
ENV APP_ENVIRONMENT=test
WORKDIR /app
ADD . /app
RUN pip install 'poetry==1.0.0b8'
RUN poetry export --dev -f requirements.txt > requirements.txt \
    && pip install -r requirements.txt
RUN poetry run pytest -k test/unit

FROM build as db-migrate
WORKDIR /app
ADD . /app
WORKDIR /app
RUN pip install 'poetry==1.0.0b8'
RUN poetry export --dev -f requirements.txt > requirements.txt \
     && pip install -r requirements.txt
CMD ["flask", "db", "upgrade"]

FROM build as integration-tests
WORKDIR /app
ENV APP_ENVIRONMENT=test
RUN pip install 'poetry==1.0.0b8'
RUN poetry export --dev -f requirements.txt > requirements.txt \
    && pip install -r requirements.txt
CMD ["pytest", "--cov", "http_quest", "--cov", "test", "test/"]

FROM build as prod
ENV APP_ENVIRONMENT=prod
WORKDIR /app
COPY --from=build /app/http_quest /app/http_quest
# To be removed later:
COPY --from=build /app/fakes.py /app/fakes.py
COPY --from=build /app/poetry.lock /app/poetry.lock
COPY --from=build /app/pyproject.toml /app/pyproject.toml
RUN pip install 'poetry==1.0.0b8'
RUN poetry export -f requirements.txt > requirements.txt \
    && pip install -r requirements.txt
RUN pip uninstall -y poetry
EXPOSE 8000
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "-w", "3"]
