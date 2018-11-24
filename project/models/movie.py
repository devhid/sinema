from ..extensions import db
import enum

MaturityRating = enum.Enum(
    value = 'MaturityRating',
    names = [
        ('NR', 0),
        ('G', 1),
        ('PG', 2),
        ('PG-13', 3),
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
    SecondsDuration INTEGER CHECK (SecondsDuration >= 0 AND SecondsDuration <= 60),
    ReleaseDate DATE,
    MaturityRating ENUM('NR', 'G', 'PG', 'PG-13', 'R', 'NC-17') DEFAULT 'NR',
    PRIMARY KEY (Id)
);
"""

class Movie(db.Model):
    movie_id = db.Column(db.Integer(), primary_key=True, nullable=False)
    movie_name = db.Column(db.String(255), nullable=False)
    synopsis = db.Column(db.String(255), server_default='No synopsis available yet for this movie.')
    rating = db.Column(db.Float(2,1), db.CheckConstraint('rating=0.0 OR (rating >= 1.0 AND rating <= 5.0)'), default=0.0)
    minutes_duration = db.Column(db.Integer, db.CheckConstraint('minutes_duration >= 0'))
    seconds_duration = db.Column(db.Integer, db.CheckConstraint('seconds_duration >= 0 AND seconds_duration <= 60'))
    release_date = db.Column(db.Date())
    maturity_rating = db.Column(db.Enum(MaturityRating), server_default='NR')
    genres = db.relationship('Genres', backref='movie', lazy=True)

    def __repr__(self):
        return 'Movie( \
                        movie_id={}, movie_name={}, synopsis={}, \
                        rating={}, minutes_duration={}, seconds_duration={}, \
                        release_date={}, maturity_rating={} \
                    )'.format(
                        self.movie_id, self.movie_name, self.synopsis, self.rating,
                        self.minutes_duration, self.minutes_duration, self.seconds_duration,
                        self.release_date, self.maturity_rating
                    )