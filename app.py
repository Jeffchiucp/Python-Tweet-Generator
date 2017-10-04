#!python3
"""main script, uses other modules to generate sentences"""
from random import randint
from flask import Flask, request, render_template, json
import helper
from python_script import sample
from python_script import markov
from python_script import Histogram_oop 
from Histogram_oop import Dictogram
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table
#import twitter
from dictogram import Dictogram
import time
import os

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

shakespeare_dictogram = Dictogram('./text/output_data.txt')
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(200), unique=True)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Tweet %r>' % self.content

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        num = request.args.get('num', default = 15, type = int)
        tweet = helper.random_sentence()
        #tweet = dictogram.generate_sentence(num)
        #random_sentence = markov.generate_random_sentence_n(140, data_structure)

        global currentTweet
        currentTweet = tweet
        return render_template('index.html', tweet=tweet, time=time.time)
    elif request.method == 'POST':
        # if currentTweet not in db:
            # addFavoriteTweet(currentTweet)
        return render_template('index.html', tweet=currentTweet, time=time.time)

"""main script, uses other modules to generate sentences"""

@app.route('/favorites', methods=['GET', 'POST'])
def fav():
    # this function gets content of tweets in db
    tweets_list = Tweet.query.all()
    tweet_strings = []
    print("Printing all content")
    for tweet in tweets_list:
        tweet_strings.append(tweet.content)
    return render_template('favorites.html', tweet=tweet_strings)


def addFavoriteTweet(tweet_content):
    tweet = Tweet(tweet_content)
    db.session.add(tweet)
    db.session.commit()
    print(Tweet.query.all())

def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print ('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()

if __name__ == "__main__":
    db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)