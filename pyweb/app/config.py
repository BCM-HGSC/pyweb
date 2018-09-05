import os
from sys import stderr


print('hello from /app/config.py', file=stderr)

bind = '0.0.0.0:8000'
pidfile = '/var/run/gunicorn.pid'


# Load any relevant environment variables as settings...

# From example here:
# https://sebest.github.io/post/protips-using-gunicorn-inside-a-docker-image/
for k, v in os.environ.items():
    if k.startswith('GUNICORN_'):
        value = v
        # Example of translating values from strings.
        # Should probably due this using a dict from the key.
        if value == 'True':
            value = True
        key = k.split('_', 1)[1].lower()
        globals()[key] = value
        print('{}={!r}'.format(key, value), file=stderr)
