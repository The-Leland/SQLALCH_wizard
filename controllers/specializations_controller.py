


from flask import jsonify
from models.specialization import WizardSpecialization
from db import db
from datetime import datetime

def create_specialization_entry(data):
    try:
        specialization = WizardSpecialization(
            wizard_id=data['wizard_id'],
            spell_id=data['spell_id'],
            proficiency_level=data.get('proficiency_level'),
            date_learned=datetime.strptime(data['date_learned'], "%Y-%m-%d")
        )
        db.session.add(specialization)
        db.session.commit()
        return jsonify(message="Specialization created successfully"), 201
    except Exception as e:
        return jsonify(error=str(e)), 400
