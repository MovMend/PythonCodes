import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#helper functions
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]


#Reading the csv file 
df = pd.read_csv("movie_dataset.csv")
#print df.columns

#The important columns of the dataset
features = ['keywords','cast','genres','director']
#Combining all the important features
for feature in features:
	df[feature] = df[feature].fillna('')

def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print ("Error:", row)	

df["combined_features"] = df.apply(combine_features,axis=1)

#print "Combined Features:", df["combined_features"].head()

# A matrix is created
cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

#Computing cosine similarity on the count_matrix
cosine_sim = cosine_similarity(count_matrix) 
movie_user_likes = "Harry Potter and the Half-Blood Prince"

#Getting index of the movies
movie_index = get_index_from_title(movie_user_likes)

similar_movies =  list(enumerate(cosine_sim[movie_index]))

#Get a list of similar movies in descending order of similarity score
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

#printing titles of the first 8 similar recommended movies
i=0
for element in sorted_similar_movies:
		print (get_title_from_index(element[0]))
		i=i+1
		if i>8:
			break