from flask import Flask, render_template, request
from textblob import TextBlob
import json
import crawler
import sentiment_analysis




app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home(): 
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def get_results():
	print request.get_json()
	artist = request.get_json().get('artist')
	title = request.get_json().get('title')
	print artist
	print title
	result = crawler.get_lyrics(artist, title)
	if isinstance(result, dict):
		polarity = sentiment_analysis.get_polarity(result['parsed'])
		song_obj = {
			'artist': artist,
			'title': title,
			'lyrics': result['lyrics'],
			'polarity': polarity['polarity'],
			'rating': polarity['rating']
		}
		print(polarity['polarity'])
		print(polarity['rating'])
		return json.dumps([song_obj])
	else:
		return json.dumps({'message': 'error'})

@app.route('/api/mood', methods=['POST'])
def get_mood_results():
	mood = request.get_json().get('mood')
	print mood
	sad_songs = [
		{
			'artist': 'Sufjan Stevens',
			'title': 'Casimir Pulaski Day'
		},
		{
			'artist': 'Hank Williams',
			'title': 'Im So Lonesome I Could Cry'
		},
		{
			'artist': 'Johnny Cash',
			'title': 'Hurt'
		},
		{
			'artist': 'The Magnetic Fields',
			'title': 'I Dont Believe In The Sun'
		},
		{
			'artist': 'Dolly Parton',
			'title': 'Jolene'
		}
	]

	happy_songs = [
		{
			'artist': 'Sia',
			'title': 'The Greatest'
		},
		{
			'artist': 'The Beach Boys',
			'title': 'Good Vibrations'
		},
		{
			'artist': 'James Brown',
			'title': 'I Got You (I Feel Good)'
		},
		{
			'artist': 'Blue Swede',
			'title': 'Hooked on a Feeling'
		},
		{
			'artist': 'Mika',
			'title': 'Love Today'
		}
	]

	song_array = sad_songs
	if mood == 'happy':
		song_array = happy_songs
	mood_results = []

	for song in song_array:
		result = crawler.get_lyrics(song['artist'], song['title'])
		polarity = sentiment_analysis.get_polarity(result['parsed'])
		song_obj = {
			'artist': song['artist'],
			'title': song['title'],
			'lyrics': result['lyrics'],
			'polarity': polarity['polarity'],
			'rating': polarity['rating']
		}
		mood_results.append(song_obj)
	return json.dumps(mood_results)




# Song title aritst lyrics polarity sadness rating