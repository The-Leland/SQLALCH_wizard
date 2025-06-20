from db import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Wizard(db.Model):
    __tablename__ = 'wizards'

    wizard_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = db.Column(UUID(as_uuid=True), db.ForeignKey('schools.school_id'))
    wizard_name = db.Column(db.String, nullable=False, unique=True)
    house = db.Column(db.String)
    year_enrolled = db.Column(db.Integer)
    magical_power_level = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=True)

    school = db.relationship('School', back_populates='wizards')
    specializations = db.relationship('WizardSpecialization', back_populates='wizard', cascade='all, delete')
