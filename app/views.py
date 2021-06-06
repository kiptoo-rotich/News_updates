from flask import render_template, request
from app import app
from .models import News
from .requests import get_news, process_news

#Views
@app.route('/')
def index():
    '''
    View function that returns index page and its data
    '''
    sources = get_news('sources')
    title = "Welcome to NewsHub"
    return render_template('index.html', title=title, sources=sources)

@app.route('/news')
def news():
    '''
    View function that returns index page and its data
    '''
    
    return render_template('news.html', title=title, )
