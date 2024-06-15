# Supermarket-Software - AKROFT TECH 🇰🇪
Akrofttechnologies supermarket software task repository

The Project Structure
```
supermarket-Software/
├── backend/
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── supermarket/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── inventory/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── sales/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── customers/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── employees/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── app.js
│   ├── clerk.js
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── inventory.html
│   ├── pos.html
│   ├── customers.html
│   ├── employees.html
│   ├── reports.html
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

### 1. Requirements Analysis
Functional Requirements:
Supermarket Registration: Admin can register their supermarket.
Login and Authorization: Used Clerk for authentication and authorization.
Inventory Management: Add, update, delete, and view products.
Point of Sale (POS) System: Process sales, generate receipts.
Customer Management: Manage customer information.
Employee Management: Manage employee details.
Reporting and Analytics: Generate sales and inventory reports.
Online Order Processing: Manage online orders (if applicable).<br>

Non-Functional Requirements:
Scalability
Security
Reliability
Maintainability
Performance
### 2. System Architecture
Frontend:
Languages: HTML, CSS, JavaScript <br>
Backend:
Framework: Django
Database: MongoDB (Use pymongo for integration)<br>
Authentication:
Service: Clerk
DevOps:
Containerization: Docker
CI/CD: GitHub Actions
Code Quality: SonarQube <br><br>
### 3. Detailed Development Plan
Frontend Development
Setup Project Structure:

Create project folders and files for HTML, CSS, and JavaScript.
Build Pages:

Home Page: Overview of supermarket features.
Login/Register Page: Integrate Clerk for authentication.
Dashboard: Admin panel for managing all functionalities.
Inventory Management:
Add/Edit/Delete Products Page
View Products Page

POS System:
Sales Processing Page
Receipt Generation Page
Customer Management:
Add/Edit/Delete Customers Page
View Customers Page
Employee Management:
Add/Edit/Delete Employees Page
View Employees Page

Reports:
Sales Reports Page
Inventory Reports Page
Design Considerations:

Tailwind CSS for responsive design.
Clean and intuitive user interface.
Modal dialogs for add/edit operations.
Display data in tables with sorting and searching functionality.
Backend Development