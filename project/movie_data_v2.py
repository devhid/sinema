from selenium import webdriver
import time
import requests
from selenium.webdriver.chrome.options import Options
import json
import re

OMDB_API_KEY='20040681'

month_map = {
    'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04',
    'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08',
    'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'
}

options = Options()
options.set_headless(headless=True)

pattern = re.compile('{.+}')

def get_movie_info(imdbid):
    browser = webdriver.Chrome(options=options)

    url = 'https://www.omdbapi.com/?apikey={apikey}&i={imdbid}'.format(apikey=OMDB_API_KEY, imdbid=imdbid)
    browser.get(url)

    time.sleep(0.2)

    response = browser.execute_script("return document.body.innerHTML")
    json_string = pattern.search(response).group()

    fields = json.loads(json_string)

    browser.quit()

    if fields['Response'] == 'False': return {}
    if fields['Type'] != 'movie': return {}
    if fields['Poster'] == 'N/A': return {}
    if requests.get(fields['Poster']).status_code == 404: return {}
    if fields['Runtime'] == 'N/A': return {}
    if len(fields['Released'].split()) != 3: return {}

    release_date = fields['Released'].split()
    title = fields['Title']
    synopsis = fields['Plot']
    release_date = "{}-{}-{}".format(release_date[2], month_map[release_date[1]], release_date[0])
    maturity_rating = 'NR' if fields['Rated'] == 'NOT RATED' or fields['Rated'] == 'N/A' else fields['Rated']
    duration = int(fields['Runtime'].split()[0])
    genres = fields['Genre'].split(', ')
    director = fields['Director'].split(' ')
    actors = clean_names(fields['Actors'])
    writers = clean_names(fields['Writer'])
    rating = round(float(0.0 if fields['imdbRating'] == 'N/A' else fields['imdbRating']) / 2.0, 1)
    movie_art_url = fields['Poster']

    return {
        'movie_name': title, 'synopsis': synopsis, 'release_date': release_date,
        'rating': rating, 'maturity_rating': maturity_rating, 'duration': duration,
        'genres': genres, 'director': director, 'actors': actors, 'writers': writers, 
        'movie_art_url': movie_art_url
    }

def clean_names(names):
    cleansed = []
    unique = set()

    for n in re.sub('\(.+?\)', '', names).split(', '):
        unique.add(n)
    
    for n in unique:
        name = n.strip().split(' ')
        if len(name) == 1:
            cleansed.append([name[0], ""])
        if len(name) == 2:
            cleansed.append([name[0], name[1]])
        if len(name) >= 3:
            cleansed.append([name[0], name[len(name) - 1]])
    
    return cleansed


