#from flask import (Flask, render_template, request, redirect,
#                   url_for, flash, send_from_directory, session)

from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():

    p = feedparser.parse('https://news.yahoo.co.jp/rss/topics/top-picks.xml')
    titles = [entry.title for entry in p.entries]
    
    n = feedparser.parse('https://www.nhk.or.jp/rss/news/cat0.xml')
    nhk = [entry.title for entry in n.entries]
    
    m = feedparser.parse( 'https://rss.msn.com/ja-jp/')
    msn = [entry.title for entry in m.entries]

    g = feedparser.parse('http://news.goo.ne.jp/rss/topstories/gootop/index.rdf')
    goo = [entry.title for entry in g.entries]

    l = feedparser.parse('https://news.livedoor.com/topics/rss/top.xml')
    door = [entry.title for entry in l.entries]


    return render_template("index.html" , 
                          titles=titles, nhk=nhk, msn=msn, goo=goo, door=door )


if __name__ == "__main__":
    app.run(debug=True)

