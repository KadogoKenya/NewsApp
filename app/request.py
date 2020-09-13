from app import app
import urllib.request,json
from .models import new

Source = new.Source

# Getting api key
api_key = app.config['SOURCE_API_KEY']

# Getting the movie base url
base_url = app.config["SOURCE_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None
        # results = []

        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        title = source_item.get('original_name')
        description=source_item.get('original_description')
        poster = movie_item.get('poster_path')
        # overview = movie_item.get('overview')
        # poster = movie_item.get('poster_path')
        # vote_average = movie_item.get('vote_average')
        # vote_count = movie_item.get('vote_count')

        if poster:
            source_object = Source(id,title,description)
            source_results.append(source_object)

    return source_results