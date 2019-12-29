FROM python:3.8 as build
ENV APP_ENVIRONMENT=test
WORKDIR /app
ADD . /app
RUN pip install 'poetry==1.0.0b8'
RUN poetry install
RUN poetry run pytest -k test/unit

FROM build as db-migrate
WORKDIR /app
ADD . /app
WORKDIR /app
RUN pip install 'poetry==1.0.0b8'
RUN poetry install
CMD ["poetry", "run", "flask", "db", "upgrade"]

FROM build as integration-tests
WORKDIR /app
ENV APP_ENVIRONMENT=test
RUN pip install 'poetry==1.0.0b8'
RUN poetry install
CMD ["poetry", "run", "pytest", "--cov", "http_quest", "--cov", "test", "test/"]

FROM build as prod
ENV APP_ENVIRONMENT=prod
WORKDIR /app
COPY --from=build /app/http_quest /app/http_quest
# To be removed later:
COPY --from=build /app/fakes.py /app/fakes.py
COPY --from=build /app/poetry.lock /app/poetry.lock
COPY --from=build /app/pyproject.toml /app/pyproject.toml
RUN pip install 'poetry==1.0.0b8'
RUN poetry install --no-dev
ENV PORT=8000
EXPOSE ${PORT}
CMD ["poetry", "run", "gunicorn", "app:app", "-b", "0.0.0.0:${PORT}", "-w", "3"]
