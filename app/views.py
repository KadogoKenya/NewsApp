from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting sources news
    
    source = get_sources('categogy')
    print(source)
    name = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', name= name,category=sources)   


@app.route('/new/<int:new_id>')
def new(new_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('new.html',id = new_id)