from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return 'hi'
@app.route('/about')
def about(): return 'about'
app.run(host='0.0.0.0', port=80)
