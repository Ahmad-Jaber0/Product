# Product Management System

This project is a basic **Product Management System** built with **Django**. It allows users to add, update, and delete products via a RESTful API. AJAX is used to interact with the API, making the system dynamic and responsive. The main focus of this project is backend functionality, with minimal frontend emphasis.

## Features

- Add new products
- Update product details
- Delete products
- View the list of all products
- API-based interaction using AJAX

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript, AJAX
- **Database**: SQLite
- **Version Control**: Git, GitHub

## Setup and Installation

### Prerequisites

- Python 3.12.2
- Django
- Django REST Framework

### Steps to Run the Project Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Ahmad-Jaber0/Product.git
    cd product-management-system
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Apply the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the server**:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and visit `http://127.0.0.1:8000/` to interact with the product management system.

## API Endpoints

Here are the main API endpoints used in the system:

- **GET /**: Fetch the homepage or product listing (index view).
- **POST /add-product/**: Add a new product.
- **PUT /edit-product/<int:pk>/**: Update an existing product by its primary key (`pk`).
- **DELETE /delete-product/<int:pk>/**: Delete a product by its primary key (`pk`).
