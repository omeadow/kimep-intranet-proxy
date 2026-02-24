from flask import Flask

app = Flask(__name__)

@app.route("/")
def send_request():
	return "send request"
