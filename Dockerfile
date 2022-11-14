FROM python:3.10.8-alpine

WORKDIR /awscertbot

COPY src/* ./
RUN apt-get update -q \
  && apt-get install --no-install-recommends -qy \
  gcc \                                  
  && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install certbot

CMD [ "/awscertbot/certbot.sh" ]
