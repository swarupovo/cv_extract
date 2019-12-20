# from django.conf import settings
from django_hosts import patterns, host

from cv_upload import settings

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),  # <-- The `name` we used to in the `DEFAULT_HOST` setting
    host(r'help', 'api.urls', name='help'),
)