## Qiita記事
- pagelink


## 使い方
- 準備
```
$ git clone https://github.com/Koki-Sato-Daito/celery-test.git
$ cd celery-test
$ docker-compose up --build
```
- ビルドができたら、コンテナ名を確認します
```
$ docker-compose ps
```
- python3コンテナに入ります
```
$ docker container exec -it python3 bash
```
- コンテナに入ったらtmuxサーバーを立てて
```
$ tmux
# Paneを複数立ち上げます(Ctrl+b を押してから " or % )
# Paneの切り替えはctrl+bを押してから o です。
```
- pythonの仮想環境を作り、サーバを起動
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver 0.0.0.0:8000
```
- Paneを切り替えて、Celeryのワーカープロセスを起動させます
```
$ source venv/bin/activate
$ celery -A proj worker -l INFO
```
- http://localhost:8000 をブラウザで開くと動作確認ができます。
