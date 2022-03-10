# django起動時にアプリが読み込まれ
# @shared_taskデコレータを利用できるようになる
from .celery import app as celery_app

__all__ = ('celery_app',)
