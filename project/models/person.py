from ..extensions import db

"""
CREATE TABLE Person(
    Id INTEGER,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    PRIMARY KEY(Id)
);
"""

class Person(db.Model):
    person_id = db.Column(db.Integer(), primary_key=True, nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    is_actor = db.Column(db.Boolean(), default=False)
    is_director = db.Column(db.Boolean(), default=False)
    is_writer = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return 'Person(person_id={}, first_name={}, last_name={})' \
            .format(self.person_id, self.first_name, self.last_name)
