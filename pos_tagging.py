import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("averaged_perceptron_tagger_eng")

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "The student is learning NLP."

tokens = word_tokenize(text)

tags = pos_tag(tokens)

print(tags)


sentences = [
    "I will book a flight.",
    "I read a book."
]

for sentence in sentences:
    tokens = word_tokenize(sentence)
    tags = pos_tag(tokens)

    print("\nSentence:")
    print(sentence)

    print("POS tags:")
    print(tags)
    
    
    lemmatizer = WordNetLemmatizer()

text = "The students are studying and playing football."

tokens = word_tokenize(text)

tags = pos_tag(tokens)

print("POS tags:")
print(tags)