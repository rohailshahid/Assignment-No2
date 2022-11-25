# Rana Rohail Shahid
from sklearn.feature_extraction.text import CountVectorizer

document = ["How are you ","It's a pleasure To meet you","My dream is to work in Google Company"]

# Create a Vectorizer Object
vectorizer = CountVectorizer()

vectorizer.fit(document)

# Printing the identified Unique words along with their indices
print("Vocabulary: ", vectorizer.vocabulary_)

# Encode the Document
vector = vectorizer.transform(document)

# Summarizing the Encoded Texts
print("Encoded Document is:")
print(vector.toarray())