FROM python:3.5

# initializations
RUN mkdir /home/app
ADD . /home/app
ADD ./docker/django/uwsgi.ini /etc/uwsgi.ini

# build steps
RUN cd /home/app \
 && pip install --upgrade pip \
 && pip install --upgrade --requirement requirements.txt

# run
WORKDIR /home/app/src

CMD uwsgi /etc/uwsgi.ini