web: gunicorn --pythonpath typeYou/ --bind :5736 --workers=4 typeYou.wsgi
worker: celery --workdir=typeYou/ --app=typeYou.celery:app --concurrency=3 worker
flower: celery --workdir=typeYou/ --app=typeYou.celery:app flower
