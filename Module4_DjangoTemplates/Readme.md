### **1. Working with Django Templates**

#### **Introduction to Django Template Language (DTL)**

- Django Template Language is a lightweight syntax for dynamically generating HTML using Python data.
- **Key Features**:
  - **Variables**: Display data from the context using `{{ variable }}`.
  - **Tags**: Perform logical operations like loops (`{% for %}`) and conditionals (`{% if %}`).
  - **Filters**: Modify data with built-in filters like `{{ name|upper }}` (converts text to uppercase).

#### **Template Inheritance and Block Tags**

- Reuse and organize templates with a **base template**.
- **Base Template**:
  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>{% block title %}Default Title{% endblock %}</title>
      <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
    </head>
    <body>
      {% block content %}{% endblock %}
    </body>
  </html>
  ```
- **Child Template**:
  ```html
  {% extends "base.html" %} {% block title %}Home Page{% endblock %} {% block
  content %}
  <h1>Welcome to the Home Page!</h1>
  {% endblock %}
  ```

#### **Rendering Data in Templates**

- Pass data from views to templates via context:
  ```python
  def home(request):
      context = {'name': 'John Doe'}
      return render(request, 'home.html', context)
  ```
- Access in templates:
  ```html
  <p>Hello, {{ name }}!</p>
  ```

---

#### **Template Tags**

Template tags are special syntax constructs that allow you to perform logic, include content, or interact with data in templates. They are enclosed within `{% %}`.

##### **Common Template Tags**

1. **Control Flow Tags**

   - Used for conditional logic or loops.

   **Examples:**

   - `{% if %}`: Checks conditions.

   ```html
   {% if user.is_authenticated %}
   <p>Welcome, {{ user.username }}!</p>
   {% else %}
   <p>Please log in.</p>
   {% endif %}
   ```

   - `{% for %}`: Iterates over a sequence.

   ```html
   <ul>
     {% for item in items %}
     <li>{{ item }}</li>
     {% endfor %}
   </ul>
   ```

   - `{% elif %}`: Adds additional conditions in `if`.
   - `{% empty %}`: Handles cases when a loop is empty.

   ```html
   <ul>
     {% for item in items %}
     <li>{{ item }}</li>
     {% empty %}
     <p>No items found.</p>
     {% endfor %}
   </ul>
   ```

2. **Variable Tags**

   - Modify or display content.
   - `{% with %}`: Simplifies context variable management.

   ```html
   {% with total=items.count %} Total items: {{ total }} {% endwith %}
   ```

3. **Include Tags**

   - `{% include %}`: Embeds another template.

   ```html
   {% include "header.html" %}
   ```

   - Useful for reusable components like headers and footers.

4. **Static File Handling**

   - `{% static %}`: Refers to static files.

   ```html
   <img src="{% static 'images/logo.png' %}" alt="Logo" />
   ```

5. **CSRF Protection**

   - `{% csrf_token %}`: Adds CSRF token for secure form submissions.

   ```html
   <form method="post">
     {% csrf_token %}
     <!-- form fields -->
   </form>
   ```

6. **URL Handling**

   - `{% url %}`: Creates URLs dynamically.

   ```html
   <a href="{% url 'app_name:view_name' arg1 arg2 %}">Link</a>
   ```

7. **Block and Extend Tags**

   - `{% block %}`: Defines a block of content in a child template.
   - `{% extends %}`: Extends a base template.

   ```html
   <!-- base.html -->
   <html>
     <head>
       {% block title %}Title{% endblock %}
     </head>
     <body>
       {% block content %}{% endblock %}
     </body>
   </html>

   <!-- child.html -->
   {% extends "base.html" %} {% block title %}Child Page{% endblock %} {% block
   content %}
   <p>Content for the child page.</p>
   {% endblock %}
   ```

8. **Custom Tags**
   - Developers can create custom tags using Python and `@register.simple_tag`.

---

#### **Template Filters**

Filters are used to transform variables and are applied using the `|` operator. For example, `{{ name|lower }}` converts the `name` variable to lowercase.

##### **Commonly Used Filters**

1. **String Manipulation**

   - `lower`: Converts a string to lowercase.
   - `upper`: Converts a string to uppercase.
   - `title`: Capitalizes the first letter of each word.
   - `default`: Provides a default value if the variable is `None`.

   ```html
   {{ name|default:"Guest" }}
   ```

2. **Date and Time**

   - `date`: Formats a date.

   ```html
   {{ date|date:"D M Y" }}
   ```

   - `time`: Formats a time.

   ```html
   {{ time|time:"H:i:s" }}
   ```

3. **Formatting**

   - `escape`: Escapes HTML characters.
   - `safe`: Marks content as safe for rendering.

   ```html
   {{ raw_html|safe }}
   ```

4. **Iteration and Counting**

   - `length`: Returns the length of a list or string.

   ```html
   {{ items|length }}
   ```

   - `slice`: Extracts a subset.

   ```html
   {{ items|slice:":3" }}
   ```

5. **Math and Logic**

   - `add`: Adds a value.

   ```html
   {{ number|add:5 }}
   ```

   - `yesno`: Converts Boolean values to custom text.

   ```html
   {{ is_active|yesno:"Yes,No" }}
   ```

6. **Custom Filters**
   - Custom filters can be created using Python.
   ```python
   @register.filter
   def custom_filter(value):
       return value[::-1]
   ```

---

#### **How to Use Custom Tags and Filters**

1. **Create a `templatetags` Directory**

   - In the app folder, create a directory named `templatetags`.
   - Add an empty `__init__.py` file to make it a module.

2. **Define Tags and Filters**

   - Create a `.py` file, e.g., `custom_tags.py`.

   ```python
   from django import template

   register = template.Library()

   @register.simple_tag
   def custom_tag(arg1, arg2):
       return f"{arg1} and {arg2}"

   @register.filter
   def reverse_string(value):
       return value[::-1]
   ```

3. **Load in Templates**
   ```html
   {% load custom_tags %}
   ```

---

#### **Handling Static Files (CSS, JavaScript, Images) and Media files(Videos) in Templates**

- Static files are stored in `static/` and referenced using the `{% static %}` tag.
- **Setup**:

  ```python
  # settings.py
  STATIC_URL = '/staticfiles/'
  STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'staticfiles')
  ]
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')

  MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/mediafiles')
  MEDIA_URL = '/mediafiles/'
  ```

- **Example**:
  ```html
  <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  <script src="{% static 'js/script.js' %}"></script>
  <img src="{% static 'images/logo.png' %}" alt="Logo" />
  ```

---

### **2. Integrating Frontend with Django**

#### **Using Bootstrap and External CSS/JS Libraries**

- Include Bootstrap via CDN:
  ```html
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
  />
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
  ```
- Use Bootstrap classes for responsive design:
  ```html
  <div class="container">
    <h1 class="text-center">Welcome!</h1>
    <button class="btn btn-primary">Click Me</button>
  </div>
  ```
- Add external CSS/JS libraries similarly.

#### **Using Bootstrap and External CSS/JS Libraries**

To use Tailwind CSS as a CDN in a Django project, follow these steps:

---

#### 1. **Add Tailwind CDN to Your Django Templates**

In your base HTML file (e.g., `base.html`), include the Tailwind CSS CDN link in the `<head>` section:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}Django Project{% endblock %}</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    {% block content %} {% endblock %}
  </body>
</html>
```

---

#### 2. **Enable Tailwind Configuration (Optional)**

You can enable custom configurations like themes or plugins by using `tailwind.config` through the CDN. Add a `<script>` block after the Tailwind CDN to configure it:

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          primary: "#1da1f2",
          secondary: "#14202a",
        },
      },
    },
  };
</script>
```

---

#### 3. **Use Tailwind Classes in Django Templates**

You can now use Tailwind CSS classes directly in your Django templates. For example:

```html
<div class="p-4 bg-primary text-white">
  <h1 class="text-2xl font-bold">Welcome to Django</h1>
  <p class="text-sm">Styled using Tailwind CSS CDN</p>
</div>
```

---

#### **Forms and Validation in Django Templates**

- Render forms using Django’s built-in `forms` module.
- **Example**:

  ```python
  from django import forms

  class ContactForm(forms.Form):
      name = forms.CharField(max_length=100)
      email = forms.EmailField()
      message = forms.CharField(widget=forms.Textarea)
  ```

  - Template:
    ```html
    <form method="post">
      {% csrf_token %} {{ form.as_p }}
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    ```

- Add validation rules in the form class, e.g., `clean_<fieldname>()`.

#### **Rendering Dynamic Content in Templates**

- Use context data to dynamically populate templates:
  ```python
  def products(request):
      items = ['Laptop', 'Phone', 'Tablet']
      return render(request, 'products.html', {'items': items})
  ```
- Template:
  ```html
  <ul>
    {% for item in items %}
    <li>{{ item }}</li>
    {% endfor %}
  </ul>
  ```

#### **Handling Form Submissions and CSRF Protection**

- **CSRF Protection**:
  - Always include `{% csrf_token %}` in forms to protect against Cross-Site Request Forgery.
  - Example:
    ```html
    <form method="post">
      {% csrf_token %}
      <input type="text" name="username" required />
      <button type="submit">Submit</button>
    </form>
    ```
- **Processing Form Submissions**:
  ```python
  def contact_view(request):
      if request.method == 'POST':
          form = ContactForm(request.POST)
          if form.is_valid():
              # Process form data
              print(form.cleaned_data)
      else:
          form = ContactForm()
      return render(request, 'contact.html', {'form': form})
  ```

---
