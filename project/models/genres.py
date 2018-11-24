from ..extensions import db
import enum

Genre = enum.Enum(
    value = 'Genre',
    names = [
        ('Action', 0),
        ('Anime', 1),
        ('Children and Family', 2),
        ('Classics', 3),
        ('Comedies', 4),
        ('Cult', 5),
        ('Documentaries', 6),
        ('Dramas', 7),
        ('Faith and Spirituality', 8),
        ('Horror', 9),
        ('Independent', 10),
        ('International', 11),
        ('LBGTQ', 12),
        ('Music and Musicals', 13),
        ('Romance', 14),
        ('SciFi and Fantasy', 15),
        ('Sports', 16),
        ('Stand-up Comedy', 17),
        ('Thrillers', 18)
    ]
)

"""
CREATE TABLE Genres(
    Genre ENUM('Action', 'Anime', 'Children & Family', 'Classics', 'Comedies', 'Cult', 'Documentaries',
    'Dramas', 'Faith & Spirituality', 'Horror', 'Independent', 'International', 'LBGTQ', 'Music & Musicals',
    'Romance', 'Sci-Fi & Fantasty', 'Sports', 'Stand-up Comedy', 'Thrillers'), 
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



