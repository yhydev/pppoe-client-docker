from flask import Flask
import os

app = Flask(__name__)

@app.route("/restart")
def restart():
    return os.popen(os.environ.get('APP_RESTART_PPPOE', "poff pppoe && pon pppoe")).read()

@app.route("/stop")
def stop():
    return os.popen(os.environ.get('APP_STOP_PPPOE', "poff pppoe")).read()

@app.route("/start")
def start():
    return os.popen(os.environ.get('APP_START_PPPOE', "pon pppoe")).read()

app.run(host='0.0.0.0', port=os.environ.get('APP_PORT', '5000'))