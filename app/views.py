from flask import render_template, request
from app import app
from .models import News, News_details
from .requests import get_news, process_news, get_articles, process_articles

#Views
@app.route('/')
def index():
    '''
    View function that returns index page and its data
    '''
    sources = get_news('sources')
    title = "Welcome to NewsHub"
    return render_template('index.html', title=title, sources=sources)

@app.route('/articles')
def news():
    '''
    View function that returns index page and its data
    '''
    general = get_articles("general")
    return render_template('articles.html',general = general)


@app.route('/business')
def business():
    '''
    View function that returns index page and its data
    '''
    business = get_articles("business")
    return render_template('business.html', business=business)

@app.route('/entertainment')
def entertainment():
    '''
    View function that returns index page and its data
    '''
    entertainment = get_articles("entertainment")
    return render_template('entertainment.html', entertainment=entertainment)

@app.route('/sports')
def sports():
    '''
    View function that returns index page and its data
    '''
    sports = get_articles("sports")
    return render_template('sports.html', sports=sports)

@app.route('/technology')
def technology():
    '''
    View function that returns index page and its data
    '''
    technology = get_articles("technology")
    return render_template('technology.html', technology=technology)

@app.route('/health')
def health():
    '''
    View function that returns index page and its data
    '''
    health = get_articles("health")
    return render_template('health.html', health=health)
