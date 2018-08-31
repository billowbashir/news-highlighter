from flask import render_template
from app import app
from .request import get_source
@app.route('/')
def index():
    news_sources=get_source()
    print(news_sources)
    title='welcome to news highter'
    return render_template('index.html', title=title, sources=news_sources)
