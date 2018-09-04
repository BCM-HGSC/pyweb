# Simple nginx reverse proxy

# /nginx/nginx.conf — the configuration file
# /nginx/html — static content mentioned in the configuration file

# http://app:8000 - the target of the reverse proxy

# docker build -t bcmhgscsub/proxyx:latest pyweb/proxyx/

FROM nginx:1.15.3
COPY /nginx /nginx/
RUN set -x \
    && rm /etc/nginx/nginx.conf \
    && ln -s /nginx/nginx.conf /etc/nginx/nginx.conf
