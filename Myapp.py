#from flask import (Flask, render_template, request, redirect,
#                   url_for, flash, send_from_directory, session)

from flask import Flask
from flask import render_template
import feedparser


app = Flask(__name__)

@app.route("/")#, methods=["GET"])
def index():


    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

