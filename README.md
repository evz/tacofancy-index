# TacoFancy Ingredient Index

An attempt at processing recipes stored in the [Tacofancy
Project](https://github.com/sinker/tacofancy) to build a searchable ingredient
index. Heavily inspired by the [LA Times Data
Desk](http://datadesk.latimes.com/posts/2013/12/natural-language-processing-in-the-kitchen/).

### Setting this thing up

Setup a Python virtualenv (using
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)) 
and ``pip install`` requirements:

``` bash
    $ mkvirtualenv index
    $ workon index
    $ pip install -r requirements.txt
```

Install NLTK requirements:

``` python
>>> import nltk
>>> nltk.download_shell()
```

This launches an interactive shell session within the python shell that will
prompt walk you through installing the nltk requirements.

### Make it work

Right now, it’s pretty unimpressive. Invoke the indexer script with a layer type
slug and recipe slug from the [Taco Randomizer
API](http://www.randomtaco.me/base_layers/),and it’ll try to identify a recipe 
step or an ingredient. It’s also almost always wrong because there isn’t really 
much training data and I don’t really know what I’m doing. Yet.

``` bash
    $ python indexer.py base_layers carnitas
```
