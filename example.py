import pickle

import spacy

s = spacy.load("en_core_web_sm")

pickle.dump(s, open("save.p", "wb"))

s = pickle.load(open("en_core_web_sm-3.2.0.p", "rb"))
