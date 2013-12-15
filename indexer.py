import re
import requests
import nltk
import pickle
from nltk.classify import MaxentClassifier
from nltk.tag.simplify import simplify_wsj_tag

training = {
    'ingredient': [
        '* 1 packet of Taco Seasoning Mix',
        '* 1 bag of lentils',
        '* 1 tbs vegetable oil',
        '* 1/2 small onion, diced',
        '* A pile of chiles.',
        '* 1 cloves garlic, peeled'
    ],
    'step': [
        '1. Set the oven to 350 degrees. Put a Dutch Oven on the range and \
            apply medium heat.',
        '2. Chop up your pile of onions. Mince up the garlic. Heck -- get \
            a beer. This is good beer-drinking-cooking. And the chiles! \
            Chop them up too. That\'ll get you going.*',
        '3. Oh yeah -- cut your pork shoulder into hunks of roughly equal \
            size. I try to keep the hunks as big as possible. Coat it all \
            over with salt.',
        '4. Add a tablespoon or so of the oil of your choice to the Dutch \
            Oven (I use bacon fat). Once it\'s hot, toss in 1/2-1/3 of your \
            chopped onion. Cook the onion until it turns translucent; add \
            about half the chopped chiles and garlic, stir well, then add \
            the pork shoulder. Start them fat-side down, and try to get the \
            fat in contact with the dutch oven.',
        '5. Pop the whole works in the oven, uncovered (to start). Grab your \
            beer, and maybe a book. Time to do some structured waiting.',
        '6. Every thirty minutes or so, check the pork shoulder. Check the \
            stuff in the bottom of the pan; as it starts to dry out, throw \
            in more onions and stir it all around. You can flip the hunks over \
            after a while -- use tongs.'
    ]
}

def prepare_input(sentence):
    words = []
    sentences = nltk.sent_tokenize(sentence)
    for sent in sentences:
        words = words + nltk.word_tokenize(sent)
    pos = nltk.pos_tag(words)
    pos = [simplify_wsj_tag(tag) for word, tag in pos]
    words = [w.lower() for w in words]
    trigrams = nltk.trigrams(words)
    trigrams = ['%s/%s/%s' % (i[0], i[1], i[2]) for i in trigrams]
    features = words + pos + trigrams
    features = dict((f, True) for f in features)
    return features

def train():
    for k,v in training.items():
        for sentence in v:
            yield (prepare_input(sentence), k)

if __name__ == '__main__':
    import sys
    training_set = []
    for features in train():
        training_set.append(features)
    classifier = MaxentClassifier.train(training_set)
    layer_type, slug = sys.argv[1:3]
    r = requests.get('http://randomtaco.me/%s/%s/' % (layer_type, slug))
    recipe = r.json()['recipe']
    recipe_sentences = nltk.sent_tokenize(recipe)
    for sent in recipe_sentences:
        print classifier.classify(prepare_input(sent))
        print '*'*80




