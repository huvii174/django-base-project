**Django User Management System**

This project is a Django-based User Management System that supports three roles:

* **Super Admin**: Can manage Admins and other Super Admins.

* **Admin**: Can manage Viewers.

* **Viewer**: Read-only access to the system.

The system includes functionality for role-based dashboards and user creation without redirection after the user is
added.

### **Features**

* Role-based authentication and authorization:

    * **Super Admin Dashboard**:

        * View all Admins and Super Admins.

        * Add Admins or Super Admins.

    * **Admin Dashboard**:

        * View all Viewers.

        * Add Viewers.

* Login system with redirect to the appropriate dashboard based on the user's role.

* Secure password hashing.

* Modular app structure for scalability.

### **Folder Structure**

```csharp
project_base/
├── app_base/                   # Main app with core functionality
│   ├── templates/              # HTML templates
│   │   └── app_base/
│   │       ├── login.html
│   │       ├── dashboard_admin.html
│   │       ├── dashboard_super_admin.html
│   │       ├── dashboard_viewer.html
│   ├── static/                 # Static files (CSS, JS, images)
│   ├── migrations/             # Database migrations
│   ├── admin.py                # Admin panel configurations
│   ├── apps.py                 # App configurations
│   ├── models.py               # Database models
│   ├── tests.py                # Unit tests
│   ├── urls.py                 # App-level URLs
│   ├── views.py                # App-level views
├── project_base/               # Project-level configurations
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Project-level URLs
│   ├── wsgi.py                 # WSGI entry point
│   ├── asgi.py                 # ASGI entry point
├── manage.py                   # Django command-line utility

```

### **Getting Started**

#### **Requirements**

* Python 3.9+

* PostgreSQL

* Virtual environment (recommended)

#### **Setup Instructions**

1.
 ```python
 pip install -r requirements.txt
 ```

2.
 ```bash
 SECRET_KEY=your-secret-key
 DEBUG=True
 DB_NAME=your_database_name
 DB_USER=your_database_user
 DB_PASSWORD=your_database_password
 DB_HOST=localhost
 DB_PORT=5432
 ```

3.
 ```python
 python manage.py makemigrations
 python manage.py migrate
 ```

4.
 ```python
 python manage.py createsuperuser
 ```

5.
 ```python
 python manage.py runserver
 ```

6. **Access the Application**

    * **Login Page**: http://127.0.0.1:8000/login/

    * **Admin Dashboard** (for Admins): http://127.0.0.1:8000/admin-dashboard/

    * **Super Admin Dashboard** (for Super Admins): http://127.0.0.1:8000/super-admin-dashboard/