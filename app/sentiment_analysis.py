from textblob import TextBlob

def get_polarity(text):
	blob = TextBlob(text)
	for sentence in blob.sentences:
		return sentence.sentiment
