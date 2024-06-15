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
Functional Requirements:<br>
Supermarket Registration: Admin can register their supermarket.<br>
Login and Authorization: Used Clerk for authentication and authorization.<br>
Inventory Management: Add, update, delete, and view products.<br>
Point of Sale (POS) System: Process sales, generate receipts.<br>
Customer Management: Manage customer information.<br>
Employee Management: Manage employee details.<br>
Reporting and Analytics: Generate sales and inventory reports.<br>
Online Order Processing: Manage online orders (if applicable).<br>

Non-Functional Requirements:<br>
Scalability<br>
Security<br>
Reliability<br>
Maintainability<br>
Performance<br>
### 2. System Architecture
```Frontend:```<br>
Languages: HTML, CSS, JavaScript <br>
```Backend:```<br>
Framework: Django<br>
Database: MongoDB (Use pymongo for integration)<br>
```Authentication:```
Service: Clerk<br>
```DevOps:```<br>
Containerization: Docker<br>
CI/CD: GitHub Actions<br>
Code Quality: SonarQube <br><br>
### 3. Detailed Development Plan
Frontend Development<br>
Setup Project Structure:<br>

Folders and files for HTML, CSS, and JavaScript.<br>
Build Pages:<br>

Home Page: Overview of supermarket features.<br>
Login/Register Page: Integrate Clerk for authentication.<br>
Dashboard: Admin panel for managing all functionalities<br>
Inventory Management:<br>
Add/Edit/Delete Products Page<br>
View Products Page
<br>
POS System:<br>
Sales Processing Page<br>
Receipt Generation Page<br>
Customer Management:<br>
Add/Edit/Delete Customers Page<br>
View Customers Page<br>
Employee Management:<br>
Add/Edit/Delete Employees Page<br>
View Employees Page<br>
<br>
Reports:<br>
Sales Reports Page<br>
Inventory Reports Page<br>
<br>
Design Considerations:<br>
Tailwind CSS for responsive design.<br>
Clean and intuitive user interface.<br>
Modal dialogs for add/edit operations.<br>
Display data in tables with sorting and searching functionality.<br>