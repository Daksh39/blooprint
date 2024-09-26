# Inventory Management API with Django Rest Framework

## Objective
Create a backend API for managing inventory items with CRUD operations, JWT authentication, and caching.

## Requirements
- **Framework**: Django Rest Framework (DRF)
- **Database**: PostgreSQL
- **Caching**: Redis
- **Authentication**: JWT
- **Logging**: Integrated logging system
- **Testing**: Unit tests with Django's test framework

## Endpoints

### 1. Authentication
- **Register/Login**: JWT-based authentication for all CRUD operations.

### 2. Item Endpoints
- **Create Item**: `POST /items/`
- **Read Item**: `GET /items/{item_id}/`
- **Update Item**: `PUT /items/{item_id}/`
- **Delete Item**: `DELETE /items/{item_id}/`

### Error Codes
- `400`: Item already exists.
- `404`: Item not found.

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Daksh39/blog-django.git

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

3. **Set Up the Database**
   ```bash
   python manage.py migrate

4. **Create a Superuser**
    ```bash
    python manage.py createsuperuser

5. **Run the Development Server**
    ```bash
    python manage.py runserver

6. **Running Tests**
   ```bash
   python manage.py test
