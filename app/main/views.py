from flask import render_template
from app import app
from .request import get_source,get_articles
@app.route('/')
def index():
    # articles=get_articles(id)
    news_sources=get_source()
    print(news_sources)
    title='welcome to news highlighter'
    return render_template('index.html', title=title, sources=news_sources)


@app.route('/articles/<string:id>')
def source(id):
    articles=get_articles(id)
    print(articles)
    return render_template('articles.html',articles=articles)
