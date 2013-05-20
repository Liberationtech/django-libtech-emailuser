========================
django-libtech-emailuser
========================

django-libtech-emailuser is a simple reusable Django app to for using emailaddress
as usernames within `django.contrib.auth` in  Django 1.5 and later.

There's a number apps out there for doing authentication with emailaddresses prior to Django 1.5.
With the advent of Django 1.5 the Django core team has made it 
very easy to use any model for authentication simply by setting
`AUTH_USER_MODEL`. Unfortunately it's not possible to create a EmailUser model by simply
subclassing the User class in `django.contrib.auth.models` instead if you want a model that plays 
nicely with the rest of `django.contrib.auth` the simplest way is to copy all the code in
`django.contrib.auth.models.User` and substitute username for emailaddress. You also need to 
edit some other minor stuff. This Django app does just that. I'm using it in production for a couple
of client sites and it works fine.

Quick start
-----------

1. Install django-libtech-emailuser

    pip install django-libtech-emailuser


2. Add "emailuser" to your INSTALLED_APPS setting in `settings.py` like this::

      INSTALLED_APPS = (
          ...
          'emailuser',
      )

3. Set your AUTH_USER_MODEL setting in `settings.py`

    AUTH_USER_MODEL = "emailuser.EmailUser"

4. Get the emailuser table created in your database

    ./mangage.py syncdb
