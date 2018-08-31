from flask import render_template
from app import app
@app.route('/')
def index():

    title='welcome to news highter'
    return render_template('index.html', title=title)
