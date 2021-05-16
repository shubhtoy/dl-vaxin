from flask import Flask, render_template, redirect
from requests.api import request
from apscheduler.schedulers.background import BackgroundScheduler


import requests
import time
import datetime

datas_ = []
keys = []
# import jsoncodes=[]

# a.status_code = 11
def update():
    print("UPDATING....")
    global datas_, keys
    a = requests.get("https://short.smittal.tech/api")
    data = a.json()
    datas_ = data["datas_"]
    keys = data["keys"]
    print("UPDATED")


sched = BackgroundScheduler(daemon=True)
sched.add_job(update, "interval", minutes=1, max_instances=1)
sched.start()

app = Flask(__name__)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "no-cache,no-store"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/45+")
def hello():
    if len(keys) == 0:
        return redirect("/")
    return render_template(
        "table.html",
        data_keys=keys[0],
        data_values=datas_[0],
    )


@app.route("/18")
def eighteen():
    if len(keys) == 0:
        return redirect("/")
    return render_template("table.html", data_values=datas_[1], data_keys=keys[1])


if __name__ == "__main__":
    app.run(debug=True)