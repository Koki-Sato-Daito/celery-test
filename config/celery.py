import os

from celery import Celery

# 'celery' プログラムのためのデフォルトの Django 設定モジュールを設定します。
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config', broker="redis://redis//")

# settings.pyにCelory関連の設定を書くときにCELERY_*という接頭辞をつけることができる
app.config_from_object('django.conf:settings', namespace='CELERY')

# Djangoに登録された全ての タスクモジュールをロードします。
app.autodiscover_tasks()

# bind=Trueは現在のタスクインスタンスを簡単に取得でいる
# このタスク自体はリクエスト情報を出力する
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
