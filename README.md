# Django REST Framework JWT Task Management System

This project is a secure RESTful API system built with Django REST Framework (DRF) and JWT authentication. It includes role-based access control for Admins, Managers, and Users.

# Project Setup

# 1. Clone the repository

git clone <your_github_repo_url>
cd cistask

# 2. Create virtual environment

python -m venv venv
venv\Scripts\activate # Windows

# 3. Install dependencies

pip install -r requirements.txt

# 4. Run migrations

python manage.py makemigrations
python manage.py migrate

# 5. Create superuser

python manage.py createsuperuser

# 6. Run server

python manage.py runserver

# Implemented Features

# Authentication

- JWT login via `/token/`
- JWT refresh via `/token/refresh/`

# Role-based Access

- Roles: Admin, Manager, User
- Admin: Full access to all APIs
- Manager: Can create tasks, assign, monitor, and reactivate users
- User: Can view assigned tasks, update task status

# Task Management

- CRUD for tasks (admin/manager)
- Users can only see/update their assigned tasks
- Deadline tracking

# Auto-deactivation

- A cron job or Celery task checks for 5 missed/unattended tasks in a week
- Automatically deactivates user

# Reactivation

- Only Admin or Manager can reactivate deactivated users

# API Testing

A Postman collection `drf_jwt_taskmanager_postman_collection.json` is included that covers:

- Registration
- Login (JWT)
- Task create/list/update
- User list/reactivation

Import it into Postman and set environment variables:

- `base_url`: `http://127.0.0.1:8000`
- `jwt_token`: JWT access token after login

# File Structure

- `core/` — app with models, views, permissions, tasks
- `project/` — Django project settings
- `requirements.txt` — dependencies
- `readme.txt` — this file

# Endpoints (Summary)

- `/api/register/` - Register new user
- `/api/token/` - Get JWT token
- `/api/users/` - Admin only
- `/api/tasks/` - Create/view/update tasks
