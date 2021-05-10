from flask import Flask, render_template, url_for, redirect
import backend

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', entry_list=backend.query_entries("none"))

@app.route('/latest')
def latest():
    return render_template('index.html', entry_list=backend.query_entries("latest"))

@app.route('/earliest')
def earliest():
    return render_template('index.html', entry_list=backend.query_entries("earliest"))

@app.route('/random')
def random():
    return render_template('index.html', entry_list=backend.query_entries("random"))

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        return render_template('upload.html')
    else:
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)