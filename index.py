from flask import Flask, render_template, make_response

app = Flask(__name__)
visit_count = 0

@app.route('/')
def index():
    global visit_count
    visit_count += 1
    response = make_response(render_template('index.html', count=visit_count))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/home')
def home():
    return 'Home Page Route'

@app.route('/about')
def about():
    return 'About Page Route'

@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'

@app.route('/contact')
def contact():
    return 'Contact Page Route'

@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text