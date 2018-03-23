from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from checker import read_status

app = Flask(__name__)

cron = BackgroundScheduler(daemon=True)
# Explicitly kick off the background thread

@app.route("/")
def hello():
    return read_status()

if __name__ == '__main__':
    cron.add_job(hello, 'cron', id='hello', second=5)
    cron.start()
    app.run()