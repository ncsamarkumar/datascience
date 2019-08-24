import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
##################################################

##Step 1: Read CSV File

df = pd.read_csv("movie_dataset.csv")
#print(df.head())
#print(df.columns)

##Step 2: Select Features

features = ['keywords','cast','genres','director']

##Step 3: Create a column in DF which combines all selected features
for feature in features:
	df[feature] = df[feature].fillna('')

def combined_features(row):
	try:
		return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
	except:
		print ("Error", row)

df["combined_features"] = df.apply(combined_features,axis=1)

#print (df["combined_features"].head())

##Step 4: Create count matrix from this new combined column

vectorizer = CountVectorizer()

count_matrix = vectorizer.fit_transform(df["combined_features"])
print(count_matrix)
##Step 5: Compute the Cosine Similarity based on the count_matrix

similarity = cosine_similarity(count_matrix)
print(similarity)

movie_user_likes = "Avatar"

## Step 6: Get index of thi s movie from its title

movie_index = get_index_from_title(movie_user_likes)

similar_movies = list(enumerate(similarity[movie_index]))

## Step 7: Get a list of similar movies in descending order of similarity score

sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

## Step 8: Print titles of first 50 movies
i = 0

for movie in sorted_similar_movies:
	print(get_title_from_index(movie[0]))
	i = i+1
	if(i>10):
		break