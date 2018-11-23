from ..extensions import db
"""
CREATE TABLE Directors(
    DirectorId INTEGER,
    MovieId INTEGER,

    PRIMARY KEY(DirectorId, MovieId),
    FOREIGN KEY(MovieId) REFERENCES Movie(Id),
    FOREIGN KEY(DirectorId) REFERENCES Person(Id)
);

"""
class Directors(db.Model):
    director_id = db.Column(db.Integer(), db.ForeignKey('person.person_id'), primary_key=True, nullable=False)
    movie_id = db.Column(db.Integer(), db.ForeignKey('movie.movie_id'), primary_key=True, nullable=False)

    def __repr__(self):
        return 'Directors(director_id={}, movie_id={})' \
            .format(self.director_id, self.movie_id)