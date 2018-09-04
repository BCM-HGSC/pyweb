# Builds a "lightweight" Gunicorn + Flask image by copying just the necessary
# Python environment onto debian.

# The /env directory contains Gunicorn.
# The /app directory contains the Python web app.

# docker build -t bcmhgscsub/pyweb:latest pyweb/pyweb/

FROM debian:stretch-slim
COPY --from=bcmhgscsub/pywebbuilder:latest /env /env/
ENV PATH=/env/bin:$PATH
WORKDIR /app
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/env/bin/gunicorn", "--config", "config.py", "app:app"]
COPY /app /app/
