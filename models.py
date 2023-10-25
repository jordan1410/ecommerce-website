from app.extensions import db
from flask_login import UserMixin

# Removed database structure

class Logins(db.Model, UserMixin):
    pass


class Pending(db.Model):
    pass


class Confirmed(db.Model):
    pass


class Completed(db.Model):
    pass
