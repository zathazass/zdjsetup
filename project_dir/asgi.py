import os
from <<project_name>>.setenv import PRODUCTION

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', PRODUCTION)

application = get_asgi_application()
