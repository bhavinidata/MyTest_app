from .app import db

class My_data(db.Model):
    __tablename__ = 'my_test_table'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))

    def __repr__(self):
        return '<My_data %r>' % (self.name)
