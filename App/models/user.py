from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username =  db.Column(db.String(80),unique=True,nullable=False)
    password = db.Column(db.String(120), nullable=False)



    def __init__(self, username,email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password':self.password
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

