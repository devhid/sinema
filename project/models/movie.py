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

class Movie(db.Model):
    movie_id = db.Column(db.Integer(), primary_key=True, nullable=False)
    movie_name = db.Column(db.String(255), unique=True, nullable=False)
    synopsis = db.Column(db.String(255))
    rating = db.Column(db.Float(2,1), db.CheckConstraint('rating=0.0 OR (rating >= 1.0 AND rating <= 5.0)'), default=0.0)
    minutes_duration = db.Column(db.Integer, db.CheckConstraint('minutes_duration >= 0'))
    seconds_duration = db.Column(db.Integer, db.CheckConstraint('seconds_duration >= 0'))
    release_date = db.Column(db.Date())
    maturity_rating = db.Column(db.Enum(MaturityRating), default='NR')

    def __repr__(self):
        return 'Movie( \
                        movie_id={}, movie_name={}, synopsis={}, \
                        rating={}, minutes_duration={}, seconds_duration={}, \
                        release_date={}, maturity_rating={} \
                    )'.format(self.movie_id, self.movie_name, self.synopsis, self.rating,
                            self.minutes_duration, self.minutes_duration, self.seconds_duration,
                            self.release_date, self.maturity_rating)