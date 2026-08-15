import nltk

nltk.download("stopwords")

from nltk.corpus import stopwords

text = "The student is learning NLP in the classroom."

stop_words = set(stopwords.words("english"))

tokens = text.lower().split()

filtered_tokens = []

for token in tokens:
    if token not in stop_words:
        filtered_tokens.append(token)

print("Original tokens:")
print(tokens)

print("\nAfter stop-word removal:")
print(filtered_tokens)


from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "play"]

for word in words:
    print(word, "→", stemmer.stem(word))