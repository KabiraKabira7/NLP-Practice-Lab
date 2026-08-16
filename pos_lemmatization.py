import nltk

nltk.download("averaged_perceptron_tagger_eng")
nltk.download("wordnet")

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()


def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return "a"
    elif tag.startswith("V"):
        return "v"
    elif tag.startswith("N"):
        return "n"
    elif tag.startswith("R"):
        return "r"
    else:
        return "n"


text = "The students are studying and playing football."

tokens = word_tokenize(text)

tags = pos_tag(tokens)

print("POS tags:")
print(tags)

print("\nLemmatized words:")

for word, tag in tags:
    pos = get_wordnet_pos(tag)
    lemma = lemmatizer.lemmatize(word, pos=pos)

    print(word, "→", lemma)