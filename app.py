#!python3

from random import randint
from flask import Flask
from python_script import sample

app = Flask(__name__)


@app.route('/')
def index():
    return sample.generate_sentence('./text/output_data.txt', randint(10, 15))


if __name__ == "__main__":
    app.run()
