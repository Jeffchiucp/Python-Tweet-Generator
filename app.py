#!python3
"""main script, uses other modules to generate sentences"""
from random import randint
from flask import Flask, request, jsonify, render_template, json
import cleanup
import markov
import twitter
import psycopg2
import sys
from dictogram import Dictogram
import time
import os

""" Code changes 
Remove SQLAlchemy (SQLlite3)database and use Postgres Database instead
Heroku supports Postgres store current tweets in the sqlite db 
# https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71?gi=fffbc546fa6b
# Markov Chain
tweets is the list of tweet storage for the tweet string generating
old route / handle both Get and Post request index handles 
the Get request for Word Generation 
changes the routes so user don't have to refresh every time 
route /tweet handles the post request for the twitter API
route /favorites handles all the favorite tweet data
route / get_tweet helps to get new tweet when the button is being clicked

Included Source Citation:
Copied Postgres Codes and Tweet Routes from Avery GitHub
https://github.com/Avery246813579/Obama-Speech-Quote-Generator/blob/master/app.py

"""

app = Flask(__name__, instance_relative_config=True)
file_name = './text/shakespeare.txt'
cleaned_file = cleanup.clean_file(file_name)
markov_chain = markov.markov_model(cleaned_file)

#Postgres library to connect to Heroku DB
#tweet is the list of tweet stored for the twitter API routing 
conn = psycopg2.connect("dbname=d2bggd7r2dh3bk user=mjbapfvphmennc password=" +
                        os.environ.get('DATABASE_PASSWORD') + " host=" + os.environ.get('DATABASE_HOST'))
cur = conn.cursor()
cur.execute("SELECT * FROM Tweets;")
tweets = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        num = request.args.get('num', default = 15, type = int)
        tweet = markov.generate_sentence(15, markov_chain)
        #tweet = dictogram.generate_sentence(num)
        #random_sentence = markov.generate_random_sentence_n(140, data_structure)

        return render_template('index.html', tweet=tweet, time=time.time)
    # how to store them in the database? I'm not sure

"""main script, uses various different routes modules to generate sentences"""

@app.route('/tweet', methods=['POST'])
def tweet():
    body = json.loads(request.data)
    try:
        twitter.tweet = tweets[body['tweet']]
        twitter.tweet(tweet_value)
        # print(twitter.tweet)
        return jsonify({
            "success": True
        })
    except Exception as e:
        return jsonify({
            "success": False
        })

@app.route('/favorites', methods=['GET', 'POST'])
def fav():
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

@app.route('/favorite_tweet', methods=['GET'])
def get_favorite_tweets():
    return jsonify({
        "success": True,
        "data": favorites
    })

@app.route('/new',methods=['POST'])
def generate_new_tweet():
    sentence = markov.generate_sentence(15, markov_chain)

    body = json.loads(request.data)

    words = body['words']

    sentence = None
    if words is None:
        sentence = markov.generate_sentence(15, markov_chain)
    else:
        try:
            sentence = markov.generate_sentence(15, markov_chain)
        except TypeError:
            sentence = markov.generate_sentence(15, markov_chain)

    tweets.append(sentence)
    return jsonify({
        "success": True,
        "data": sentence,
        "id": len(tweets) - 1
    })
if __name__ == "__main__":
    app.run(debug = True)
