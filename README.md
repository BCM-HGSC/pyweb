# pyweb

Docker files for a simple Flask + Gunicorn + nginx stack

See `docker-compose.yml` for an example of using the resulting images.
Normally, only `proxyx` and `pyweb` (or a decendent) are required for
production.

Note that although all the examples here use the tag `latest`, production
deployments should use fixed tags.

## proxyx

https://hub.docker.com/r/bcmhgscsub/proxyx/

This image is a simple [nginx](https://hub.docker.com/r/_/nginx/) reverse proxy.

Serves: port 80

Target of the reverse proxy:

`http://app:8000`

Locations inside the container:

* `/nginx/nginx.conf` — the configuration file
* `/nginx/html` — static content mentioned in the configuration file
* `/nginx` — nice location for mounting over for troubleshooting

Build:

`docker build -t bcmhgscsub/proxyx:latest proxyx`

See:

* https://hub.docker.com/r/_/nginx/

## pyweb

https://hub.docker.com/r/bcmhgscsub/pyweb/

This image combines Gunicorn with Flask, starting with
[Debian](https://hub.docker.com/r/_/nginx/). The necessary Python components
are copied from a much heavier "builder" image based on
[continuumio/miniconda3](https://hub.docker.com/r/continuumio/miniconda3/).

Serves: port 8000

Locations inside the container:

* `/env` directory contains Python 3, Gunicorn, and Flask
* `/app` directory contains the Python web app

Build:

`docker build -t bcmhgscsub/pyweb:latest pyweb`

See:

* https://hub.docker.com/_/debian/
* https://hub.docker.com/r/continuumio/miniconda3/

## builder

https://hub.docker.com/r/bcmhgscsub/pywebbuilder/

This image uses
[continuumio/miniconda3](https://hub.docker.com/r/continuumio/miniconda3/)
to build `/env`, which contains Python 3, Gunicorn, and Flask.

See the file `builder/conda-package-list.txt` for the list of packages and
versions included.

The resulting image contains far more software than is needed in production,
so `pyweb` or some other derivative should be deployed instead. To use:

    # Dockerfile
    FROM debian:stretch-slim
    COPY --from=bcmhgscsub/pywebbuilder:latest /env /env/
    # Add your own build commands here.

Build:

`docker build -t bcmhgscsub/pywebbuilder:latest builder`

See:

* https://hub.docker.com/_/debian/
* https://hub.docker.com/r/continuumio/miniconda3/
