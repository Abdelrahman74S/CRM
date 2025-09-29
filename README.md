# Django CRM

A simple, web-based Customer Relationship Management (CRM) system built with Django to help you manage customer data and interactions effectively.

## Features

*   **User Authentication**: Secure user registration and login system.
*   **Customer Record Management**: Easily create, view, update, and delete customer records.
*   **Clean UI**: A responsive and user-friendly interface built with Bootstrap and Crispy Forms.
*   **Dashboard**: A central dashboard to view all customer records at a glance.

## Technologies Used

*   [Python](https://www.python.org/)
*   [Django](https://www.djangoproject.com/)
*   [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) for form rendering.
*   [Bootstrap](https://getbootstrap.com/) for front-end styling.
*   SQLite3 (default database).

## Prerequisites

Before you begin, ensure you have the following installed on your system:
*   Python 3.8+
*   pip (Python package installer)
*   Git

## Installation and Setup

Follow these steps to get your development environment set up:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Abdelrahman74S/CRM.git
    cd src
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    *(Note: Make sure you have a `requirements.txt` file in your project's root directory.)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.
