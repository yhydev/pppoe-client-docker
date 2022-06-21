from flask import Flask
import os

app = Flask(__name__)

@app.route("/restart")
def restart():
    return os.popen("poff pppon && pon pppon").read()

@app.route("/stop")
def restart():
    return os.popen("poff pppon").read()

@app.route("/start")
def restart():
    return os.popen("pon pppon").read()

app.run(host='0.0.0.0', port=os.environ.get('APP_PORT', '5000'))