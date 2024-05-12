from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return 'hi, here\'s <a href="/lambda">lambda</a>'
@app.route('/about')
def about(): return 'about'
app.run(host='0.0.0.0', port=80)
