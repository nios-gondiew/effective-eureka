from datetime import datetime
from app import db

class Blog(db.Model):
    """
    Blog model representing a blog post.
    """

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Blog {self.id} - {self.title}>'
