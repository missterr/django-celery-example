from django_celery_example.celery import app


@app.task
def test():
    print('Test')
    with open('/tmp/test.txt', 'w') as hndl:
        hndl.write('Hello!here')
