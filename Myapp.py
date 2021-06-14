#from flask import (Flask, render_template, request, redirect,
#                   url_for, flash, send_from_directory, session)

from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    titles=[]
    yahoop_URL = 'https://news.yahoo.co.jp/rss/topics/top-picks.xml'
    p = feedparser.parse(yahoop_URL)
    for entry in p.entries:
        titles.append(entry.title)


    nhk=[]
    NHK_URL = 'https://www.nhk.or.jp/rss/news/cat0.xml'
    N = feedparser.parse(NHK_URL)
    for entry in N.entries:
        nhk.append(entry.title)

    msn=[]
    msn_URL = 'https://rss.msn.com/ja-jp/'
    M = feedparser.parse(msn_URL)
    for entry in M.entries:
        msn.append(entry.title)

    goo=[]
    goo_URL = 'http://news.goo.ne.jp/rss/topstories/gootop/index.rdf'
    G = feedparser.parse(goo_URL)
    for entry in G.entries:
        goo.append(entry.title)

    door=[]
    door_URL = 'https://news.livedoor.com/topics/rss/top.xml'
    L = feedparser.parse(door_URL)
    for entry in L.entries:
        door.append(entry.title)

    return render_template("index.html" , 
                          titles=titles, nhk=nhk, msn=msn, goo=goo, door=door )


if __name__ == "__main__":
    app.run(debug=True)

