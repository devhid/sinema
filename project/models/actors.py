from ..extensions import db
"""
    CREATE TABLE Actors(
    ActorId INTEGER,
    MovieId INTEGER,

    PRIMARY KEY(ActorId, MovieId),
    FOREIGN KEY(ActorId) REFERENCES Person(Id),
    FOREIGN KEY(MovieId) REFERENCES Movie(Id)
);
"""

class Actors(db.Model):
    actor_id = db.Column(db.Integer(), db.ForeignKey('person.person_id'), primary_key=True, nullable=False)
    movie_id = db.Column(db.Integer(), db.ForeignKey('movie.movie_id'), primary_key=True, nullable=False)

    def __repr__(self):
        return 'Actors(actor_id={}, movie_id={})' \
            .format(self.actor_id, self.movie_id)