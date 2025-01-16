# This line runs your Django app with Gunicorn for handling HTTP requests
web: gunicorn Swiftgen--Core.wsgi:application --bind 0.0.0.0:$PORT


# This line runs Daphne for handling WebSocket connections
daphne -u /tmp/daphne.sock Work.asgi:application

# This line runs the Channels worker for handling background tasks
# worker: python manage.py runworker
worker: python manage.py runworker -v2 channels
