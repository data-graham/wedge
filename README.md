# wedge
### Django logging deadlock demo

This app demonstrates a case where an HTML page served from a view triggers many (3 or more) AJAX calls to additional (trivial) template views in the Django app, all executed in parallel and at effectively the same time. This eventually leads to a deadlock that appears to be caused by the logging subsystem.

It may be possible to recreate this deadlock via a simpler test such as a high volume of simultaneous requests to a single view, but this AJAX approach is what has exposed the issue in production (Apache/wsgi) environments as well as via `runserver`.

## Installation

1. Create a venv (I used python 3.7.2) and activate
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`

See `LOGGING` in `wedge/settings.py` for how to repro.
