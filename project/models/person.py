from ..extensions import db

class Person(db.Model):
    person_id = db.Column(db.Integer(), primary_key=True, nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return 'Person(person_id={}, first_name={}, last_name={})' \
            .format(self.person_id, self.first_name, self.last_name)
