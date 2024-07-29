# Recipe Platform

## Description

Recipe Platform is a Django web application that allows users to create, view, and manage recipes. It includes features for user authentication, recipe management, and an "about" page.

## Features

- User authentication (login, signup, logout)
- Recipe creation and management
- Recipe listing
- User-friendly interface with Bootstrap
- About page with project information

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.12.x
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository:**

    ```bash
    git clone <repository-URL>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    ```

    **Activate the virtual environment:**

    - **Windows:**

      ```bash
      venv\Scripts\activate
      ```

    - **macOS/Linux:**

      ```bash
      source venv/bin/activate
      ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure

- **manage.py**: Command-line utility for administrative tasks.
- **recipe_platform/**: Main project directory.
  - **settings.py**: Project settings.
  - **urls.py**: URL configurations.
- **recipes/**: App directory containing models, views, and templates for recipes.
- **static/**: Directory for static files (CSS, JavaScript, images).
- **media/**: Directory for uploaded media files.
- **requirements.txt**: File listing project dependencies.

## Contributing

Contributions are welcome! Please follow these guidelines:
1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a pull request.


## Acknowledgments

- Django framework
- Bootstrap for styling

