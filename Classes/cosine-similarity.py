
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ["London Paris London", "Paris Paris London"]
vectorizer = CountVectorizer()


# tokenize and build vocab

# summarize

# encode document
vector = vectorizer.fit_transform(text)
# summarize encoded vector
print(vector)
varray = vector.toarray()
print(varray)
similarity = cosine_similarity(varray)
print(similarity)
