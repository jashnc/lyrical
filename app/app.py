from flask import Flask, render_template
import crawler

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home(): 
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def get_counts():
    result = crawler.get_lyrics("jamesblunt", "staythenight")
    return result
