from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home(): 
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def get_counts():
    return "Hello from the backend"
