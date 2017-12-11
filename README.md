# Python Tweet Generator

Contributers&ensp;·&ensp;[Jeff Chiu](https://jeffchiucp.github.io/portfolio/)

> Python Tweet Generator is a light weight Markov Model implemented into python


## Installation

Installation is super friendly using `pip`

```
$ pip install 
$ python app.py
```

### Deployment
Install the Heroku toolbelt.
```
heroku create myapp
git push heroku master
```

## Documentation

* [Quickstart](./quickstart.md)


## Usage
Avaliable online at https://shakespeare-tweet.herokuapp.com

## Example

**What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?**

    -`app.py` - main script for my Flask Server, it uses other modules to generate sentences 
    -`cleanup.py` - module for cleaning up source text and generates corpus.txt
    - `histogram.py` - grabs a list of words from a body of text
    - `dictogram.py` - refactoring histogram class to Dictogram class which helps to generates the random_weighted_words
    - `sample.py` - handles all the percentage handling and creating a list of words+occurrences and makes a text file for it.
    - `markov.py` - Markov model module generating tweet sentence word from generate_markov_model 

- In Progress Code
    - `crawler.py` # module for creating lists of tokens from a text
    - `markov.py` # Markov model module generating a sentence word from 81490 Shakespeare corpus
    - `twitter.py` # calling the Twitter API  

