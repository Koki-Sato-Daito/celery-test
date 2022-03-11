import time
from demoapp.models import Widget

from celery import shared_task


@shared_task
def count_widgets():
    time.sleep(60)
    return Widget.objects.count()

@shared_task
def rename_widget(widget_id, name):
    time.sleep(60)
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()
