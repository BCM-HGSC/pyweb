import logging
import logging.config
import os


bind = '0.0.0.0:8000'
pidfile = '/var/run/gunicorn.pid'

# See: http://docs.gunicorn.org/en/latest/settings.html#logconfig-dict
logconfig_dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '[%Y-%m-%d %H:%M:%S %z]'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    },
    'loggers': {
        'asyncio': {},
        'concurrent.futures': {},
        'gunicorn': {},
        'gunicorn.access': {'level': 'INFO', 'propagate': False},
        'gunicorn.error': {'level': 'INFO', 'propagate': True},
        'gunicorn.http': {},
        'gunicorn.http.wsgi': {},
    },
}

logging.info('Hello from /app/config.py on %d', os.getpid())


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
        logging.info('%s=%r', key, value)

logging.info('Leaving /app/config.py')
