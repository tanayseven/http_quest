FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip install -e .

ENV FLASK_APP="http_quiz.app:app"

CMD ["flask", "db", "upgrade"]

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
