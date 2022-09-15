import os
from django.core.wsgi import get_wsgi_application
from aiohttp_wsgi import serve


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "happytax.settings")


application = get_wsgi_application()
serve(application)

