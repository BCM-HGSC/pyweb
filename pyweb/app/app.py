import logging

from flask import Flask, Response


app = Flask(__name__)

DATA = b"""\
Hello world from Gunicorn!

Replace the contents of /app/app.py
with your WSGI application.

I just made words with my hands!

I did it again!

It's getting less fun now.

I can keep going.
"""

@app.route('/')
def hello_world():
    logging.info('hello from app.hello_world')
    return Response(DATA, mimetype='text/plain')
