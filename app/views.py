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
    top_headlines = get_news('top-headlines?sources=techcrunch')
    wall_street_journal = get_news('everything?domains=wsj.com')
    tesla = get_news('everything?q=tesla&from=2021-05-05&sortBy=publishedAt')
    title = "Welcome to NewsHub"
    return render_template('index.html', title=title, top_headlines=top_headlines, wall_street_journal=wall_street_journal, tesla=tesla)
