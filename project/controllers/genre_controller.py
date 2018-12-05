from ..models import movie, genres

def get_genres_by_movie(movie_id):
    genre_tuples = genres.Genres.query.filter_by(movie_id=movie_id)
    if not genre_tuples:
        return ['N/A']
    
    movie_genres = ", ".join([strip_enum(genre_tuple.genre) for genre_tuple in genre_tuples])

    return movie_genres

def strip_enum(enum_member):
    return str(enum_member).replace('Genre.', '')