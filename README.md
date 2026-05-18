# Healthcare API

A full-stack Healthcare API built with **Python**, **Django**, and **Django REST Framework (DRF)** to manage patient and doctor information. Supports full CRUD operations, session-based authentication, permissions, and displays data via Django frontend templates.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Frontend](#frontend)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Healthcare API provides a robust backend system to manage healthcare data including patients and doctors. It exposes RESTful endpoints using DRF Routers and renders the API data on a frontend using Django Templates (HTML & CSS).

---

## Features

- Full **CRUD** operations for Patients and Doctors
- **Session-based Authentication** for secure access
- **Permissions** — only authenticated users can access protected routes
- **DRF Routers** for clean, automatic URL routing
- **Frontend Templates** to display API data in the browser
- Lightweight **SQLite3** database — zero configuration needed
- Django Admin panel for easy data management

---

## Tech Stack

| Layer           | Technology                        |
|-----------------|-----------------------------------|
| Backend         | Python 3.x, Django                |
| API Framework   | Django REST Framework (DRF)       |
| Database        | SQLite3                           |
| Authentication  | Session Authentication            |
| Frontend        | Django Templates (HTML5, CSS3)    |
| Routing         | Django REST Framework Routers     |

---

## Project Structure

```
healthcare-api/
├── healthcare_api/             # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── patients/                   # Patients app
│   ├── migrations/
│   ├── templates/
│   │   └── patients/
│   │       ├── patient_list.html
│   │       └── patient_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── permissions.py
├── doctors/                    # Doctors app
│   ├── migrations/
│   ├── templates/
│   │   └── doctors/
│   │       ├── doctor_list.html
│   │       └── doctor_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── static/
│   └── css/
│       └── style.css
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/healthcare-api.git
   cd healthcare-api
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Visit: `http://127.0.0.1:8000`

---

## API Endpoints

### Patients

| Method | Endpoint              | Description          | Auth Required |
|--------|-----------------------|----------------------|---------------|
| GET    | `/api/patients/`      | List all patients    |    Yes        |
| POST   | `/api/patients/`      | Create a patient     |    Yes        |
| GET    | `/api/patients/<id>/` | Retrieve a patient   |    Yes        |
| PUT    | `/api/patients/<id>/` | Update a patient     |    Yes        |
| DELETE | `/api/patients/<id>/` | Delete a patient     |    Yes        |

### Doctors

| Method | Endpoint             | Description         | Auth Required |
|--------|----------------------|---------------------|---------------|
| GET    | `/api/doctors/`      | List all doctors    |    Yes        |
| POST   | `/api/doctors/`      | Create a doctor     |    Yes        |
| GET    | `/api/doctors/<id>/` | Retrieve a doctor   |    Yes        |
| PUT    | `/api/doctors/<id>/` | Update a doctor     |    Yes        |
| DELETE | `/api/doctors/<id>/` | Delete a doctor     |    Yes        |

### Auth

| Method | Endpoint              | Description |
|--------|-----------------------|-------------|
| POST   | `/api/auth/login/`    | Login       |
| POST   | `/api/auth/logout/`   | Logout      |

> All routes are auto-generated using **DRF Routers**.

---

## Authentication

This project uses **Django Session Authentication**.

- Login via `/api/auth/login/` or the Django Admin panel
- Once logged in, the session cookie authenticates subsequent requests
- Unauthenticated requests to protected endpoints return `403 Forbidden`

To test with the DRF browsable API:
1. Go to `http://127.0.0.1:8000/api/`
2. Click **"Log in"** in the top right
3. Enter your superuser credentials

---

## Frontend

API data is rendered using **Django Templates** with HTML and CSS.

| URL                 | Description         |
|---------------------|---------------------|
| `/`                 | Home / Dashboard    |
| `/patients/`        | Patient list view   |
| `/patients/<id>/`   | Patient detail view |
| `/doctors/`         | Doctor list view    |
| `/doctors/<id>/`    | Doctor detail view  |
| `/admin/`           | Django admin panel  |

---

## Screenshots

<img width="932" height="440" alt="image" src="https://github.com/user-attachments/assets/79f1555a-3807-43bb-a5c4-2c23d6a5b148" />
<img width="380" height="294" alt="image" src="https://github.com/user-attachments/assets/88078cba-8a46-49ab-b5da-9f553f095e05" />

<img width="935" height="435" alt="image" src="https://github.com/user-attachments/assets/dc2f41a2-520e-4823-8d1e-b3d096469545" />
<img width="929" height="415" alt="image" src="https://github.com/user-attachments/assets/23e14b9b-4ec9-4970-983a-3893a71057b4" />
<img width="590" height="287" alt="image" src="https://github.com/user-attachments/assets/461731ad-e1ae-4fee-a7b3-e8d7c7b93c78" />

<img width="945" height="426" alt="image" src="https://github.com/user-attachments/assets/4b813c6d-ba81-4c30-b75c-08f8529fcd5b" />
<img width="918" height="433" alt="image" src="https://github.com/user-attachments/assets/f88ff49d-c5ec-4397-b371-88c10fde1a8b" />

---


## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Your Name**
- GitHub: [urk19cs1207i](https://github.com/urk19cs1207i)
- LinkedIn: "linkedin.com/in/jonnalagadda-akshaya"


