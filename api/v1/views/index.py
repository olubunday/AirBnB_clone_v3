#!/usr/bin/python3
"""
Contains the endpoint to retrieve the number of each object by type
"""

from flask import jsonify, Blueprint
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

stats = Blueprint('stats', __name__)

@stats.route('/api/v1/stats', methods=['GET'])
def get_stats():
    classes = {
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }
    stats_data = {}
    
    for class_name, class_obj in classes.items():
        count = storage.count(class_obj)
        stats_data[class_name] = count

    return jsonify(stats_data)

