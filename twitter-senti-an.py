import tweepy
from textblob import TextBlob


# please use your own authentication details, as this are invalid

consumer_key = "cKMGlwVjwVMtOuxzi9S2PyksY"
consumer_secret = "5Cw0cj0cd0LmhB8ObBN2HcdfrwrqpqqjU4GbX1IeQ2u9cAD0hn"

access_token = "593429683-n18LvfVRkDsR9ebzmJjgIgkiy8XvzT9GeG2kA0M6"
access_token_secret = "OKvopq1C3J9LwC3FwQz9o7WrjDbA4sNFJbzfmPzCE4yVJ"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Amazon')
x = 1
for tweet in public_tweets:
	print("------------------------------")
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	x = x+1
	if(x==10):
		break