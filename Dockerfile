FROM python:3.10.8-alpine

WORKDIR /awscertbot

COPY src/* ./
RUN chmod a+x ./certbot.sh
RUN chmod a+x ./auth-hook.py
RUN chmod a+x ./cleanup-hook.py
RUN apk add build-base libffi-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install certbot

CMD [ "/awscertbot/certbot.sh" ]
