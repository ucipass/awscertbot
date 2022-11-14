FROM python:3.10.8-alpine

WORKDIR /awscertbot

COPY src/* ./
RUN apk add build-base libffi-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install certbot

CMD [ "/awscertbot/certbot.sh" ]
