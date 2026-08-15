import nltk

nltk.download("averaged_perceptron_tagger_eng")

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "The student is learning NLP."

tokens = word_tokenize(text)

tags = pos_tag(tokens)

print(tags)