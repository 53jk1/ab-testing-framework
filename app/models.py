from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variant = db.Column(db.String(1), nullable=False)
    conversion = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User id={self.id}, variant={self.variant}, conversion={self.conversion}>'
