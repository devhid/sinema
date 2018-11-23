from ..extensions import db
"""
CREATE TABLE Producers(
    ProducerId INTEGER,
    MovieId INTEGER,

    PRIMARY KEY(ProducerId, MovieId),
    FOREIGN KEY(MovieId) REFERENCES Movie(Id),
    FOREIGN KEY(ProducerId) REFERENCES Person(Id)
);
"""
class Producers(db.Model):
    producer_id = db.Column(db.Integer(), db.ForeignKey('person.person_id'), primary_key=True, nullable=False)
    movie_id = db.Column(db.Integer(), db.ForeignKey('movie.movie_id'), primary_key=True, nullable=False)

    def __repr__(self):
        return 'Producers(producer_id={}, movie_id={})' \
            .format(self.actor_id, self.movie_id)