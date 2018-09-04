# Uses Miniconda 3 to build an environment containing Flask and Gunicorn.
# The resulting directory is /env, and the intention is to copy the /env
# directory into a lightweight image that contains a web application.

# docker build -t bcmhgscsub/pywebbuilder:latest pyweb/builder/

# FROM debian:stretch-slim
# COPY --from=bcmhgscsub/pywebbuilder:latest /env /env/

FROM continuumio/miniconda3:4.5.4 as builder
COPY /conda-package-list.txt /
RUN set -x \
    && /opt/conda/bin/conda create -p /env --file conda-package-list.txt \
    && /opt/conda/bin/conda clean -tipsy
