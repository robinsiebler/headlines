import feedparser

from flask import Flask

__author__ = 'Robin Siebler'
__date__ = '4/8/2018'

app = Flask(__name__)

RSS_FEEDS = {'pycharm': 'https://blog.jetbrains.com/pycharm/feed/',
             'giveaway': 'http://feeds.feedburner.com/giveawayoftheday/feed',
             'bitsdujour': 'http://blog.bitsdujour.com/feeds/posts/default',
             'engadget': 'https://www.engadget.com/rss.xml',
             'gizmodo': 'https://gizmodo.com/index.xml'
             }


@app.route('/')
@app.route('/<publication>')
def get_news(publication='engadget'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1> Blog Headlines </h1>
            <b>{0}</b> <br/>
            <i>{1}</1> <br/>
            <p>{2}</p> <br/>
        </body>
    </html>""".format(first_article.get('title'), first_article.get('published'), first_article.get('summary'))


if __name__ == '__main__':
    app.run(port=5000)
