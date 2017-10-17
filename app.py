#!python3
"""main script, uses other modules to generate sentences"""
# from python_script import markov
# from python_script import Histogram_oop 
# from Histogram_oop import Dictogram
from random import randint
from flask import Flask, request, jsonify, render_template, json
import markov
import cleanup
import twitter
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table
import twitter
from dictogram import Dictogram
import time
import os

"""Use SQLAlchemy database to store current tweets in the sqlite db 
tweets is the list of tweet storage for the tweet string generating
old route / handle both Get and Post request
index handles the Get request for Word Generation when we refresh the page
new routes
route /tweet handles the post request for the twitter API
route /favorites handles all the favorite tweet data
route / get_tweet helps to get new tweet when the button is being clicked

"""

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
tweets = []
file_name = './text/complete_cleaned.txt'
cleaned_file = cleanup.clean_file(file_name)
markov_chain = markov.markov_model(cleaned_file)
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
        tweet = markov.generate_sentence(15, markov_chain)
        #tweet = dictogram.generate_sentence(num)
        #random_sentence = markov.generate_random_sentence_n(140, data_structure)

        return render_template('index.html', tweet=tweet, time=time.time)
    # how to store them in the database? I'm not sure
    #uncomment the lines to take of the Sqlite feature
    # elif request.method == 'POST':
    #     # if currentTweet not in db:
    #     addFavoriteTweet(currentTweet)
    #     return render_template('index.html', tweet=currentTweet, time=time.time)


"""main script, uses various different routes modules to generate sentences"""
# cal the tweet method

@app.route('/tweet', methods=['POST'])
def tweet():
    body = json.loads(request.data)
    # noinspection PyBroadException
    try:
        twitter.tweet = tweets[body['tweet']]
        print(twitter.tweet)
        print(jsonify)
        return jsonify({
            "success": True
        })
    except Exception as e:
        print(jsonify)
        return jsonify({
            "success": False
        })

@app.route('/favorites', methods=['GET', 'POST'])
def fav():
    # this function gets content of tweets in db
    sentence = markov.generate_sentence(15, markov_chain)

    tweets_list = Tweet.query.all()
    tweet_strings = []
    print("Printing all content")
    for tweet in tweets_list:
        tweet_strings.append(tweet.content)
    print(jsonify)
    return jsonify({
        "success": True,
        "data": sentence,
    })

    #return render_template('favorites.html', tweet=tweet_strings)

@app.route('/favorite_tweet', methods=['GET'])
def get_favorite_tweets():
    return jsonify({
        "success": True,
        "data": favorites
    })

@app.route('/get_tweet',methods=['GET', 'POST'])
def generate_new_tweet():

    sentence = markov.generate_sentence(15, markov_chain)

    tweets_list = Tweet.query.all()
    tweet_strings = []
    print("Printing all content")
    for tweet in tweets_list:
        tweet_strings.append(tweet.content)
    print(jsonify)
    return jsonify({
        "success": True,
        "data": sentence,
    })

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

    app.run(debug = True)