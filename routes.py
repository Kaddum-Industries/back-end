from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from models import app, db, User, Project, Role, Employee, DailyTracking, DailyDairy

# Existing route to add daily dairy
@app.route('/daily_dairy', methods=['POST'])
def add_daily_dairy():
    data = request.get_json()
    job_name = data.get('job_name')
    client = data.get('client')
    day = data.get('day')
    supervisor = data.get('supervisor')
    activities_discussed = data.get('activities_discussed')
    safety_issues_discussed = data.get('safety_issues_discussed')
    delays_occurred = data.get('delays_occurred')
    details_of_delay = data.get('details_of_delay')
    jha = data.get('jha')
    ccc = data.get('ccc')
    take_5 = data.get('take_5')
    stop_seek = data.get('stop_seek')
    instructions_received = data.get('instructions_received')
    visitors_on_site = data.get('visitors_on_site')
    daily_progress_description = data.get('daily_progress_description')
    handover_notes = data.get('handover_notes')

    new_daily_dairy = DailyDairy(
        job_name=job_name,
        client=client,
        day=datetime.strptime(day, '%Y-%m-%d').date(),
        supervisor=supervisor,
        activities_discussed=activities_discussed,
        safety_issues_discussed=safety_issues_discussed,
        delays_occurred=delays_occurred,
        details_of_delay=details_of_delay,
        jha=jha,
        ccc=ccc,
        take_5=take_5,
        stop_seek=stop_seek,
        instructions_received=instructions_received,
        visitors_on_site=visitors_on_site,
        daily_progress_description=daily_progress_description,
        handover_notes=handover_notes
    )
    db.session.add(new_daily_dairy)
    db.session.commit()

    return jsonify({'message': 'Daily dairy added successfully'}), 201

# Route to add daily tracking
@app.route('/tracking', methods=['POST'])
def add_tracking():
    data = request.get_json()
    project_id = data.get('project_id')
    employee_id = data.get('employee_id')
    role_id = data.get('role_id')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    if not all([project_id, employee_id, role_id, start_time, end_time]):
        return jsonify({'message': 'Missing required fields'}), 400

    new_tracking = DailyTracking(
        project_id=project_id,
        employee_id=employee_id,
        role_id=role_id,
        start_time=datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S'),
        end_time=datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    )
    db.session.add(new_tracking)
    db.session.commit()

    return jsonify({'message': 'Tracking information added successfully'}), 201

# Route to add employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    name = data.get('name')
    preferred_contact = data.get('preferred_contact')
    background = data.get('background')
    status = data.get('status')

    if not all([name, preferred_contact, background, status]):
        return jsonify({'message': 'Missing required fields'}), 400

    new_employee = Employee(name=name, preferred_contact=preferred_contact, background=background, status=status)
    db.session.add(new_employee)
    db.session.commit()

    return jsonify({'message': 'Employee added successfully'}), 201

# Route to update employee
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.get_json()
    employee = Employee.query.get(employee_id)

    if not employee:
        return jsonify({'message': 'Employee not found'}), 404

    employee.name = data.get('name', employee.name)
    employee.preferred_contact = data.get('preferred_contact', employee.preferred_contact)
    employee.background = data.get('background', employee.background)
    employee.status = data.get('status', employee.status)
    db.session.commit()

    return jsonify({'message': 'Employee updated successfully'}), 200

# Route to add role
@app.route('/roles', methods=['POST'])
def add_role():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    pay_rate = data.get('pay_rate')

    if not name or pay_rate is None:
        return jsonify({'message': 'Missing name or pay rate'}), 400

    new_role = Role(name=name, description=description, pay_rate=pay_rate)
    db.session.add(new_role)
    db.session.commit()

    return jsonify({'message': 'Role added successfully'}), 201

# Route to register user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password or not role:
        return jsonify({'message': 'Missing username, password, or role'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    # Special case for creating user "clinton@kaddum.com.au" with the given password
    if username == "clinton@kaddum.com.au":
        hashed_password = generate_password_hash("K@ddum@11")
        new_user = User(username=username, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

    # For other users, proceed with regular registration
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


# Route to login user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid username or password'}), 401

    session['user_id'] = user.id
    return jsonify({'message': 'Logged in successfully', 'role': user.role})

# Route to logout user
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'})

# Route to get user profile
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return jsonify({'message': 'You are not logged in'}), 401

    user_id = session['user_id']
    user = User.query.get(user_id)
    return jsonify({'username': user.username, 'role': user.role})

# Route to add project
@app.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    new_project = Project(
        name=data['name'],
        start_date=datetime.strptime(data['start_date'], '%Y-%m-%d').date(),
        location=data['location'],
        status=data['status']
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project added successfully'}), 201

# Route to update project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.get_json()
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'message': 'Project not found'}), 404
    project.name = data.get('name', project.name)
    project.start_date = datetime.strptime(data.get('start_date', project.start_date.strftime('%Y-%m-%d')), '%Y-%m-%d').date()
    project.location = data.get('location', project.location)
    project.status = data.get('status', project.status)
    db.session.commit()
    return jsonify({'message': 'Project updated successfully'}), 200

# Route to delete project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'message': 'Project not found'}), 404
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
