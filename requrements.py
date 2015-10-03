import sys

install_requires = {
    # Entity classes
    'SQLAlchemy >= 1.0.0',
    'alembic >= 0.8.2',
    # Configuration
    'PyYAML >= 3.11',
    # Crawler
    'celery >= 3.1.17',
    'lxml >= 3.4.3',
    'psycopg2 >= 2.6',  # FIXME
    'requests >= 2.6.0',
    # Web
    'Flask >= 0.10.1',
    'Werkzeug >= 0.10.4',
    # Sparql
    'SPARQLWrapper >= 1.6.2',
    # CLI
    'click >= 4.0',
    # Locale
    'Babel >= 1.3',
    # SCSS
    'libsass >= 0.7.0',
    # OAuth client
    'Flask-OAuthlib >= 0.9.1',
    # Sentry: Log Aggregation
    'raven >= 5.2.0',
    'blinker >= 1.3',
}

if sys.version_info < (3, 4, 0):
    install_requires |= {
        'pathlib >= 1.0',
        'enum34 >= 1.0',
    }

tests_require = {
    'pytest >= 2.6.4',
    'cssselect >= 0.9.1',
    'import-order >= 0.0.1',
}

docs_require = {
    'Sphinx >= 1.2.3',
}

deploy_requires = {
    "invoke == 0.9.0",  # FIXME: least version is 0.10.1. check it with deploy
}
