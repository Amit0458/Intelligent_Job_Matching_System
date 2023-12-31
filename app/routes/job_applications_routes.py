from flask import Blueprint, jsonify, request
from app.models import db, Application, JobPosting, JobSeeker

job_applications_bp = Blueprint('applications', __name__, url_prefix='/applications')

# Create a new application for a job posting
@job_applications_bp.route('/<int:job_posting_id>', methods=['POST'])
def create_application(job_posting_id):
    try:
        job_posting = JobPosting.query.get_or_404(job_posting_id)

        data = request.json
        if not data:
            return jsonify({'error': 'Empty request data'}), 400

        new_application = Application(**data)
        new_application.job_posting = job_posting
        db.session.add(new_application)
        db.session.commit()
        return jsonify(new_application.serialize()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get all applications for a specific job posting
@job_applications_bp.route('/<int:job_posting_id>', methods=['GET'])
def get_applications_for_job_posting(job_posting_id):
    try:
        job_posting = JobPosting.query.get_or_404(job_posting_id)
        applications = Application.query.filter_by(job_posting_id=job_posting_id).all()
        return jsonify([application.serialize() for application in applications]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@job_applications_bp.route('/details/<int:application_id>', methods=['GET'])
def get_application_details(application_id):
    try:
        application = Application.query.get_or_404(application_id)
        
        # Retrieve job posting details
        # job_posting = JobPosting.query.get(application.job_posting_id)
        
        # Retrieve job seeker details
        job_seeker = JobSeeker.query.get(application.job_seeker_id)
        
        if job_seeker:
            # Return application, job posting, and job seeker details
            return jsonify({
                'application_details': application.serialize(),
                # 'job_posting_details': job_posting.serialize(),
                'job_seeker_details': job_seeker.serialize()
            }), 200
        else:
            return jsonify({'error': 'Job seeker or job posting details not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Application not found'}), 404

# Update details of a specific application by ID
@job_applications_bp.route('/<int:application_id>', methods=['PATCH'])
def update_application(application_id):
    try:
        application = Application.query.get_or_404(application_id)
        data = request.json
        for key, value in data.items():
            setattr(application, key, value)
        db.session.commit()
        return jsonify(application.serialize()), 200
    except KeyError as e:
        return jsonify({'error': 'Missing key in JSON data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a specific application by ID
@job_applications_bp.route('/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    try:
        application = Application.query.get_or_404(application_id)
        db.session.delete(application)
        db.session.commit()
        return jsonify({'message': 'Application deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
