# Staff Leave Management System (SLMS)

A web-based Staff Leave Management System developed using Django. This application allows staff members to apply for leave and track leave requests, while administrators can manage staff accounts and approve or reject leave applications.

## Features

### Authentication

* User Registration
* User Login
* User Logout
* Role-based Access (Admin and Staff)

### Staff Module

* Apply for Leave
* View Leave Status
* Track Approved, Rejected, and Pending Requests

### Admin Module

* Dashboard Overview
* Manage Staff Accounts
* Add Staff
* Edit Staff Details
* Delete Staff Accounts
* View Leave Requests
* Approve Leave Requests
* Reject Leave Requests

## Technologies Used

* Python
* Django
* HTML5
* CSS3
* SQLite3

## Project Structure

```text
SLMS/
│
├── leave_app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   └── image/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/staff-leave-management-system.git
```

### Navigate to the Project Directory

```bash
cd staff-leave-management-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install django
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Open the browser and visit:

```text
http://127.0.0.1:8000/
```

## Future Enhancements

* Email Notifications
* Leave Balance Management
* Department Management
* Reporting and Analytics
* Export Leave Reports to PDF/Excel
* Profile Management

## Author
 Sravya E

## License

This project is created for educational and learning purposes.
