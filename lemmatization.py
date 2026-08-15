from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


word = "studies"

print(lemmatizer.lemmatize(word))



word = "studies"

print(lemmatizer.lemmatize(word))


import nltk

nltk.download("wordnet")

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = [
    "playing",
    "played",
    "studies",
    "studying",
    "running",
    "better"
]

for word in words:
    print(word, "→", lemmatizer.lemmatize(word))
    

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("playing", pos="v"))
print(lemmatizer.lemmatize("played", pos="v"))
print(lemmatizer.lemmatize("running", pos="v"))    
    