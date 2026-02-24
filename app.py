from flask import Flask

import scraper
from scraper import html



app = Flask(__name__)

@app.route("/")
def send_request():
	return html
