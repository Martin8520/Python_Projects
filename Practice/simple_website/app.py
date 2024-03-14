from flask import Flask, render_template, request, redirect

app = Flask(__name__)
entries = []


@app.route('/')
def index():
    return render_template('index.html', entries=entries)


@app.route('/add_entry', methods=['POST'])
def add_entry():
    title = request.form['title']
    content = request.form['content']
    entries.append({'title': title, 'content': content})
    return redirect('/')
