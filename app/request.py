# import urllib.request,json
# from .models import Map
# from app import app

# base_url = None
# base_url = app.config['BLOG_API_BASE_URL']

# def configure_request(app):
#     global base_url
    

# def get_map():

#     get_movies_url = base_url
  
#     print(base_url)

#     with urllib.request.urlopen(base_url) as url:
#         get_quotes_data = url.read()
#         get_quotes_response = json.loads(get_quotes_data)

#         quote_object = None

#         if get_quotes_response:
#             id=get_quotes_response.get('id')
#             author=get_quotes_response.get('author')
#             quote=get_quotes_response.get('quote')
#             quote_object = Map(id,author,quote)

#     return quote_object


import urllib.request,json
from .models import Map

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


