from project import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    default_url = db.Column(db.Text, unique=True, nullable=False)
    short_url = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"Url ('{self.default_url}', '{self.shortener_url}')"
