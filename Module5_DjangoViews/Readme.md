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

## Authentication and Authorization
