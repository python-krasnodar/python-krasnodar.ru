FROM nginx:stable

ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /home/build/static && \
    mkdir -p /home/build/media

VOLUME ["/home/build/static"]
VOLUME ["/home/build/media"]
