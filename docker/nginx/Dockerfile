FROM nginx:stable

ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /var/www/static && \
    mkdir -p /var/www/media

VOLUME ["/var/www/static", "/var/www/media"]
