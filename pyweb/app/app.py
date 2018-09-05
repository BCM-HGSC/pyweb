import logging

from flask import Flask, Response


app = Flask(__name__)

DATA = b"""\
Hello world from Gunicorn!

And Flask!

Replace the contents of /app/app.py
with your Flask or WSGI application.
"""

@app.route('/')
def hello_world():
    logging.info('hello from app.hello_world')
    return Response(DATA, mimetype='text/plain')
