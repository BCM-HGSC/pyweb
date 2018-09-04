DATA = b"""\
Hello world from Gunicorn!

Replace the contents of /app/app.py
with your WSGI application.

I just made words with my hands!

I did it again!

It's getting less fun now.

I can keep going.
"""

def app(environ, start_response):
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(DATA)))
    ])
    return iter([DATA])
