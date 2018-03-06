from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gym.settings')

# app = Celery('PyRef')
app = Celery('Gym', broker='redis://guest@localhost:6379/')
# app.config_from_object('PyRef:settings', namespace='CELERY')
