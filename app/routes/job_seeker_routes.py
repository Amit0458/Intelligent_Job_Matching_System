from flask import Blueprint, jsonify, request
from app.models import db, JobSeeker

job_seekers_bp = Blueprint('job_seekers', __name__, url_prefix='/job_seekers')

# Get all job seekers
@job_seekers_bp.route('/', methods=['GET'])
def get_all_job_seekers():
    try:
        job_seekers = JobSeeker.query.all()
        return jsonify([job_seeker.serialize() for job_seeker in job_seekers]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific job seeker by ID
@job_seekers_bp.route('/<int:id>', methods=['GET'])
def get_job_seeker(id):
    try:
        job_seeker = JobSeeker.query.get_or_404(id)
        return jsonify(job_seeker.serialize()), 200
    except Exception as e:
        return jsonify({'error': 'Job seeker not found'}), 404

# Create a new job seeker profile
@job_seekers_bp.route('/', methods=['POST'])
def create_job_seeker():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Empty request data'}), 400

        new_job_seeker = JobSeeker(**data)
        db.session.add(new_job_seeker)
        db.session.commit()
        return jsonify(new_job_seeker.serialize()), 201
    except KeyError as e:
        return jsonify({'error': 'Missing key in JSON data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing job seeker profile
@job_seekers_bp.route('/<int:id>', methods=['PUT'])
def update_job_seeker(id):
    try:
        job_seeker = JobSeeker.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(job_seeker, key, value)
        db.session.commit()
        return jsonify(job_seeker.serialize()), 200
    except KeyError as e:
        return jsonify({'error': 'Missing key in JSON data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a job seeker profile
@job_seekers_bp.route('/<int:id>', methods=['DELETE'])
def delete_job_seeker(id):
    try:
        job_seeker = JobSeeker.query.get_or_404(id)
        db.session.delete(job_seeker)
        db.session.commit()
        return jsonify({'message': 'Job Seeker deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
