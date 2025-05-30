
# Student Management System (STDMS) 🏫

This is a Django-based web application designed to manage student records, attendance, marks, assignments, and announcements in an educational institution.

---

## 🔧 Features

- **Student Login** – View subjects, marks, announcements, attendance  
- **Teacher Login** – Generate QR for attendance, manage marks, assignments, announcements  
- **Admin Panel** – Manage students/teachers, upload CSV, edit/delete records  
- **QR-based Attendance System** with geolocation validation  
- **Celery + Redis** integration to automatically mark absent students  
- **CSV Upload** for bulk student, teacher, and marks management  
- **Role-based Authentication** for Admin, Teacher, and Student  

---

## 🛠️ Tech Stack

- **Backend:** Django 5.1.6, Celery  
- **Database:** MySQL  
- **Frontend:** HTML, CSS (via Django templates)  
- **Queue:** Redis  
- **Other:** SSL support for local testing, logging, environment separation  

---

## 🚀 How to Run Locally

1. Clone the repo:
    ```bash
    git clone https://github.com/your-username/student-management-system.git
    cd student-management-system
    ```

2. Create virtual environment & install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Set up MySQL database:
    - Create a DB named `student_management_system`
    - Update DB credentials in `settings.py`

4. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Start Redis:
    ```bash
    sudo service redis-server start
    ```

7. Start Django app & Celery:
    ```bash
    python manage.py runserver
    celery -A stdms worker --loglevel=info
    ```

8. (Optional) Run with SSL:
    ```bash
    python manage.py runsslserver --certificate certs/cert.pem --key certs/key.pem 127.0.0.1:8000
    ```
Screenshots shows the description about Login Page , Dashboard  and functionality of Admin , Student and Teacher! 
& visual Representation of Attendance in Student Dashboard
=
---
![Screenshot 2025-05-05 151717](https://github.com/user-attachments/assets/929af885-cca5-471a-abef-560c5a76887d)
![Screenshot 2025-05-05 151702](https://github.com/user-attachments/assets/fda58c52-e031-4e7b-aff5-31d10bc4c6af)
![Screenshot 2025-05-05 151643](https://github.com/user-attachments/assets/d1245aa6-f381-47b6-8134-f037ee86ce13)
![Screenshot 2025-05-05 160030](https://github.com/user-attachments/assets/b763480b-c5a5-4204-8dc8-5133560bc99c)
![Screenshot 2025-05-05 151521](https://github.com/user-attachments/assets/f3cb7f5d-b6f3-4a02-938f-7cb53d84cef3)
![Screenshot 2025-05-05 150704](https://github.com/user-attachments/assets/829c1634-fa6c-4bfa-a5de-f2c428865460)
![Screenshot 2025-05-05 150238](https://github.com/user-attachments/assets/c29d0542-1fde-4f45-963c-f33a01d5f43c)

