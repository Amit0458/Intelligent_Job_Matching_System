from flask import Blueprint, jsonify, request
from app.models import db, HiringManager

hiring_managers_bp = Blueprint('hiring_managers', __name__, url_prefix='/hiring_managers')

# Get all hiring managers
@hiring_managers_bp.route('/', methods=['GET'])
def get_all_hiring_managers():
    try:
        hiring_managers = HiringManager.query.all()
        return jsonify([hiring_manager.serialize() for hiring_manager in hiring_managers]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific hiring manager by ID
@hiring_managers_bp.route('/<int:id>', methods=['GET'])
def get_hiring_manager(id):
    try:
        hiring_manager = HiringManager.query.get_or_404(id)
        return jsonify(hiring_manager.serialize()), 200
    except Exception as e:
        return jsonify({'error': 'Hiring manager not found'}), 404

# Create new hiring manager or managers
@hiring_managers_bp.route('/', methods=['POST'])
def create_hiring_managers():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Empty request data'}), 400

        new_hiring_managers = []
        for hiring_manager_data in data:
            new_hiring_manager = HiringManager(**hiring_manager_data)
            new_hiring_managers.append(new_hiring_manager)

        db.session.add_all(new_hiring_managers)
        db.session.commit()
        return jsonify([hiring_manager.serialize() for hiring_manager in new_hiring_managers]), 201
    except KeyError as e:
        return jsonify({'error': 'Missing key in JSON data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing hiring manager
@hiring_managers_bp.route('/<int:id>', methods=['PATCH'])
def update_hiring_manager(id):
    try:
        hiring_manager = HiringManager.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(hiring_manager, key, value)
        db.session.commit()
        return jsonify(hiring_manager.serialize()), 200
    except KeyError as e:
        return jsonify({'error': 'Missing key in JSON data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a hiring manager
@hiring_managers_bp.route('/<int:id>', methods=['DELETE'])
def delete_hiring_manager(id):
    try:
        hiring_manager = HiringManager.query.get_or_404(id)
        db.session.delete(hiring_manager)
        db.session.commit()
        return jsonify({'message': 'Hiring Manager deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
