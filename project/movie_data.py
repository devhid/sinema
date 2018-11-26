from omdb import OMDBClient

API_KEY="698088bb"
client = OMDBClient(apikey=API_KEY)

month_map = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
}

def get_movie_info(imdbid):
    fields = client.get(imdbid=imdbid)
    if not fields:
        return ()

    title = fields['title']
    synopsis = fields['plot']
    release_date = fields['released'].split()
    release_date = "{}-{}-{}".format(release_date[2], month_map[release_date[1]], release_date[0])
    maturity_rating = 'NR' if fields['rated'] == 'NOT RATED' else fields['rated']
    duration = int(fields['runtime'].split()[0])
    genres = fields['genre'].split(', ')
    director = fields['director'].split(' ')
    actors = clean_names(fields['actors'].split(', '))
    writers = clean_names(fields['writer'].split(', '))
    rating = round(float(fields['imdb_rating']) / 2.0, 1)
    movie_art_url = fields['poster']

    return title, synopsis, release_date, rating, maturity_rating, duration, genres, director, actors, writers, movie_art_url

def clean_names(names):
    cleansed = []
    for n in names:
        name = n.split(' ')
        if len(name) == 1:
            cleansed.append([name[0], ""])
        if len(name) == 2:
            cleansed.append([name[0], name[1]])
        if len(name) >= 3:
            cleansed.append([name[0], name[len(name) - 1]])
    
    return cleansed;

