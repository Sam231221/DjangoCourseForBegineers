Here’s a comprehensive **Django commands cheatsheet** for quick reference:

---

### **Project Commands**

1. **Create a new project**
   ```bash
   django-admin startproject project_name
   ```
   To create as a base project_name
   ```bash
   django-admin startproject project_name .
   ```
2. **Run the development server**
   ```bash
   python manage.py runserver
   ```
3. **Change the port of the server (default is 8000)**
   ```bash
   python manage.py runserver 8080
   ```
4. **Create a new app**
   ```bash
   python manage.py startapp app_name
   ```

---

### **Database Commands**

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
6. **Create a new migration file (after model changes)**
   ```bash
   python manage.py makemigrations
   ```
7. **Check SQL queries for a migration**
   ```bash
   python manage.py sqlmigrate app_name migration_number
   ```
   Example:
   ```bash
   python manage.py sqlmigrate myapp 0001
   ```
8. **Inspect the database schema**
   ```bash
   python manage.py inspectdb
   ```
9. **Reset migrations (delete and recreate)**
   ```bash
   find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
   python manage.py makemigrations
   python manage.py migrate --fake-initial
   ```

---

### **User Management**

10. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```
11. **Change a user’s password**
    ```bash
    python manage.py changepassword username
    ```

---

### **Managing Requirements files**

12. **Appending dependencies to requriements.txt file**
    ```bash
    pip freeze > requirements.txt
    ```
    Creates a file(if not already present) enlisting all the dependencies required for your project.
13. **Installing requirements for your project**
    ```bash
    pip install -r requirements.txt
    ```

---

### **Testing and Debugging**

12. **Run tests**
    ```bash
    python manage.py test
    ```
13. **Check for errors (linting)**
    ```bash
    python manage.py check
    ```

---

### **Data Management**

14. **Load data from a JSON file**
    ```bash
    python manage.py loaddata filename.json
    ```
15. **Dump data to a JSON file**

    ```bash
    python manage.py dumpdata myapp --exclude auth --exclude contenttypes --exclude sessions --exclude admin.logentry --indent 4 > fixtures/data.json

    ```

16. **Delete database entries**
    ```bash
    python manage.py flush
    ```
    **Note:** This will remove all data from the database but keep the schema intact.

---

### **Admin and Shell**

17. **Open the Django shell**
    ```bash
    python manage.py shell
    ```
18. **Clear the session table**
    ```bash
    python manage.py clearsessions
    ```

---

### **Static Files**

19. **Collect static files**
    ```bash
    python manage.py collectstatic
    ```
20. **Clear static files (before re-collecting them)**
    ```bash
    python manage.py collectstatic --clear
    ```

---

### **Advanced**

21. **Start a custom command**

    ```bash
    python manage.py mycustomcommand
    ```

    **To create a custom command:**

    - Create a `management/commands` folder in your app.
    - Add a Python file for the command.
    - Example path: `myapp/management/commands/mycustomcommand.py`

22. **Show available commands**
    ```bash
    python manage.py help
    ```
23. **Show detailed help for a command**
    ```bash
    python manage.py help command_name
    ```

---
