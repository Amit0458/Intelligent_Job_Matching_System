from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS
from app.routes.hiring_manager_routes import hiring_managers_bp
from app.routes.job_seeker_routes import job_seekers_bp
from app.routes.job_posting_routes import job_postings_bp
from app.routes.job_applications_routes import job_applications_bp
from app.routes.skill_sets_routes import skill_sets_bp
from app.models import db


def create_app():

    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@localhost/{os.getenv('DB_DATABASENAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Enableed CORS for all routes
    CORS(app)

    with app.app_context():
        db.create_all()

    # Registered blueprints
    app.register_blueprint(hiring_managers_bp)
    app.register_blueprint(job_seekers_bp)
    app.register_blueprint(job_postings_bp)
    app.register_blueprint(job_applications_bp)
    app.register_blueprint(skill_sets_bp)

    return app
