#!python3

from random import randint
from flask import Flask
import sample

app = Flask(__name__)


@app.route('/')
def index():
    return sample.generate_sentence('fish.txt', randint(6, 15))


if __name__ == "__main__":
    app.run()
