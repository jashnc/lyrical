from textblob import TextBlob

def get_polarity(text):
	blob = TextBlob(text)
	for sentence in blob.sentences:
		return get_rating(sentence.sentiment)

def get_rating(sentiment):
	rating = 'Neutral'
	if sentiment.polarity > 0.25:
		rating = 'Happy'
	elif sentiment.polarity <= 0.25:
		rating = 'Sad'
	return {'polarity': sentiment.polarity, 'rating': rating}