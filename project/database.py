from .movie_data import get_movie_info
from .models import person, movie, actors, writers, directors, genres

imdb_ids = "tt0108052,tt0083866,tt0082971,tt3778644,tt3748528,\
            tt0319343,tt1386588,tt0838283,tt1772341,tt0371746,\
            tt1228705,tt1300854,tt0443453,tt2582846,tt0989757,\
            tt1099212,tt1702439,tt0468569,tt1375666,tt0172495,\
            tt0120815,tt1345836,tt0133093,tt0499549,tt0988045,\
            tt5215952,tt0289043,tt1139797,tt5700672,tt1457767,\
            tt6644200,tt3235888,tt1591095".split(',')

def populate_database(db):
    for imdbid in imdb_ids:
        movie_info = get_movie_info(imdbid=imdbid)

        if not movie_info: continue

        movie_id = add_movie(db, movie_info)

        for genre in movie_info['genres']:
            add_genre(db, genre, movie_id)
        
        all_people = movie_info['actors'] + movie_info['writers'] + [movie_info['director']]

        for p in all_people:
            person_sql = person.Person.query.filter_by(first_name=p[0], last_name=p[1])

            if(person_sql.count() > 1):
                person_sql = person_sql.first()

                person_sql.is_actor = True if [person_sql.first_name, person_sql.last_name] in movie_info['actors'] else person_sql.is_actor
                person_sql.is_writer = True if [person_sql.first_name, person_sql.last_name] in movie_info['writers'] else person_sql.is_writer
                person_sql.is_director = True if person_sql.first_name == movie_info['director'][0] and person_sql.last_name == movie_info['director'][1] else person_sql.is_director
                
                continue
            
            person_id = add_person(db, p[0], p[1])
            person_sql = person.Person.query.get(person_id)

            if p in movie_info['actors']:
                person_sql.is_actor = True
                add_actor(db, person_id, movie_id)
            
            if p in movie_info['writers']:
                person_sql.is_writer = True
                add_writer(db, person_id, movie_id)
            
            if p[0] == movie_info['director'][0] and p[1] == movie_info['director'][1]:
                person_sql.is_director = True
                add_director(db, person_id, movie_id)

def add_movie(db, movie_info):
    new_movie = movie.Movie(
        movie_name=movie_info['movie_name'],
        synopsis=movie_info['synopsis'],
        rating=movie_info['rating'],
        minutes_duration=movie_info['duration'],
        release_date=movie_info['release_date'],
        maturity_rating=movie_info['maturity_rating'],
        movie_art_url=movie_info['movie_art_url']
    )

    db.session.add(new_movie)
    db.session.commit()

    return new_movie.movie_id

def add_genre(db, genre, movie_id):
    if not validate_genre(genre): return

    new_genre = genres.Genres(
        movie_id=movie_id,
        genre=genre
    )

    db.session.add(new_genre)
    db.session.commit()

def add_person(db, first_name, last_name):
    new_person = person.Person(
        first_name=first_name,
        last_name=last_name
    )

    db.session.add(new_person)
    db.session.commit()

    return new_person.person_id

def add_actor(db, person_id, movie_id):
    new_actor = actors.Actors(
        actor_id=person_id,
        movie_id=movie_id
    )

    db.session.add(new_actor)
    db.session.commit()

def add_director(db, person_id, movie_id):
    new_director = directors.Directors(
        director_id=person_id,
        movie_id=movie_id
    )

    db.session.add(new_director)
    db.session.commit()

def add_writer(db, person_id, movie_id):
    new_writer = writers.Writers(
        writer_id=person_id,
        movie_id=movie_id
    )

    db.session.add(new_writer)
    db.session.commit()

def validate_genre(genre):
    return genre in genres.get_genres()