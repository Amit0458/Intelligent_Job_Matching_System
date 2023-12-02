from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HiringManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(15))
    department = db.Column(db.String(100))

    def __repr__(self):
        return f'<HiringManager {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'department': self.department
        }

class JobSeeker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(15))
    status = db.Column(db.Boolean)
    skills = db.Column(db.String(255))
    experience = db.Column(db.String(50))
    bio = db.Column(db.Text)
    availability = db.Column(db.Date)

    def __repr__(self):
        return f'<JobSeeker {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'status': self.status,
            'skills': self.skills,
            'experience': self.experience,
            'bio': self.bio,
            'availability': str(self.availability) if self.availability else None
        }
    
# Many-to-Many Relationship Association Table for SkillSet and JobPosting
class SkillSetJobPosting(db.Model):
    __tablename__ = 'skillset_jobposting'
    skillset_id = db.Column(db.Integer, db.ForeignKey('skillset.id'), primary_key=True)
    jobposting_id = db.Column(db.Integer, db.ForeignKey('jobposting.id'), primary_key=True)


class JobPosting(db.Model):
    __tablename__ = 'jobposting'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100))
    status = db.Column(db.String(50))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    
    # relationship with Hiring Manager
    hiring_manager_id = db.Column(db.Integer, db.ForeignKey('hiring_manager.id'))
    hiring_manager = db.relationship('HiringManager', backref=db.backref('job_postings', lazy=True))
    
    # many-to-many relationship with SkillSet
    skillsets = db.relationship('SkillSet', secondary='skillset_jobposting', backref='job_postings')
    
    # one-to-many relationship with Application
    applications = db.relationship('Application', backref='job_posting', lazy=True)

    def __repr__(self):
        return f'<JobPosting {self.job_title}>'

    def serialize(self):
        return {
            'id': self.id,
            'job_title': self.job_title,
            'status' : self.status,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'hiring_manager': self.hiring_manager.serialize() if self.hiring_manager else None,
            'skillsets': [skillset.serialize() for skillset in self.skillsets],
            'applications': [application.serialize() for application in self.applications]
        }    

class SkillSet(db.Model):
    __tablename__ = 'skillset'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
    jobpostings = db.relationship('JobPosting', secondary='skillset_jobposting', backref='associated_skillsets')

    def __repr__(self):
        return f'<SkillSet {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    


class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    job_posting_id = db.Column(db.Integer, db.ForeignKey('jobposting.id'))
    status = db.Column(db.String(50))
    
    # applicant details from JobSeeker
    job_seeker_id = db.Column(db.Integer, db.ForeignKey('job_seeker.id'))
    job_seeker = db.relationship('JobSeeker', backref=db.backref('applications', lazy=True))

    def __repr__(self):
        return f'<Application {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'job_posting_id': self.job_posting_id,
            'status': self.status,
            'job_seeker_id': self.job_seeker_id
        }


    

