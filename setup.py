import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-libtech-emailuser',
    version='0.2',
    packages=['emailuser'],
    include_package_data=True,
    license='BSD License',
    description='Use emailaddress as username in Django +1.5',
    long_description=README,
    url='https://github.com/Liberationtech/django-libtech-emailuser',
    author='Oivvio Polite',
    author_email='oivvio@liberationtech.net',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
