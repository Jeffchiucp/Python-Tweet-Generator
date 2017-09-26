#!python3
"""main script, uses other modules to generate sentences"""
from random import randint
from flask import Flask, request, render_template
from python_script import sample
import time
app = Flask(__name__)


# @app.route('/')
# def index():
#     return sample.generate_sentence('./text/output_data.txt', randint(10,15))


@app.route('/', methods=['GET', 'POST'])
def hello():

    tweet = sample.generate_sentence('./text/output_data.txt', randint(10,15))
    if request.method == 'GET':
        return render_template('index.html', tweet=tweet, time=time.time)
    elif request.method == 'POST':
        print("Posting!")
        return render_template('index.html', tweet=tweet, time=time.time)


if __name__ == "__main__":
    app.run()
