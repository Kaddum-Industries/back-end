# Project Name

Brief description or tagline summarizing the project.

## Table of Contents

- [User Authentication](#user-authentication)
- [Projects](#projects)
- [Employees](#employees)
- [Roles](#roles)
- [Daily Activities](#daily-activities)
- [Live Deployment](#live-deployment)

## User Authentication

- **Register User:** `POST /register`
  Register a new user with a username, password, and role.
  
- **Login User:** `POST /login`
  Log in an existing user with a username and password.
  
- **Logout User:** `GET /logout`
  Log out the currently logged-in user.
  
- **Get User Profile:** `GET /profile`
  Retrieve the profile information of the currently logged-in user.

## Projects

- **Add Project:** `POST /projects`
  Add a new project with a name, start date, location, and status.
  
- **Update Project:** `PUT /projects/<project_id>`
  Update an existing project identified by project_id.
  
- **Delete Project:** `DELETE /projects/<project_id>`
  Delete an existing project identified by project_id.

## Employees

- **Add Employee:** `POST /employees`
  Add a new employee with a name, preferred contact, background, and status.
  
- **Update Employee:** `PUT /employees/<employee_id>`
  Update an existing employee identified by employee_id.

## Roles

- **Add Role:** `POST /roles`
  Add a new role with a name, description, and pay rate.

## Daily Activities

- **Add Daily Dairy:** `POST /daily_dairy`
  Add a new daily dairy entry with various fields describing daily activities on a job site.
  
- **Add Daily Tracking:** `POST /tracking`
  Add tracking information for daily activities on a project, including project ID, employee ID, role ID, start time, and end time.

## Live Deployment

The backend server is deployed and accessible at [Kaddum Industries Backend](https://kaddum-adbf0051a9ce.herokuapp.com/).
