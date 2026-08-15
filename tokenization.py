text = "I love NLP! NLP is amazing, isn't it?"

print("Original text:")
print(text)

print("\nUsing split():")
print(text.split())




text = "I Love NLP! NLP is AMAZING, isn't it?"

print("Original text:")
print(text)

print("\nLowercase text:")
print(text.lower())

print("\nTokens:")
print(text.lower().split())


import string

text = "I Love NLP! NLP is AMAZING."

print("Original text:")
print(text)

text = text.lower()

print("\nLowercase:")
print(text)

for character in string.punctuation:
    text = text.replace(character, "")

print("\nWithout punctuation:")
print(text)

tokens = text.split()

print("\nTokens:")
print(tokens)