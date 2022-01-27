import os
import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artdox_api.settings')

app = Celery('artdox_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'checkOrderItems':{
        'task':'Order.tasks.checkOrderItems',
        'schedule' : crontab(minute=0,hour=0 )
    },

}
