# SLMS - Staff Leave Management System

A complete Staff Leave Management System built with Django.

## Features

- 🔐 **User Authentication** - Login/Register system with role-based access
- 👑 **Admin Dashboard** - Real-time analytics and insights
- 👥 **Staff Management** - Add, edit, and delete staff members
- 📋 **Leave Management** - Apply, approve, and reject leave requests
- 📊 **Live Statistics** - Total leaves, pending, approved, rejected, and total staff
- 🎨 **Modern UI** - Beautiful glass-morphism design
- 📱 **Fully Responsive** - Works on all devices

## Tech Stack

- **Django** - Python Web Framework
- **Python** - Backend Logic
- **SQLite** - Database
- **HTML5** - Structure
- **CSS3** - Styling with Glass-morphism
- **Django Template Language (DTL)** - Templating

## Installation

1. Clone the repository
```bash
git clone https://github.com/Inchara-08/SLMS-Staff-Leave-Management-System.git

2. Create a virtual environment
python -m venv test

3. Create a virtual environment
.\test\Scripts\activate

4. Install dependencies
pip install django

5. Run migrations
py manage.py makemigrations
py manage.py migrate

6. Create superuser (Admin)
py manage.py createsuperuser

7. Run the server
py manage.py runserver

8. Access the application at: http://127.0.0.1:8000

User Roles
Role	               Access
Admin	Full access -  Manage staff, approve/reject leaves, view analytics
Staff	            -  Apply for leaves, view leave status

Author
Inchara
GitHub: @Inchara-08

