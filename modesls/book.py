


from db import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Book(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = db.Column(UUID(as_uuid=True), db.ForeignKey('schools.school_id'))
    title = db.Column(db.String, nullable=False, unique=True)
    author = db.Column(db.String)
    subject = db.Column(db.String)
    rarity_level = db.Column(db.Integer)
    magical_properties = db.Column(db.String)
    available = db.Column(db.Boolean, default=True)

    school = db.relationship('School', back_populates='books')
