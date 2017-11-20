=====
SkyGate
=====

SkyGate is a simple Django app which generates an 'admin panel'.


Quick start
-----------

1. Add "SkyGate" and Django REST Framework to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'SkyGate',
        'rest_framework'

    ]

2. Install Django REST Framework by running 'pip install djangorestframework'

3. Add URLs into settings, just under ROOT_URLCONF like this:

ROOT_URLCONF = 'yourproject.urls' <---- under this
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'

4. Include those URLconfs in your project urls.py like this::

        url(r'^', include('SkyGate.urls', namespace='SkyGate')),
        url(r'^registration/', include('SkyGate.urls', namespace="registration")),

5. Run `python manage.py migrate` to create the SkyGate models.

6. Create superuser - run `python manage.py createsuperuser`

7. Visit http://127.0.0.1:8000

8. Login using your superuser credentials.

9. Enjoy SkyGate!