from flask import Flask, render_template
from textblob import TextBlob
import crawler
import sentiment_analysis

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home(): 
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def get_results():
    result = crawler.get_lyrics("jamesblunt", "staythenight")
    polarity = sentiment_analysis.get_polarity(result)
    return polarity
