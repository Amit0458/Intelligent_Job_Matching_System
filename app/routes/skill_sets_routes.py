from flask import Blueprint, jsonify, request
from app.models import db, SkillSet, JobPosting

skill_sets_bp = Blueprint('skill_sets', __name__, url_prefix='/skill_sets')

# Create a new skill set linked to a specific job posting
@skill_sets_bp.route('/<int:job_posting_id>', methods=['POST'])
def create_skill_set(job_posting_id):
    try:
        job_posting = JobPosting.query.get_or_404(job_posting_id)

        data = request.json
        if not data:
            return jsonify({'error': 'Empty request data'}), 400

        new_skill_set = SkillSet(**data)
        new_skill_set.job_postings.append(job_posting)  # Link the skill set to the job posting
        db.session.add(new_skill_set)
        db.session.commit()
        return jsonify(new_skill_set.serialize()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get all skill sets associated with a specific job posting
@skill_sets_bp.route('/<int:job_posting_id>', methods=['GET'])
def get_skill_sets_for_job_posting(job_posting_id):
    try:
        job_posting = JobPosting.query.get_or_404(job_posting_id)
        skill_sets = SkillSet.query.filter(SkillSet.job_postings.any(id=job_posting_id)).all()
        return jsonify([skill_set.serialize() for skill_set in skill_sets]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get details of a specific skill set by ID
@skill_sets_bp.route('/details/<int:skill_set_id>', methods=['GET'])
def get_skill_set_details(skill_set_id):
    try:
        skill_set = SkillSet.query.get_or_404(skill_set_id)
        return jsonify(skill_set.serialize()), 200
    except Exception as e:
        return jsonify({'error': 'Skill set not found'}), 404

# Update details of a specific skill set by ID
@skill_sets_bp.route('/<int:skill_set_id>', methods=['PUT'])
def update_skill_set(skill_set_id):
    try:
        skill_set = SkillSet.query.get_or_404(skill_set_id)
        data = request.json
        for key, value in data.items():
            setattr(skill_set, key, value)
        db.session.commit()
        return jsonify(skill_set.serialize()), 200
    except KeyError as e:
        return jsonify({'error': 'Missing key in JSON data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a specific skill set by ID
@skill_sets_bp.route('/<int:skill_set_id>', methods=['DELETE'])
def delete_skill_set(skill_set_id):
    try:
        skill_set = SkillSet.query.get_or_404(skill_set_id)
        db.session.delete(skill_set)
        db.session.commit()
        return jsonify({'message': 'Skill set deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
