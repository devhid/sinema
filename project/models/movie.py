from ..extensions import db
import enum
import simplejson as json

MaturityRating = enum.Enum(
    value = 'MaturityRating',
    names = [
        ('NR', 0),
        ('TV-Y', 1),
        ('TV-Y7', 1),
        ('TV-G', 1),
        ('G', 1),
        ('TV-PG', 2),
        ('PG', 2),
        ('PG-13', 3),
        ('TV-14', 3),
        ('TV-MA', 4),
        ('R', 4),
        ('NC-17', 5)
    ]
)

"""
CREATE TABLE Movie(
    Id INTEGER,
    MovieName VARCHAR(255) NOT NULL,
    Synopsis VARCHAR(255) DEFAULT 'No synopsis available yet for this movie.',
    Rating FLOAT(2, 1) DEFAULT 0.0 CHECK (Rating=0.0 OR (Rating >= 1.0 AND Rating <= 5.0)),
    MinutesDuration INTEGER CHECK (MinutesDuration >= 0),
    ReleaseDate DATE,
    MaturityRating ENUM('NR', 'TV-Y', 'TV-Y7', 'TV-G', 'G', 'PG', 'PG-13', 'PG-13', 'TV-14', 'TV-MA', 'R', 'NC-17') DEFAULT 'NR',
    PRIMARY KEY (Id)
);
"""

class Movie(db.Model):
    movie_id = db.Column(db.Integer(), primary_key=True, nullable=False)
    movie_name = db.Column(db.String(255), nullable=False)
    synopsis = db.Column(db.String(255), server_default='No synopsis available yet for this movie.')
    rating = db.Column(db.Float(2,1), db.CheckConstraint('rating=0.0 OR (rating >= 1.0 AND rating <= 5.0)'), default=0.0)
    minutes_duration = db.Column(db.Integer, db.CheckConstraint('minutes_duration >= 0'))
    release_date = db.Column(db.Date())
    maturity_rating = db.Column(db.Enum(MaturityRating), server_default='NR')
    movie_art_url = db.Column(db.String(255)) 
    genres = db.relationship('Genres', backref='movie', lazy=True)

    def serialize(self): 
        return json.dumps({
            'movie_id': self.movie_id,
            'movie_name': self.movie_name,
            'synopsis': self.synopsis,
            'rating': self.rating,
            'minutes_duration': self.minutes_duration,
            'release_date': self.release_date.__str__(),
            'maturity_rating': self.maturity_rating.__str__(),
            'movie_art_url': self.movie_art_url
        })

    def __repr__(self):
        return 'Movie( \
                        movie_id={}, movie_name={}, synopsis={}, \
                        rating={}, minutes_duration={}, release_date={}\
                        maturity_rating={}, movie_art_url={} \
                    )'.format(
                        self.movie_id, self.movie_name, self.synopsis, 
                        self.rating, self.minutes_duration, self.release_date, 
                        self.maturity_rating, self.movie_art_url
                    )