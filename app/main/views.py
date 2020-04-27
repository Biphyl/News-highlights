from flask import render_template
from . import main

# Views 
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'News Highlights'
    
    return render_template('index.html')

@main.route('/articles/<id>')
def articles(id):
    '''
    View source page function that returns the source details page and its data
    '''
    return render_template('articles.html')