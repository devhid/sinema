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

class Genres(db.Model):
        movie_id_genre = db.Column(db.Integer, primary_key=True, nullable=False, db.ForeignKey('movie.movie_id'))
        genre = db.Column(db.Enum(Genre), primary_key=True, nullable=False)

        def __repr__(self):
            return 'Movie( \
                        movie_id_genre={}, genre={} \
                    )'.format(self.movie_id_genre, maturity_rating)



