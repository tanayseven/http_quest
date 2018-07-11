FROM python:3.7

WORKDIR /app

ADD . /app

# Install Chrome for Selenium
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update -y \
    && apt-get install -y google-chrome-stable

# Install chromedriver for Selenium
RUN curl https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip -o chromedriver_linux64.zip \ 
    && apt-get update \
    && apt-get install unzip -y \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver

RUN pip install -e .

ENV FLASK_APP="http_quiz.app:app"

CMD ["flask", "db", "upgrade"]

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
