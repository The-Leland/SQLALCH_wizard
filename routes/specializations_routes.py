

from flask import Blueprint, request
from controllers.specializations_controller import *

specializations_routes = Blueprint('specializations_routes', __name__)

@specializations_routes.route('/wizard/specialize', methods=['POST'])
def create_specialization():
    return create_specialization_entry(request.json)
