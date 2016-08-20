FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE "pykrd.settings"
ENV DOCKERIZE_VERSION v0.2.0

RUN mkdir -p /app/src \
 && mkdir -p /app/static \
 && mkdir -p /app/media

ADD ./src /app/src
ADD ./requirements.txt /app/requirements.txt
ADD ./docker/django/uwsgi.ini /app/uwsgi.ini

RUN apt-get update && apt-get install -yq curl wget \
 && curl -sL https://deb.nodesource.com/setup | bash - \
 && apt-get update && apt-get install -yq nodejs \
 && npm install -g npm bower

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# copy local settings for django
#RUN cp /app/src/pykrd/localsettings.py.docker.dist /app/src/pykrd/localsettings.py

# install pip packages
RUN pip install --upgrade pip \
 && pip install -r /app/requirements.txt

VOLUME ["/app/static", "/app/media", "/app/src"]
WORKDIR /app/src
EXPOSE 3000

CMD dockerize -wait tcp://db:5432 \
 && cp /app/src/pykrd/localsettings.py.docker.dist /app/src/pykrd/localsettings.py \
 && python manage.py migrate --no-input \
 && python manage.py bower_install -- --allow-root \
 && python manage.py collectstatic --no-input \
 && uwsgi --ini /app/uwsgi.ini
