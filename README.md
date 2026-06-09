# Shopping Mall Management System

A responsive web application developed using the Django MVC framework designed to simplify product records, track available store stocks, and manage retail inventories seamlessly.

This project was engineered as an Open-Ended Lab (OEL) assignment for the Web Engineering Course (CYS-463) at the University of Wah, Computer Science Department.

---

## Key Features

* **📦 Comprehensive CRUD Architecture:** Full pipeline capability allowing shop managers to Add new products, View current inventories, Edit item fields, and Delete outdated listings.
* **⚡ Dynamic Stock Control:** Interactive backend management layout to seamlessly update item quantities, categories, and pricing instantly.
* **🔍 Live Filter & Search Engine:** A functional query filter built directly into the central dashboard to look up specific product entries instantly by their item names.
* **🛡️ Client-Side Validation Form:** Integrated custom front-end JavaScript loops to intercept and validate input data fields securely before submittal to prevent negative quantities or empty logs.
* **📱 Grid Fluid Layout:** Styled comprehensively using Bootstrap 5 to ensure a fully mobile-responsive administration interface across all screen sizes.

---

## Technology Stack

* **Backend Framework:** Python & Django (utilizing Django ORM and Form validation layers)
* **Frontend Canvas:** HTML5, CSS3, Bootstrap 5, and Django Template Language (DTL)
* **Client Scripts:** Vanilla JavaScript (ES6+)
* **Database Engine:** SQLite 3

---

## Modular Application Architecture

The project directory follows clean modular design separation across four explicit operational zones:
1. **Data Model (`models.py`):** Establishes the database schema structure detailing item properties such as product name, unit price, stock quantity, and category strings.
2. **Input Controller (`forms.py`):** Translates structural database definitions directly into secure HTML rendering forms while injecting standard responsive UI classes.
3. **Logic Processor (`views.py`):** Manages requests, filters data querysets using active search keywords, removes items securely, and saves new form sets.
4. **Endpoint Router (`urls.py`):** Manages clean navigation mapping, directly binding network paths onto targeted logical view routines.

---

## Installation & Local Setup

Deploy a local copy of this environment running on your machine by following these instructions:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/shopping-mall-management.git](https://github.com/YOUR_USERNAME/shopping-mall-management.git)
   cd shopping-mall-management
