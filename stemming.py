from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "play",
    "playing",
    "played",
    "studies",
    "studying",
    "connection",
    "connected",
    "running",
    "better"
]

for word in words:
    print(word, "→", stemmer.stem(word))