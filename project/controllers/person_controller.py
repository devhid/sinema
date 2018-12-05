from ..models import movie, person, actors, writers, directors

def get_actors_by_movie(movie_id):
    actor_tuples = actors.Actors.query.filter_by(movie_id=movie_id)
    if not actor_tuples:
        return ['N/A']
    
    actor_ids = [actor_tuple.actor_id for actor_tuple in actor_tuples]
    person_tuples = [person.Person.query.get(actor_id) for actor_id in actor_ids]

    actor_names = ", ".join([actor.first_name + " " + actor.last_name for actor in person_tuples])

    return actor_names

def get_directors_by_movie(movie_id):
    director_tuples = directors.Directors.query.filter_by(movie_id=movie_id)
    if not director_tuples:
        return ['N/A']
    
    director_ids = [director_tuple.director_id for director_tuple in director_tuples]
    person_tuples = [person.Person.query.get(director_id) for director_id in director_ids]

    director_names = ", ".join([director.first_name + " " + director.last_name for director in person_tuples])

    return director_names

def get_writers_by_movie(movie_id):
    writer_tuples = writers.Writers.query.filter_by(movie_id=movie_id)
    if not writer_tuples:
        return ['N/A']
    
    writer_ids = [writer_tuple.writer_id for writer_tuple in writer_tuples]
    person_tuples = [person.Person.query.get(writer_id) for writer_id in writer_ids]

    writer_names = ", ".join([writer.first_name + " " + writer.last_name for writer in person_tuples])

    return writer_names