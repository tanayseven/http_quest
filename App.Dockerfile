FROM python:3.6

WORKDIR /app

ADD . /app

# Install Chrome for Selenium
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb

# Install chromedriver for Selenium
RUN curl https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver

RUN pip install -e .

ENV FLASK_APP="http_quiz.app:app"

CMD ["flask", "db", "upgrade"]

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
