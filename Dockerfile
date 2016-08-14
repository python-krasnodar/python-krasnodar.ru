FROM python:3.5

ENV DJANGO_SETTINGS_MODULE "pykrd.settings"

RUN mkdir -p /home/build && \
    mkdir -p /home/build/static && \
    mkdir -p /home/build/media

ADD ./src /home/build/src
ADD ./requirements.txt /home/build/requirements.txt
ADD ./.bowerrc /home/build/.bowerrc
ADD ./bower.json /home/build/bower.json
ADD ./docker/django/uwsgi.ini /home/build/uwsgi.ini

VOLUME ["/home/build/static", "/home/build/media"]

RUN pip install --upgrade pip && \
    pip install -r /home/build/requirements.txt

RUN cp /home/build/src/pykrd/localsettings.py.docker.dist /home/build/src/pykrd/localsettings.py

RUN apt-get update &&  apt-get install -y wget node npm \
 && ln -s /usr/bin/nodejs /usr/bin/node \
 && npm install -g bower

RUN cd /home/build

ENV DOCKERIZE_VERSION v0.2.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /home/build/src

EXPOSE 8000
CMD dockerize -wait tcp://db:5432 && \
    python manage.py migrate --no-input && \
    python manage.py collectstatic --no-input && \
    uwsgi --ini /home/build/uwsgi.ini
