from ..extensions import db
"""
CREATE TABLE Writers(
    WriterId INTEGER,
    MovieId INTEGER,

    PRIMARY KEY(WriterId, MovieId),
    FOREIGN KEY(MovieId) REFERENCES Movie(Id),
    FOREIGN KEY(WriterId) REFERENCES Person(Id)
);
"""
class Writers(db.Model):
    writer_id = db.Column(db.Integer(), db.ForeignKey('person.person_id'), primary_key=True, nullable=False)
    movie_id = db.Column(db.Integer(), db.ForeignKey('movie.movie_id'), primary_key=True, nullable=False)

    def __repr__(self):
        return 'Writers(writer_id={}, movie_id={})' \
            .format(self.writer_id, self.movie_id)