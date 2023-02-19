FROM centos:7

USER root

ENV PIP_DEFAULT_TIMEOUT 720
ENV VIRTUALENV_NO_DOWNLOAD=1
ENV VAULT_VERSION=1.7.2
ADD . /usr/bin/
RUN mkdir /app/weather_app
RUN cp -r src/ /app/weather_app
RUN chmod +x /app/weather_app/weather_app.py

ENTRYPOINT /app/weather_app/weather_app.py
