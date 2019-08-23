import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#to fetch data and format

data = fetch_movielens(min_rating=4.0)
print(data)

#printtraining and testing data

print(repr(data['train']))
print(repr(data['test']))


# creating of model -  We will store a model by creating a variable called model
# Loss - it measures the difference between the model's predection and desired output
# warp - Weighted approximate - Rank Pairwise(a method in loss function used to minimize the training so that it gets more accurate to our model)
# warp - Here it is used to create recommendations for each user by looking at the existing users writing pairs and predicting rankings for each.
# warp - It uses the gradient descent algorithm to iteratively to find the way then imprve our predection over time.
# warp - It is Hybrid system which predicts according with both content + collaborative.  

model = LightFM(loss='warp')

#Traing of module
# Fit method of model object to train it.
model.fit(data['train'], epochs=30, num_threads=2)

# TO generate a recomendation, to generate it we will wite a sample function with 3 parameters.

def sample_recommendation(model,data,user_ids):

	# number of users and movies in traning using the shape attribute of data dictionary to create it

	n_users, n_items = data['train'].shape

	# To generate recommendations for each user we input

	for user_id in user_ids:

		# movies they already like
		known_positivies = data['item_labels'][data['train'].tocsr()[user_id].indices]

		# movies our model predicts they will like

		scores = model.predict(user_id, np.arange(n_items))

		# rank them in order of most liked to least

		top_items = data['item_labels'][np.argsort(-scores)]

		#print out the results 

		print("user %s" % user_id)
		print("Known positivities:")

		for x in known_positivies[:3]:
			print("      %s" % x)

		print("recomended")

		for x in top_items[:3]:
			print(".    %s" % x)

sample_recommendation(model, data, [34,254,400])
