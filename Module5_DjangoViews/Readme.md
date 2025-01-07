# A . Django Forms

## **Creating and Handling Forms in Django**

Django provides a powerful framework for creating and handling forms. It simplifies tasks like rendering HTML forms, validating user input, and processing form submissions. Forms can be created in Django in two main ways:

### 1. **Manually Creating Forms**

Manually creating forms involves defining HTML forms in your templates and handling form processing in views. This approach gives complete control over the form’s structure and styling.

#### Pros:

- Full control over the HTML and styling.
- No dependency on Django’s form classes.

#### Cons:

- Time-consuming.
- Requires manual handling of validation and data binding.

#### Example:

```html
<form method="POST" action="">
  {% csrf_token %}
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" />
  <button type="submit">Submit</button>
</form>
```

```python
from django.shortcuts import render
from django.http import HttpResponse

def handle_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            return HttpResponse(f"Hello, {name}!")
    return render(request, "form.html")
```

### 2. **Using Django’s Form Classes**

Django’s `forms` module provides a structured way to define forms. The `Form` class is used to define form fields and handle validation.

#### Example:

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

```python
from django.shortcuts import render

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            return HttpResponse(f"Thanks, {name}!")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
```

#### Pros:

- Automatic form generation and validation.
- Built-in widgets for common fields.

#### Cons:

- Less flexibility in customization without overriding default behavior.

#### Ways of Creating forms in Django.

In Django, there are two primary ways to create forms: `forms.Form` and `forms.ModelForm`. Both are used for creating and handling forms, but they differ in functionality and use cases.

### 1. `forms.Form`

`forms.Form` is used when you need to create a form that does not directly relate to a model. It is a more flexible, general-purpose form used for a wide variety of scenarios.

#### **Pros:**

- **Flexibility**: You can create any kind of form, even if it doesn't correspond to a model.
- **Custom Validation**: You have full control over the fields, validation logic, and form handling.
- **Not Tied to Database**: It doesn't automatically interact with a database, making it useful for forms that aren't directly related to a model (like user input or external data).

#### **Cons:**

- **More Boilerplate**: You need to manually handle form fields, validation, and saving data to the database.
- **No Automatic Model Interaction**: You must handle saving and updating model instances manually if needed.

#### **When to Use:**

- When the form data doesn’t need to be directly tied to a database model.
- For complex forms that require custom fields, validation, or special processing not related to a model.
- When you are using external data or custom logic (e.g., APIs, non-model data).

### Example:

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if 'spam' in message:
            raise forms.ValidationError("No spam!")
        return message
```

### 2. `forms.ModelForm`

`forms.ModelForm` is a subclass of `forms.Form` specifically designed to work with Django models. It provides an easy way to create forms that map directly to model instances.

#### **Pros:**

- **Automatic Field Generation**: It automatically generates form fields based on the fields of the associated model.
- **Simplified Code**: You don't need to manually define each field since it's automatically tied to the model's attributes.
- **Easy Save and Update**: You can directly save or update a model instance without needing to handle database operations manually.
- **Validation Built-in**: Model fields come with built-in validation (e.g., field types, constraints like `max_length`, etc.).

#### **Cons:**

- **Less Flexibility**: If you need complex, non-model-related fields or logic, it might not be as flexible as `forms.Form`.
- **Tight Coupling**: It is tightly coupled to a model, making it difficult to use for forms that aren't directly related to the database.
- **Automatic Saving**: It automatically handles saving to the database, but you might not always want this behavior.

#### **When to Use:**

- When the form is directly related to a model (e.g., user registration, profile editing).
- When you want to automatically save form data to the database.
- For forms that need automatic validation and simple creation/editing of model instances.

### Example:

```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
```

### Key Differences:

| Feature                  | `forms.Form`                      | `forms.ModelForm`                                |
| ------------------------ | --------------------------------- | ------------------------------------------------ |
| **Use Case**             | Custom forms not tied to models   | Forms based on models                            |
| **Field Generation**     | Must define fields manually       | Automatically generates fields based on model    |
| **Database Interaction** | No automatic database interaction | Automatically saves and updates database entries |
| **Validation**           | Custom validation logic           | Built-in model validation + custom validation    |
| **Flexibility**          | Highly flexible                   | Tied to model structure                          |

### Summary:

- **Use `forms.Form`** when you need more control over the form and it doesn't directly relate to a model. It’s useful for forms that don’t deal with database models or require complex custom fields and validation.
- **Use `forms.ModelForm`** when your form is directly tied to a model, and you want to simplify form handling with automatic database saving, validation, and field generation.

---

## Default Form Rendering in Templates

In Django, there are several ways to render a form in templates. Each approach offers flexibility for structuring and styling your form. Below are the common methods:

---

### 1. **Using `form.as_p`**

This method renders each field wrapped in a `<p>` tag.

```html
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Submit</button>
</form>
```

---

### 2. **Using `form.as_table`**

This method renders each field as a row in an HTML table.

```html
<form method="post">
  {% csrf_token %} {{ form.as_table }}
  <button type="submit">Submit</button>
</form>
```

---

### 3. **Using `form.as_ul`**

This method renders each field as a list item in an unordered list.

```html
<form method="post">
  {% csrf_token %} {{ form.as_ul }}
  <button type="submit">Submit</button>
</form>
```

---

### 4. **Rendering Fields Individually**

If you need more control over the HTML structure, you can render individual fields using a loop or by explicitly referencing each field.

#### a) **Using a Loop**

```html
<form method="post">
  {% csrf_token %} {% for field in form %}
  <div>{{ field.label_tag }} {{ field }} {{ field.errors }}</div>
  {% endfor %}
  <button type="submit">Submit</button>
</form>
```

#### b) **Explicitly Specifying Fields**

```html
<form method="post">
  {% csrf_token %}
  <div>
    {{ form.username.label_tag }} {{ form.username }} {{ form.username.errors }}
  </div>
  <div>
    {{ form.password.label_tag }} {{ form.password }} {{ form.password.errors }}
  </div>
  <button type="submit">Submit</button>
</form>
```

---

### 5. **Using Custom Templates for Widgets**

For complete customization, you can override the widget templates. For example, if you're using `TextInput` widgets, you can define a custom template in the `templates/widgets/` directory.

#### Example:

Create a custom widget template (`templates/widgets/textinput.html`):

```html
<input
  type="text"
  name="{{ widget.name }}"
  value="{{ widget.value|default:'' }}"
  {{
  widget.attrs|flatatt
  }}
/>
```

Configure it in the form field widget:

```python
from django import forms

class MyForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'template_name': 'widgets/textinput.html'}))
```

---

### 6. **Using `crispy-forms` for Styling**

The [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) library allows you to easily style forms with frameworks like Bootstrap.

#### Installation:

```bash
pip install django-crispy-forms
```

#### Configuration:

Add `'crispy_forms'` to `INSTALLED_APPS` and configure the form renderer:

```python
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

#### Template:

```html
<form method="post">
  {% csrf_token %} {% crispy form %}
  <button type="submit">Submit</button>
</form>
```

---

### 7. **Manually Writing HTML**

For full control, you can write your own HTML and include field attributes manually.

```html
<form method="post">
  {% csrf_token %}
  <div>
    <label for="id_username">Username:</label>
    <input
      type="text"
      id="id_username"
      name="username"
      value="{{ form.username.value }}"
    />
  </div>
  <div>
    <label for="id_password">Password:</label>
    <input type="password" id="id_password" name="password" />
  </div>
  <button type="submit">Submit</button>
</form>
```

---

## **Form Validation and Custom Validators**

### **Form Validation in Django**

Form validation in Django is a process that ensures the data submitted through forms meets specific criteria before it is processed. This is essential to prevent invalid or malicious data from being saved in your database or affecting your application.

### How Form Validation Works in Django

Django provides two main classes for handling forms:

1. **`forms.Form`**: Used for creating simple HTML forms not tied to a model.
2. **`forms.ModelForm`**: Automatically tied to a Django model, making it easier to handle form fields and validation.

Both classes offer built-in validation features and allow custom validations.

---

### **Built-in Validation**

1. **Field Validation**:

   - Django includes validation rules for various fields such as `CharField`, `EmailField`, and `IntegerField`.
   - Example:

     ```python
     from django import forms

     class ContactForm(forms.Form):
         name = forms.CharField(max_length=50, required=True)
         email = forms.EmailField(required=True)
         message = forms.CharField(widget=forms.Textarea, required=True)
     ```

2. **Validators**:

   - Validators are reusable functions for validating specific conditions. For example:

     ```python
     from django.core.validators import MinLengthValidator
     from django import forms

     class UsernameForm(forms.Form):
         username = forms.CharField(validators=[MinLengthValidator(5)])
     ```

3. **Field-specific Validation**:
   - Each field has its own default validation logic. For example:
     - `IntegerField`: Validates input as an integer.
     - `EmailField`: Ensures the value is a valid email address.

---

### **Custom Validation**

1. **`clean_<fieldname>` Method**:

   - Validate individual fields by overriding the `clean_<fieldname>` method.
   - Example:

     ```python
     class SignupForm(forms.Form):
         username = forms.CharField(max_length=50)
         email = forms.EmailField()

         def clean_username(self):
             username = self.cleaned_data.get('username')
             if username.lower() == "admin":
                 raise forms.ValidationError("Username 'admin' is not allowed.")
             return username
     ```

2. **`clean` Method**:

   - Perform validation across multiple fields by overriding the `clean` method.
   - Example:

     ```python
     class SignupForm(forms.Form):
         password = forms.CharField(widget=forms.PasswordInput)
         confirm_password = forms.CharField(widget=forms.PasswordInput)

         def clean(self):
             cleaned_data = super().clean()
             password = cleaned_data.get("password")
             confirm_password = cleaned_data.get("confirm_password")

             if password != confirm_password:
                 raise forms.ValidationError("Passwords do not match.")
     ```

3. **Custom Validators**:

   - Create reusable custom validators.
   - Example:

     ```python
     from django.core.exceptions import ValidationError

     def validate_no_special_characters(value):
         if any(char in "!@#$%^&*()" for char in value):
             raise ValidationError("Special characters are not allowed.")
     ```

---

### **Error Handling**

Django automatically collects validation errors and displays them on the form. You can access these errors using the `form.errors` attribute in your template or view.

Example:

```python
if form.is_valid():
    # Process the form data
    pass
else:
    print(form.errors)  # Print or log the errors
```

---

### **Using Validation with ModelForms**

For `ModelForm`, validation is tightly integrated with the model's field attributes, such as `max_length`, `unique`, and `null`.

Example:

```python
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from the example.com domain.")
        return email
```

### **Client-side Validation**

While Django primarily handles server-side validation, you can enhance user experience by adding client-side validation using JavaScript. For example, you might use the `required` attribute or add custom JavaScript to check field values before submission.

### **Example**

Here is an example demonstrating form validation in Django, including both built-in and custom validation using forms.Form.

---

### **Scenario**

We are creating a **Registration Form** where users must provide a username, email, and password. The form should validate that:

1. The username is not "admin".
2. The email belongs to the "example.com" domain.
3. The password and confirm password fields match.

---

### **Step 1: Create the Form**

```python
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label="Username")
    email = forms.EmailField(required=True, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True, label="Confirm Password")

    # Custom validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username.lower() == "admin":
            raise forms.ValidationError("The username 'admin' is not allowed.")
        return username

    # Custom validation for email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must belong to the 'example.com' domain.")
        return email

    # Cross-field validation for password matching
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
```

---

### **Step 2: Create the View**

```python
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the validated data
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # Do something with the data, like saving to the database
            return HttpResponse(f"Registration successful for {username}!")
        else:
            # Form has errors
            return render(request, "register.html", {"form": form})

    # Render an empty form for GET requests
    form = RegistrationForm()
    return render(request, "register.html", {"form": form})
```

---

### **Step 3: Create the Template**

**`register.html`**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Register</title>
  </head>
  <body>
    <h1>Register</h1>
    <form method="post">
      {% csrf_token %} {{ form.as_p }}
      <button type="submit">Register</button>
    </form>

    {% if form.errors %}
    <h3>Errors:</h3>
    <ul>
      {% for field, errors in form.errors.items %}
      <li><strong>{{ field }}:</strong> {{ errors|join:", " }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </body>
</html>
```

---

### **Step 4: Testing the Form**

1. If the username is "admin", an error message will appear:  
   `The username 'admin' is not allowed.`

2. If the email is not from the "example.com" domain, an error message will appear:  
   `Email must belong to the 'example.com' domain.`

3. If the password and confirm password do not match, an error message will appear:  
   `Passwords do not match.`

4. If all fields are valid, a success message will be displayed:  
   `Registration successful for [username]!`

---

## **Formsets and Inline Formsets**

#### **1. Formsets**

A **Formset** in Django is a way to manage multiple forms on a single page. It is essentially a collection of forms that share the same structure but handle multiple instances of data.

##### **How to Use Formsets**

1. **Define a Form:**
   Create a standard Django form for your model or any data.

   ```python
   from django import forms
   from .models import Author

   class AuthorForm(forms.ModelForm):
       class Meta:
           model = Author
           fields = ['name', 'email']
   ```

2. **Create a Formset:**
   Use Django's `formset_factory` to create a formset from the form.

   ```python
   from django.forms import formset_factory

   AuthorFormSet = formset_factory(AuthorForm, extra=2)
   ```

3. **Render in the Template:**
   Pass the formset to the template and loop through its forms.

   ```python
   # views.py
   def manage_authors(request):
       formset = AuthorFormSet()
       return render(request, 'manage_authors.html', {'formset': formset})
   ```

   ```html
   <!-- manage_authors.html -->
   <form method="post">
     {{ formset.management_form }} {% for form in formset %} {{ form.as_p }} {%
     endfor %}
     <button type="submit">Save</button>
   </form>
   ```

4. **Handle Form Submission:**
   Validate and save the data.

   ```python
   def manage_authors(request):
       if request.method == "POST":
           formset = AuthorFormSet(request.POST)
           if formset.is_valid():
               for form in formset:
                   form.save()
       else:
           formset = AuthorFormSet()
       return render(request, 'manage_authors.html', {'formset': formset})
   ```

##### **Real-World Use Case**

- A survey where the user needs to input responses for multiple questions of the same type.
- Adding multiple email addresses for a user in a contact form.

---

#### **2. Inline Formsets**

An **Inline Formset** is a specialized version of a formset tied to a parent model and its related model. It's used when you want to handle data for a parent and its child models on the same form.

##### **How to Use Inline Formsets**

1. **Define the Models:**

   ```python
   from django.db import models

   class Author(models.Model):
       name = models.CharField(max_length=100)

   class Book(models.Model):
       title = models.CharField(max_length=100)
       author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
   ```

2. **Create an Inline Formset:**

   ```python
   from django.forms import inlineformset_factory

   BookInlineFormSet = inlineformset_factory(Author, Book, fields=('title',), extra=2)
   ```

3. **Render in the Template:**
   Pass the inline formset to the template.

   ```python
   def manage_books(request, author_id):
       author = Author.objects.get(id=author_id)
       formset = BookInlineFormSet(instance=author)
       return render(request, 'manage_books.html', {'formset': formset, 'author': author})
   ```

   ```html
   <!-- manage_books.html -->
   <form method="post">
     {{ formset.management_form }} {% for form in formset %} {{ form.as_p }} {%
     endfor %}
     <button type="submit">Save</button>
   </form>
   ```

4. **Handle Form Submission:**

   ```python
   def manage_books(request, author_id):
       author = Author.objects.get(id=author_id)
       if request.method == "POST":
           formset = BookInlineFormSet(request.POST, instance=author)
           if formset.is_valid():
               formset.save()
       else:
           formset = BookInlineFormSet(instance=author)
       return render(request, 'manage_books.html', {'formset': formset, 'author': author})
   ```

##### **Real-World Use Case**

- Adding or editing books for a specific author in one form.
- Managing items in an order for a specific customer.

---

#### **Difference Between Formsets and Inline Formsets**

| Feature              | Formsets                                         | Inline Formsets                                      |
| -------------------- | ------------------------------------------------ | ---------------------------------------------------- |
| **Purpose**          | Manage multiple forms for the same type of data. | Manage child forms related to a parent model.        |
| **Relation**         | No parent-child relationship required.           | Requires a parent-child relationship between models. |
| **Data Scope**       | Handles independent forms.                       | Handles related model forms.                         |
| **Example Use Case** | Adding multiple authors.                         | Adding multiple books for an author.                 |

Both Formsets and Inline Formsets simplify managing multiple forms, but Inline Formsets shine when handling related models.

---

# B. Authentication and Authorization

Django provides a robust built-in authentication system that simplifies user management, login, registration, and access control. Here's a detailed explanation of its components:

### 1. Managing Users, Groups, and Permissions

#### Users:

- **User Model**: Django includes a `User` model, which stores essential information about users such as username, email, password, first and last name, and date of birth. The `User` model is included in `django.contrib.auth.models` and can be extended to meet specific project needs.
- **Creating Users**: You can create users using Django's `User` model or the `UserManager` class. Django provides methods like `User.objects.create_user()` for creating users with hashed passwords.

```python
from django.contrib.auth.models import User

user = User.objects.create_user(username='john', email='john@example.com', password='password')
```

#### Groups:

- **Groups**: Groups are collections of users. Each group can have certain permissions assigned, and users belonging to that group inherit those permissions. Groups are defined using `Group` model in `django.contrib.auth.models`.

```python
from django.contrib.auth.models import Group

# Creating a group
admin_group = Group.objects.create(name='Admin')
```

#### Permissions:

- **Permissions**: Permissions define the actions a user or group can perform. They can be assigned to individual users or groups. You can use Django's built-in permissions (add, change, delete, view) or create custom permissions.

```python
from django.contrib.auth.models import Permission

# Assigning permission to a user
user = User.objects.get(username='john')
permission = Permission.objects.get(codename='can_edit')
user.user_permissions.add(permission)
```

### 2. Login, Logout, and Registration Views

Django provides views and forms to manage login, logout, and user registration:

#### Login View:

- Django has a built-in `LoginView` that handles user authentication. It takes care of verifying the username and password, and if successful, it creates a session.

```python
from django.contrib.auth.views import LoginView

# URL pattern
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
```

#### Logout View:

- The `LogoutView` ends the user session. Once the user logs out, their session data is cleared, and they are redirected to a specified URL (usually the homepage).

```python
from django.contrib.auth.views import LogoutView

# URL pattern
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
]
```

#### Registration View:

- Django doesn’t provide a built-in registration view, but you can easily create one using a form that accepts user data and registers a new user. You can use Django's `UserCreationForm` for this.

```python
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
```

### 3. Implementing Role-Based Access Control (RBAC)

RBAC (Role-Based Access Control) in Django can be implemented using **Groups** and **Permissions**.

#### Role-Based Access Control:

- **Role**: A role is defined by a group. Each role can be associated with specific permissions (like viewing or editing certain models).
- You can define different roles for your users such as `Admin`, `Manager`, or `Editor`. You assign permissions to these roles, and then assign users to these roles (groups).
- Access control can be handled by checking if a user has the necessary permissions or group membership.

#### Example of Role-Based Access Control:

You could create a view where users can only access the content if they belong to the `Admin` group.

```python
from django.contrib.auth.decorators import user_passes_test

# Decorator for checking if the user is an admin
@user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
```

### 4. Resetting Passwords and Email Verification

#### Password Reset:

- Django includes built-in views for password reset that handle sending an email to the user with a password reset link.

```python
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
```

- The password reset process involves:
  1. **Password Reset Request**: The user enters their email.
  2. **Email with Reset Link**: A link is sent to the user’s email with a token.
  3. **Password Reset**: The user enters a new password on the reset form.

#### Email Verification:

- **Email Verification**: Django doesn’t provide built-in email verification, but you can implement this functionality by sending an email with a verification link (containing a token). After the user clicks the link, you can activate their account.

```python
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

def send_verification_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(str(user.pk).encode())
    verification_url = f"http://{get_current_site(request).domain}/verify/{uid}/{token}"
    send_mail('Verify your email', f'Click here to verify your email: {verification_url}', 'noreply@mydomain.com', [user.email])
```

# C. Miscellaneous

### 1. **Django Signals**

Django **signals** are a mechanism for decoupling different parts of an application. They allow certain senders to notify subscribers when specific actions occur. Signals help in implementing event-driven programming in Django.

#### Commonly Used Signals:

- `pre_save` / `post_save`: Triggered before or after a model's save operation.
- `pre_delete` / `post_delete`: Triggered before or after a model is deleted.
- Custom signals can also be created.

#### Example: Using `post_save` Signal

```python
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

```python
# apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals  # Import signals here
```

In this example, a `Profile` instance is automatically created whenever a new `User` instance is saved.

---

### 2. **Context Processors**

Context processors are Python functions that return a dictionary of data to be added to the template context. These are globally available in templates without passing explicitly through the view.

#### Example: Custom Context Processor

1. Create a context processor:

```python
# context_processors.py
def site_name(request):
    return {
        'site_name': 'My Django Site'
    }
```

2. Add it to `TEMPLATES` in `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'myapp.context_processors.site_name',  # Add here
            ],
        },
    },
]
```

3. Use it in a template:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ site_name }}</title>
  </head>
  <body>
    <h1>Welcome to {{ site_name }}</h1>
  </body>
</html>
```

The `site_name` variable will now be available in all templates.

---

### 3. **`re_path`**

`re_path` is used to define URL patterns with regular expressions. It's similar to `path` but allows more complex matching using regex.

#### Example: Using `re_path`

```python
# urls.py
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^articles/(\d{4})/$', views.year_archive, name='year_archive'),
]
```

#### Explanation:

- The URL pattern `^articles/(\d{4})/$` matches URLs like `articles/2025/`.
- `(\d{4})` captures a 4-digit number, which is passed to the `year_archive` view.

#### View Function:

```python
# views.py
from django.http import HttpResponse

def year_archive(request, year):
    return HttpResponse(f"Articles from the year {year}")
```

When a user visits `/articles/2025/`, the response will be:  
`Articles from the year 2025`.

---
