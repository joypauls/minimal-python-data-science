FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y cron

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab
RUN touch /var/log/cron.log

COPY . .

CMD [ "cron", "-f" ]