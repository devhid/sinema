from ..extensions import db
import enum

Genre = enum.Enum(
    value = 'Genre',
    names = [
        ('Action', 0),
        ('Adventure', 1),
        ('Biography', 2),
        ('Comedy', 3),
        ('Crime', 4),
        ('Documentary', 5),
        ('Drama', 6),
        ('Family', 7),
        ('Fantasy', 8),
        ('Horror', 9),
        ('International', 10),
        ('Music and Musicals', 11),
        ('Romance', 12),
        ('Sci-Fi', 13),
        ('Sport', 14),
        ('Thriller', 15)
    ]
)

def get_genres():
    return list(Genre.__members__.keys())

"""
CREATE TABLE Genres(
    Genre ENUM('Action', 'Adventure', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
    'Family', 'Fantasy', 'Horror', 'International', 'Music and Musicals',
    'Romance', 'Sci-Fi', 'Sport', Thriller'), 
    MovieId INTEGER,

    PRIMARY KEY(Genre, MovieId),
    FOREIGN KEY(MovieId) REFERENCES Movie(Id)
);
"""

class Genres(db.Model):
        movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'), primary_key=True, nullable=False)
        genre = db.Column(db.Enum(Genre), primary_key=True, nullable=False)

        def __repr__(self):
            return 'Movie(movie_id={}, genre={})'.format(self.movie_id_genre, maturity_rating)



