from project.celery import app
import time

@app.task
def hello_world():
    print("Linuxcao is a nice man")
    time.sleep(5)
    print("Linuxcao is a handsome man")