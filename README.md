# flask-gunicorn-server

This repository contains a Flask app with a small html.index, which can be configured through environmental variables. The purpose behind this project is to have a small webapp, that can be configured through a helm chart and used for testing e.g. redirecting traffic to a test app.

# Status
![Dockerfile](https://github.com/AlbertHahn/flask-gunicorn-server/actions/workflows/docker-image-app.yml/badge.svg?branch=main)

## Local deployment

## gunicorn

```sh
cd app
pip install -r requirements.txt
gunicorn -c ./gunicorn/gunicorn.conf.py main:app
http://0.0.0.0:5000
```

## docker

```sh
cd app
docker build -t flask-app .
docker run -p 5000:5000 flask-app
http://0.0.0.0:5000
```