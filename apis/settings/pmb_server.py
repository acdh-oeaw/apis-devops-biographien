from .base import *
import os
import dj_database_url
import re

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEV_VERSION = False
APIS_LIST_VIEWS_ALLOWED = True
APIS_DETAIL_VIEWS_ALLOWED = True
CUSTOM_LOGO_IMG = "https://shared.acdh.oeaw.ac.at/apis/pmb/project-logo.svg"
REDMINE_ID = "13424"
LANGUAGE_CODE = "de"

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = (
    "rest_framework.permissions.IsAuthenticatedOrReadOnly",
)

PROJECT_NAME = "pmb"

APIS_BASE_URI = "https://pmb.acdh.oeaw.ac.at/"

REDMINE_ID = "13424"
APIS_RELATIONS_FILTER_EXCLUDE += ['annotation', 'annotation_set_relation']

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

ALLOWED_HOSTS = re.sub(
    r"https?://",
    "",
    os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,pmb.acdh.oeaw.ac.at,.acdh-cluster.arz.oeaw.ac.at,pmb.acdh-dev.oeaw.ac.at,pmbdev.acdh-cluster.arz.oeaw.ac.at"),
).split(",")
# You need to allow '10.0.0.0/8' for service health checks.
ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]

APIS_SKOSMOS = {
    'url': os.environ.get('APIS_SKOSMOS', 'https://vocabs.acdh-dev.oeaw.ac.at'),
    'vocabs-name': os.environ.get('APIS_SKOSMOS_THESAURUS', 'pmbthesaurus'),
    'description': 'Thesaurus of the PMB project. Used to type entities and relations.'
}

BIRTH_REL = [88, ]
DEATH_REL = [89, ]
PL_A_PART_OF = [1106, 1136]
PL_B_LOCATED_IN = [971, ]
ORG_LOCATED_IN = [1141, 970, 1160]
AUTHOR_RELS = [1049, ]

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://f6b8b2a614c84034b5e8135c08a80b1a@o4504360778661888.ingest.sentry.io/4504360844394496",
    integrations=[DjangoIntegration()],
    environment="production",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)


####### ROBOTS.TXT HANDLING #######

# robots.txt file needs to be located in a folder that is registered as a template-dir
# both the end of the url from where the file is served as well as the file itself needs to be named robots.txt
# if you want to add your own robots txt, create a new folder in the root directory and register it here

# replace the path to the folder in which the robots.txt file is to be found here
ROBOTS_TXT_FOLDER = os.path.join(BASE_DIR, "robots_template")

# register above folder as a template-dir
TEMPLATES[0]["DIRS"] += [ROBOTS_TXT_FOLDER,]