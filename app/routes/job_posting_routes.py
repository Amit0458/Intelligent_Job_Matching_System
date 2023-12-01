from flask import Blueprint, jsonify, request
from app.models import db, JobPosting

job_postings_bp = Blueprint('job_postings', __name__, url_prefix='/job_postings')

# Get all job postings
@job_postings_bp.route('/', methods=['GET'])
def get_all_job_postings():
    try:
        job_postings = JobPosting.query.all()
        return jsonify([job_posting.serialize() for job_posting in job_postings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a specific job posting by ID
@job_postings_bp.route('/<int:id>', methods=['GET'])
def get_job_posting(id):
    try:
        job_posting = JobPosting.query.get_or_404(id)
        return jsonify(job_posting.serialize()), 200
    except Exception as e:
        return jsonify({'error': 'Job posting not found'}), 404

# Create a new job posting
@job_postings_bp.route('/', methods=['POST'])
def create_job_posting():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Empty request data'}), 400

        new_job_posting = JobPosting(**data)
        db.session.add(new_job_posting)
        db.session.commit()
        return jsonify(new_job_posting.serialize()), 201
    except KeyError as e:
        return jsonify({'error': 'Missing key in JSON data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update an existing job posting
@job_postings_bp.route('/<int:id>', methods=['PATCH'])
def update_job_posting(id):
    try:
        job_posting = JobPosting.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(job_posting, key, value)
        db.session.commit()
        return jsonify(job_posting.serialize()), 200
    except KeyError as e:
        return jsonify({'error': 'Missing key in JSON data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a job posting
@job_postings_bp.route('/<int:id>', methods=['DELETE'])
def delete_job_posting(id):
    try:
        job_posting = JobPosting.query.get_or_404(id)
        db.session.delete(job_posting)
        db.session.commit()
        return jsonify({'message': 'Job Posting deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
