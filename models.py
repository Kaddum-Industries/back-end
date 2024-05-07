from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this to a secure secret key
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Enum('Not-Started', 'In-progress', 'Completed'), default='Not-Started', nullable=False)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    pay_rate = db.Column(db.Float, nullable=False)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    preferred_contact = db.Column(db.String(100), nullable=False)
    background = db.Column(db.Enum('Not local', 'Local', 'Local Indigenous', 'Not local Indigenous'), nullable=False)
    status = db.Column(db.Enum('Active', 'Deactive'), nullable=False)


class DailyTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)


class DailyDairy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(100), nullable=False)
    client = db.Column(db.String(100), nullable=False)
    day = db.Column(db.Date, nullable=False)
    supervisor = db.Column(db.String(50), nullable=False)  # Assuming supervisor is a username
    activities_discussed = db.Column(db.Text)
    safety_issues_discussed = db.Column(db.Text)
    delays_occurred = db.Column(db.Enum('Access', 'Awaiting Instructions', 'Lack of Drawings', 'Subcontractors',
                                         'Awaiting Decision', 'Awaiting Materials', 'Poor Weather', 'Rework',
                                         'Industrial Matters', 'Other'))
    details_of_delay = db.Column(db.Text)
    jha = db.Column(db.Integer)
    ccc = db.Column(db.Integer)
    take_5 = db.Column(db.Integer)
    stop_seek = db.Column(db.Integer)
    instructions_received = db.Column(db.Text)
    visitors_on_site = db.Column(db.Text)
    daily_progress_description = db.Column(db.Text)
    handover_notes = db.Column(db.Text)
