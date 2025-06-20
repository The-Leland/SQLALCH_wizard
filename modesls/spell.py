


from db import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Spell(db.Model):
    __tablename__ = 'spells'

    spell_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    spell_name = db.Column(db.String, nullable=False, unique=True)
    incantation = db.Column(db.String)
    difficulty_level = db.Column(db.Float)
    spell_type = db.Column(db.String)
    description = db.Column(db.String)

    specializations = db.relationship('WizardSpecialization', back_populates='spell', cascade='all, delete')
