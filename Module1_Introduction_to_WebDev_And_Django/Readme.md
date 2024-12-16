## Module 1: Introduction to Web Development and Django Framework

### Overview of Web Development

#### Introduction to Web Development and Frameworks

Web development refers to the process of building and maintaining websites and web applications that are accessible over the internet. It involves both technical and creative aspects, such as designing the layout, ensuring responsiveness, and enabling dynamic interactions with users. Frameworks are pre-built software tools and libraries that simplify web development by providing reusable code, components, and best practices. Examples include Django, React, and Laravel.

#### Understanding Client-Server Architecture

The client-server architecture is the foundation of web development. It consists of two main components:

- **Client:** The front-facing part where users interact, typically through a web browser or mobile application.
- **Server:** The backend system that processes requests from the client, retrieves or manipulates data, and sends responses back to the client.
  For example, when a user submits a login form, the client sends the form data to the server for validation, and the server responds with the appropriate result.

#### Overview of Frontend vs Backend

- **Frontend:** Refers to the visual and interactive aspects of a website, developed using languages like HTML, CSS, and JavaScript. Frameworks like React and Angular enhance frontend development.
- **Backend:** Involves the server-side logic, database interactions, and application functionalities, developed using languages like Python, Ruby, or PHP. Frameworks like Django and Flask streamline backend development.

### Introduction to Django

#### What is Django?

Django is a high-level Python web framework that simplifies the development of secure, scalable, and maintainable web applications. It is known for its "batteries-included" philosophy, offering built-in features such as authentication, ORM (Object-Relational Mapping), and an admin interface.

#### Key Features of Django Framework

1. **Fast Development:** Django's modular structure and ready-to-use components accelerate the development process.
2. **Secure:** Built-in security features protect against common vulnerabilities such as SQL injection, XSS, and CSRF.
3. **Scalable:** Suitable for handling high traffic and complex applications.
4. **Flexible:** Works seamlessly with various databases and frontend technologies.

#### The Django MVC (Model-View-Controller) Pattern

Django follows the **Model-View-Controller (MVC)** pattern, which is modified as **Model-View-Template (MVT)** in Django:

- **Model:** Handles database structure and interactions.
- **View:** Contains the business logic and processes user requests.
- **Template:** Manages the presentation layer by defining the structure of web pages.

#### Installing Django and Setting Up the Development Environment

1. **Prerequisites:** Ensure Python and pip (Python package manager) are installed.
2. **Install Django:** Run the command: `pip install django`.
3. **Verify Installation:** Check the Django version using: `django-admin --version`.
4. **Set Up Development Environment:** Use virtual environments for isolated development:
   - Create: `python -m venv env`
   - Activate:
     - Windows: `env\Scripts\activate`
     - Mac/Linux: `source env/bin/activate`

### First Django Project

#### Poetry

Poetry is a modern dependency and packaging tool for Python. It offers a streamlined way to manage your project's dependencies, including Django.

**Key Benefits of Using Poetry with Django:**

- **Dependency Management:** Poetry simplifies the process of managing dependencies, ensuring that your project uses the correct versions of packages.
- **Virtual Environments:** Poetry automatically creates and manages virtual environments, isolating project dependencies from your system-wide Python installation.
- **Packaging and Distribution:** You can easily package and distribute your Django project using Poetry's packaging capabilities.
- **Reproducible Environments:** Poetry's lock file guarantees that your project can be reliably reproduced on different machines.

#### **Setting Up a Django Project with Poetry**

#### 1. **Install Poetry**

- **On macOS/Linux:**
  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```
- **On Windows:**
  - Download the installer from the official website.
  - Follow the installation instructions.
  - You can install it using pip package manager
  ```
  pip install poetry
  ```

#### 2. **Create a New Poetry Project**

- Navigate to your desired project directory in your terminal.
- Initialize a new Poetry project:
  ```bash
  poetry init
  ```
  - Follow the prompts to provide basic information about your project.

### 3. **Add Django as a Dependency**

- Add Django to your `pyproject.toml` file:
  ```bash
  poetry add django
  ```

### 4. **Create a Django Project**

- Use the `poetry run` command to execute Django commands within your Poetry environment:
  ```bash
  poetry run django-admin startproject my_project
  ```
  Replace `my_project` with your desired project name.

### 5. **Activate the Virtual Environment**

- To activate the virtual environment created by Poetry:
  ```bash
  poetry shell
  ```

### 6. **Run the Development Server**

- Navigate to your project directory:
  ```bash
  cd my_project
  ```
- Append the inital migration to the database:

  ```bash
  python manage.py migrate
  ```

  Note: db.sqlite3 is created in the root directory

- Start the development server:
  ```bash
  python manage.py runserver
  ```

#### Django Project Structure Explained

1. **manage.py:** Command-line utility for managing the project.
2. **settings.py:** Configuration settings for the project.
3. **urls.py:** Defines URL patterns for routing.
4. **wsgi.py/asgi.py:** Gateway interfaces for deploying the application.
5. **App Folder:** Contains files such as `models.py`, `views.py`, `admin.py`, and `tests.py` for app-specific functionality.
6. \***\*pycache** and **init**.py:\*\*
   The `__pycache__` folder and `__init__.py` file play specific roles in Python projects, including Django applications:

---

#### **`__pycache__` Folder**

This folder contains compiled bytecode files for Python modules. These are files with extensions like `.pyc` or `.pyo` and are generated automatically when Python scripts are executed.
The compiled bytecode helps Python execute the code faster because it avoids recompiling the `.py` files every time they are run.

**In Django**: It stores compiled versions of Python files in your Django app, making subsequent runs of your app slightly faster.

- **Key Points**:
  - You can safely delete the `__pycache__` folder; Python will recreate it when needed.
  - It is typically ignored in version control (e.g., added to `.gitignore`).

---

#### **`__init__.py` File**

The `__init__.py` file indicates that the directory it is in should be treated as a Python package. This allows Python to import modules from that directory.

**In Django**:

- Every app folder in a Django project is a Python package, so it usually includes an `__init__.py` file (even if it's empty).
- In complex apps, you can use this file to define app-level imports, configurations, or initializations.
- **Key Points**:
  - It can be empty or include Python code.
  - In modern Python versions, the `__init__.py` file is not strictly required but is still widely used for clarity and compatibility.

---

#### Example

1. **`__pycache__`**:

   - If you have a `views.py` file in your app, Python will create a `views.cpython-XX.pyc` file inside `__pycache__` after running your app.

2. **`__init__.py`**:

   - In your Django app folder, you might find an empty `__init__.py` to mark it as a package.
   - Example use:
     ```python
     # myapp/__init__.py
     from .models import MyModel
     ```

   This allows you to import `MyModel` directly from `myapp`:

   ```python
   from myapp import MyModel
   ```

---

**Note: There are other files like views.py and folders like templates which we define later.**

#### Running the Development Server

1. **Start Server:** Use the command: `python manage.py runserver`.
2. **Access Application:** Open `http://127.0.0.1:8000/` in a web browser.
3. **Stop Server:** Use `Ctrl+C` to terminate the server.

#### Introduction to Django Admin Interface

1. **Creating a user:** Add a superuser using: `python manage.py createsuperuser` for accessing admin pages.
2. **Access Admin Interface:** Navigate to `http://127.0.0.1:8000/admin/` and log in with superuser credentials.
3. **Manage Data:** Use the admin interface to view, add, update, or delete database records.
