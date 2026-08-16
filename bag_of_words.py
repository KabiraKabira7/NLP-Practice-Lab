from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love NLP",
    "I love Python",
    "NLP is powerful"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBag of Words matrix:")
print(X.toarray())