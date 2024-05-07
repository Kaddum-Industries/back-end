# back-end

#git clone git@github.com:Kaddum-Industries/back-end.git

# cd <directory name>

# pip install -r requirements.txt

# python app.py

Api on : https://kaddum-adbf0051a9ce.herokuapp.com/


User Authentication:
Register User: POST /register - Register a new user with username, password, and role.
Login User: POST /login - Log in an existing user with username and password.
Logout User: GET /logout - Log out the currently logged-in user.
Get User Profile: GET /profile - Retrieve the profile information of the currently logged-in user.
Projects:
Add Project: POST /projects - Add a new project with name, start date, location, and status.
Update Project: PUT /projects/<project_id> - Update an existing project identified by project_id.
Delete Project: DELETE /projects/<project_id> - Delete an existing project identified by project_id.
Employees:
Add Employee: POST /employees - Add a new employee with name, preferred contact, background, and status.
Update Employee: PUT /employees/<employee_id> - Update an existing employee identified by employee_id.
Roles:
Add Role: POST /roles - Add a new role with name, description, and pay rate.
Daily Dairy:
Add Daily Dairy: POST /daily_dairy - Add a new daily dairy entry with various fields describing daily activities on a job site.
Daily Tracking:
Add Daily Tracking: POST /tracking - Add tracking information for daily activities on a project, including project ID, employee ID, role ID, start time, and end time.
