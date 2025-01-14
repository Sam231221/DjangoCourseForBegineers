## **A. Introduction to REST APIs**

**API: A Bridge Between Software**

An API, or Application Programming Interface, is essentially a set of rules and protocols that allow different software applications to communicate and interact with each other. Think of it as a messenger that carries requests and responses between two systems.

**Types of APIs**

There are several types of APIs, each serving a specific purpose:

1. **Public APIs:**

   - Openly accessible to the public.
   - No restrictions on usage.
   - Examples: Google Maps API, Twitter API

2. **Partner APIs:**

   - Restricted to specific business partners or clients.
   - Require authorization or API keys.
   - Examples: APIs for accessing partner-only data or services

3. **Private APIs:**

   - Used internally within a single organization.
   - Not exposed to external users.
   - Examples: APIs for managing internal systems or databases

4. **Composite APIs:**
   - Combine data and services from multiple sources into a single API endpoint.
   - Streamline complex tasks by providing a unified interface.
   - Examples: APIs that combine weather data, traffic information, and restaurant reviews

### **REST API: A Popular Architectural Style**

**Representational State Transfer (REST)** is a popular architectural style for building APIs.

- It utilizes the HTTP protocol for communication, employing methods like GET, POST, PUT, and DELETE to interact with resources.
- REST APIs are known for their simplicity, flexibility, and scalability.

**Key Characteristics of REST APIs:**

- **Client-Server Architecture:** Clear separation between the client (the application making the request) and the server (the application providing the service).
- **Statelessness:** Each request from the client contains all the necessary information for the server to understand and process it.
- **Cacheability:** Responses can be cached to improve performance and reduce server load.
- **Layered System:** Multiple servers can act as intermediaries between the client and the final server.
- **Code on Demand (Optional):** The server can optionally transfer executable code to the client to extend functionality.

**Why REST APIs are Popular**

- **Simplicity:** Easy to understand and implement.
- **Flexibility:** Supports various data formats (JSON, XML).
- **Scalability:** Can handle a large number of requests.
- **Platform Independence:** Works across different platforms and programming languages.

By understanding the different types of APIs and the principles of REST, developers can effectively design and build robust, scalable, and user-friendly applications.

---

### **Understanding REST Principles**

REST principles are guidelines for building RESTful APIs:

1. **Client-Server Separation**: The client and server are independent. The server handles data and logic, while the client focuses on the user interface.
2. **Stateless Communication**: Each API call contains all the required information, and the server doesn’t store client context. A RESTful API being **stateless** means that the server does not store any information about the client between requests. Each request from a client to the server must contain all the information needed for the server to fulfill the request.

   **Key Points**:

   1. **No Session State**:

      - The server does not remember anything about the user or their previous requests.
      - Authentication and data required for processing must be included in every request (e.g., tokens, user IDs).

   2. **Independence of Requests**:

      - Each request is independent and self-contained.
      - For example, if you're accessing user data through a REST API, your request should include all necessary details (like an API key or token) without relying on previous interactions.

   3. **Scalability**:

      - Statelessness makes it easier to scale applications because any server can handle any request without needing to know the "history" of the client.

   4. **Consistency**:

      - Since the server doesn't rely on past interactions, it ensures consistent behavior regardless of which server in a distributed system handles the request.

   ##### Example of Stateless Behavior:

   ##### Request 1: Authenticate User

   ```http
   POST /login
   Content-Type: application/json

   {
   "username": "john_doe",
   "password": "password123"
   }
   ```

   Response:

   ```json
   {
     "token": "abcdef123456"
   }
   ```

   ##### Request 2: Fetch User Profile (Stateless)

   ```http
   GET /user/profile
   Authorization: Bearer abcdef123456
   ```

   Here, the server doesn't remember who "john_doe" is from the previous request. It uses the provided token to authenticate and process this request.

   This stateless nature is a core principle of REST and contrasts with stateful systems, where a server might rely on saved sessions or previous interactions to handle requests.

3. **Uniform Interface**: APIs should have a consistent structure for easy consumption:

   - Use clear and descriptive URLs.
   - Follow standard HTTP methods and status codes.

4. **Layered System**: APIs can be layered to improve scalability and modularity. For instance, a caching layer might sit between the client and server.
5. **Cacheability**: APIs should define whether responses are cacheable to optimize performance.
6. **Code on Demand (Optional)**: Servers can send executable code (e.g., JavaScript) to clients, enhancing functionality.

---

### **Introduction to Django REST Framework (DRF)**

Django REST Framework (DRF) is a powerful library for building RESTful APIs in Django. It simplifies API development with built-in tools for serialization, authentication, and views.

#### **Key Features of DRF**:

1. **Serialization**: Easily convert complex data types (like Django models) to JSON and vice versa.
2. **Class-Based Views**: Extendable views for handling CRUD operations (`ListAPIView`, `RetrieveAPIView`).
3. **Authentication and Permissions**: Built-in support for authentication methods (e.g., Token, JWT) and permission handling.
4. **Browsable API**: A user-friendly web interface to test and interact with APIs.
5. **Pagination**: Built-in support for paginating large datasets.

---

### **Setting Up DRF in a Django Project with Poetry**

Poetry is a modern dependency management and packaging tool for Python projects. Here's how to set up DRF in a Django project using Poetry:

#### **1. Create a Django Project Using Poetry**

1. **Install Poetry**:

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

2. **Create a New Project**:

- Navigate to your desired project directory in your terminal.
- Create a Folder that will contain your django project.Then,initialize a new Poetry project inside it:
  ```bash
  cd My_project_drf
  poetry init
  ```
  - Follow the prompts to provide basic information about your project.

3. **Add Django and DRF to Dependencies**:

   ```bash
   poetry add django djangorestframework
   ```

4. **Start a New Django Project**:

   ```bash
   poetry run django-admin startproject myproject .
   ```

   This create a virtual environment for your project.
   You can activate the environment by running command:

   ```bash
    poetry shell
   ```

5. **Apply Migrations**:

   ```bash
   poetry run python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   poetry run python manage.py runserver
   ```

---

#### **2. Configure Django REST Framework**

1. **Install DRF**:
   DRF is already added with `poetry add djangorestframework`.

2. **Add DRF to `INSTALLED_APPS`** in `settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
   ]
   ```

3. **Add Basic DRF Configuration (Optional)**:
   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.SessionAuthentication',
       ],
       'DEFAULT_PERMISSION_CLASSES': [
           'rest_framework.permissions.AllowAny',
       ],
   }
   ```

---

### **Create Your First DRF API**

---

#### **1. Create a New Django App**

1. **Create a Django App**:
   Run the following command to create a new app named `my_blog`:

   ```bash
   poetry run python manage.py startapp my_blog
   ```

2. **Register the App in `settings.py`**:
   Add the `blog` app to the `INSTALLED_APPS` list:
   ```python
   INSTALLED_APPS = [
       ...
       'my_blog',
   ]
   ```

---

#### **2. Create the Blog Model**

In `my_blog/models.py`, define the `Blog` model:

```python
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

---

#### **3. Apply Migrations**

1. **Make Migrations**:

   ```bash
   poetry run python manage.py makemigrations my_blog
   ```

2. **Apply Migrations**:
   ```bash
   poetry run python manage.py migrate
   ```

---

#### **4. Create the Blog Serializer**

In `my_blog/serializers.py`, create a serializer for the `Blog` model:

```python
from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
```

---

#### **5. Create Blog API Views**

In `my_blog/views.py`, define the API view for listing blogs:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

---

#### **6. Configure URLs**

In `blog/urls.py`, set up the endpoint:

```python
from django.urls import path
from .views import BlogListView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
]
```

Include the app’s URLs in the project’s `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
]
```

---

#### **7. Run the Development Server**

Start the server:

```bash
poetry run python manage.py runserver
```

---

#### **8. Test Your Blog API**

1. Open your browser or Postman and navigate to:
   ```
   http://127.0.0.1:8000/api/blogs/
   ```
   - **GET**: Fetch all blogs.
   - **POST**: Add a new blog (provide JSON data like below):
     ```json
     {
       "title": "Introduction to REST APIs",
       "content": "REST APIs are powerful for communication between systems.",
       "author": "John Doe"
     }
     ```

---

## B. Building Apis with DRF

Building APIs with Django Rest Framework (DRF) involves several key steps to ensure efficient data handling and interaction. Here's a breakdown of each component:

---

### 1. **Creating Serializers for Data Serialization**

In Django Rest Framework (DRF), a **serializer** is a powerful and flexible tool that helps convert complex data types, such as Django models, into JSON (or other content types) for use in APIs. It also enables deserialization, i.e., converting JSON or other data types back into Python objects to be used in the application.

### Key Functions of Serializers

1. **Serialization**: Converts Django model instances or other Python objects into JSON or other formats that can be easily sent over the internet.
2. **Deserialization**: Validates and converts incoming data (e.g., JSON) into Python data types or Django model instances.
3. **Validation**: Provides a way to enforce rules on input data during deserialization.

---

### Types of Serializers in DRF

#### 1. **`Serializer` Class**

- The base class for building custom serializers manually.
- Fields are defined explicitly, and you write custom logic for serialization and validation.

```python
from rest_framework import serializers

class MyCustomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value
```

#### 2. **`ModelSerializer` Class**

- A shortcut for creating serializers directly from Django models.
- Automatically generates fields based on the model, and can include custom fields or validation.

```python
from rest_framework import serializers
from myapp.models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'age']
```

---

### Example: Using Serializers

#### Serialization Example

```python
# Assume MyModel is defined as:
# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

# Assume we have a model instance
from myapp.models import MyModel
instance = MyModel.objects.first()

# Serialization Example
instance = MyModel.objects.create(name="Alice", age=25)
#Serialzie it
serializer = MyModelSerializer(instance)
print(serializer.data)

# Outputs JSON-like Python dictionary
# Output:
{'id': 1, 'name': 'Alice', 'age': 25}  # Assuming the instance ID is 1
```

#### Deserialization Example

```python
# Deserialization Example
data = {'name': 'John Doe', 'age': 30}
serializer = MyModelSerializer(data=data)

if serializer.is_valid():
    validated_data = serializer.validated_data
    # Output:{'name': 'John Doe', 'age': 30}
    print(validated_data)  # Output 2
else:
    print(serializer.errors)
    #i.e if age is missing
   """
    # Input data:
      data = {'name': 'John Doe'}
    # Output:
      {'age': ['This field is required.']}
   ""
```

---

### Advantages of Serializers

- Simplifies the process of creating RESTful APIs.
- Built-in validation and error handling.
- Flexibility to customize fields and behavior as needed.
- Easy integration with Django's ORM.

Serializers bridge the gap between complex Django models and simple, client-consumable formats like JSON, making them a core feature of Django Rest Framework.

#### More on Serializers:

1. **Customizing validation**:

   ```python
   def validate_field_name(self, value):
       if not value.isalnum():
           raise serializers.ValidationError("Field must be alphanumeric")
       return value
   ```

2. **Handling relationships** (e.g., nested or related objects):

   ```python
   class RelatedModelSerializer(serializers.ModelSerializer):
       class Meta:
           model = RelatedModel
           fields = '__all__'

   class MyModelSerializer(serializers.ModelSerializer):
       related_field = RelatedModelSerializer(many=True)

       class Meta:
           model = MyModel
           fields = '__all__'
   ```

---

### 2. **Creating API Views**

DRF supports two main types of views:

- **Function-Based Views (FBVs)**
- **Class-Based Views (CBVs)**

In Django Rest Framework (DRF), you can implement APIs using three main styles: **Function-Based Views (FBVs)**, **Class-Based Views (CBVs)**, and **Generic Class-Based Views (GCBVs)**. Below are examples of each type:

---

#### **1. Function-Based API Views**

FBVs are simple Python functions where you handle HTTP methods explicitly using conditions.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def contact_view(request):
    if request.method == 'GET':
        data = {"message": "GET method called"}
        return Response(data)
    elif request.method == 'POST':
        data = {"message": "POST method called", "data": request.data}
        return Response(data, status=status.HTTP_201_CREATED)
```

---

#### **2. Class-Based API Views (CBVs)**

CBVs are Python classes where you define methods for each HTTP verb.

#### Example: Standard `APIView`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ExampleAPIView(APIView):
    def get(self, request):
        data = {"message": "GET method called"}
        return Response(data)

    def post(self, request):
        data = {"message": "POST method called", "data": request.data}
        return Response(data, status=status.HTTP_201_CREATED)
```

#### Example: `ViewSet`

A `ViewSet` handles multiple HTTP methods for a resource. It’s useful for RESTful patterns.

```python
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class ExampleViewSet(ViewSet):
    def list(self, request):  # Handles GET for listing all resources
        data = {"message": "List of resources"}
        return Response(data)

    def create(self, request):  # Handles POST for creating a resource
        data = {"message": "Resource created", "data": request.data}
        return Response(data)

    def retrieve(self, request, pk=None):  # Handles GET for a single resource
        data = {"message": f"Details of resource {pk}"}
        return Response(data)
```

---

#### **3. Generic Class-Based Views (GCBVs)**

Generic API Views in DRF are pre-built views that provide a simple and consistent way to perform common operations on resources. They abstract away a lot of coding that developers would otherwise need to write for handling basic CRUD actions.

Here are some of the most commonly used Generic API Views:

**1. ListAPIView**

- **Purpose:** Retrieves a list of objects.
- **Example:**

```python
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

**2. RetrieveAPIView**

- **Purpose:** Retrieves a single object.
- **Example:**

```python
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'  # Use ISBN as the unique identifier
```

**3. CreateAPIView**

- **Purpose:** Creates a new object.
- **Example:**

```python
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

**4. UpdateAPIView**

- **Purpose:** Updates an existing object.
- **Example:**

```python
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'
```

**5. DestroyAPIView**

- **Purpose:** Deletes an existing object.
- **Example:**

```python
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'
```

**6. ListCreateAPIView**

- **Purpose:** Combines `ListAPIView` and `CreateAPIView` to handle both listing and creating objects in a single view.
- **Example:**

```python
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

**7. RetrieveUpdateDestroyAPIView**

- **Purpose:** Combines `RetrieveAPIView`, `UpdateAPIView`, and `DestroyAPIView` to handle retrieving, updating, and deleting a single object in a single view.
- **Example:**

```python
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'
```

#### **4.Viewsets**

Viewsets are a powerful tool in DRF that simplify API development by providing a higher-level abstraction for creating common API endpoints. They promote code organization, reusability, and maintainability while reducing boilerplate code.

**Key Viewset Classes:**

- **`ModelViewSet`:** This is the most commonly used Viewset. It provides all the standard HTTP methods (GET, POST, PUT, PATCH, DELETE) for a given model.
- **`ReadOnlyModelViewSet`:** Similar to `ModelViewSet`, but only allows GET and HEAD requests, making it suitable for read-only APIs.
- **`GenericViewSet`:** A base class for creating custom Viewsets. It doesn't provide any default actions, allowing you to define your own methods and behavior.

**Example:**

```python
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

In this example:

1. We import `viewsets` from `rest_framework`.
2. We define a `BookViewSet` class that inherits from `viewsets.ModelViewSet`.
3. We specify the `queryset` to be all instances of the `Book` model.
4. We define the `serializer_class` to be the `BookSerializer` we created for our model.

**Using Viewsets with Routers:**

- DRF's Routers are used to automatically generate URL patterns for Viewsets.
- **`DefaultRouter`:** The most common Router, it creates URL patterns for common actions (list, retrieve, create, etc.) using standard URL conventions.

```python
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

# Now, you can access the following URLs:
# - /books/ (GET: list all books, POST: create a new book)
# - /books/<pk>/ (GET: retrieve a single book, PUT/PATCH: update, DELETE: delete)
```

**Benefits of Using Viewsets:**

- **Reduced Boilerplate Code:** Significantly less code is required compared to defining individual views for each HTTP method.
- **Improved Code Reusability:** Viewsets can be easily reused across different parts of your API.
- **Enhanced Maintainability:** Changes to API behavior can be made in one place, making maintenance easier.

---

### **Key Differences:**

| Type      | Use Case                                                                                  |
| --------- | ----------------------------------------------------------------------------------------- |
| **FBVs**  | When you need simple logic and minimal abstraction.                                       |
| **CBVs**  | When you want to organize code into classes with methods for each HTTP verb.              |
| **GCBVs** | When you need CRUD operations quickly and want to minimize the code for repetitive tasks. |

Each style has its purpose, and you can mix them based on the complexity and requirements of your API.

---

### 3. **Authentication in APIs**

To implement a token-based authentication system in Django Rest Framework (DRF), you can follow these steps:

#### Step 1: Install Required Packages

First, you need to install `djangorestframework` and `djangorestframework-simplejwt`, which is a JWT-based authentication package for DRF.

```bash
pip install djangorestframework
pip install djangorestframework-simplejwt
```

#### Step 2: Configure Installed Apps

Add `rest_framework` and `rest_framework_simplejwt` to the `INSTALLED_APPS` in your Django project's `settings.py` file.

```python
INSTALLED_APPS = [
    # other apps
    'rest_framework',
    'rest_framework_simplejwt',
]
```

#### Step 3: Update Settings for Authentication

Next, configure DRF to use JWT tokens for authentication. In `settings.py`, add the following under `REST_FRAMEWORK`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

This ensures that JWT will be used for authentication and that the default permission will require the user to be authenticated.

#### Step 4: Create API Views for Authentication

To generate tokens, you'll use `SimpleJWT`'s built-in views. These views are provided by the package to handle the token creation and refreshing.

1. **Obtain Token**: The first view is to get an authentication token by providing valid user credentials (username and password).

2. **Refresh Token**: The second view will allow users to refresh their tokens when they expire.

In your `urls.py`, add the following:

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # other URL patterns
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

- `TokenObtainPairView`: This will handle the creation of JWT tokens by providing the user's credentials.
- `TokenRefreshView`: This will allow the user to refresh the token once it expires.

#### Step 5: Create a Custom User Serializer (Optional)

While the built-in views should work out of the box, you might want to customize how users are handled. For example, you might want to include a custom `UserSerializer`.

Create a `serializers.py` file if it doesn't exist already:

```python
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
```

#### Step 6: Add Views That Require Authentication

You can now create views that require token-based authentication. You can secure any view by using the `IsAuthenticated` permission.

For example, if you want to create a view to get user details:

```python
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
        })
```

Make sure this view is included in your `urls.py`:

```python
from django.urls import path
from .views import UserDetailView

urlpatterns = [
    # other URL patterns
    path('api/user/', UserDetailView.as_view(), name='user_detail'),
]
```

Now, only authenticated users (with a valid JWT token) will be able to access this view.

#### Step 7: Testing the Token Authentication

1. **Obtain Token**: To get a token, send a `POST` request to `/api/token/` with the user's credentials.

```bash
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

The response will contain the `access` and `refresh` tokens.

```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

2. **Use Token for Authentication**: To access the protected endpoint, send a `GET` request to `/api/user/` with the `Authorization` header set to `Bearer <your_access_token>`.

```bash
GET /api/user/
Authorization: Bearer your_access_token
```

3. **Refresh Token**: When the `access` token expires, you can refresh it by sending a `POST` request to `/api/token/refresh/` with the `refresh` token.

```bash
POST /api/token/refresh/
{
    "refresh": "your_refresh_token"
}
```

This will return a new `access` token.

#### Step 8: Handle Token Expiration and Access Control

Since the JWT tokens have an expiration time (by default 5 minutes for the access token and 1 day for the refresh token), you need to ensure the client application properly handles expired tokens by using the refresh token to obtain a new access token.

#### Optional: Customize Token Expiry and Other Settings

You can customize the expiration time of the access and refresh tokens by modifying the settings in `settings.py`:

```python
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Customize the access token expiry time
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # Customize the refresh token expiry time
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}
```

---

### 4. **Pagination, Filtering, and Searching in APIs**

#### a. Pagination

Pagination in Django Rest Framework (DRF) helps to limit the number of results returned in an API response, making it easier to handle large datasets such as blog entries. Here's how you can set up pagination for a Blog model in DRF:

**1. Define the Blog Model**:

Ensure you have a `Blog` model defined. For example:

```python
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="blog_posts"
    )
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name="blog_posts")
    tags = models.CharField(
        max_length=200, blank=True, help_text="Comma-separated tags"
    )
    thumbnail = models.ImageField(
        upload_to="uploads/blog_images/",
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse(
            "my_blog:blog_detail_view",
            kwargs={
                "slug": self.slug,
            },
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
```

**2. Create a Serializer for the Blog Model:**

The serializer converts the model instances into JSON:

```python
from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'created_at']
```

**3. Set Up Pagination:**

**Option A: Global Pagination**

To set pagination globally, update the `settings.py` file:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Number of items per page
}
```

This applies pagination to all views that use the DRF defaults.

**Option B: Custom Pagination Class**

You can create a custom pagination class if you need more control:

In myapp/pagination.py

```python
from rest_framework.pagination import PageNumberPagination

class BlogPagination(PageNumberPagination):
    page_size = 5  # Items per page
    page_size_query_param = 'page_size'  # Allow clients to override
    max_page_size = 100  # Maximum items per page
```

**4. Create a Blog View:**

##### Using `GenericAPIView`

```python
from rest_framework.generics import ListAPIView
from .models import Blog
from .serializers import BlogSerializer
from .pagination import BlogPagination  # Import if using custom pagination

class BlogListView(ListAPIView):
    queryset = Blog.objects.all().order_by('-date_created')
    serializer_class = BlogSerializer
    pagination_class = BlogPagination  # Use this if using custom pagination
```

##### Using `APIView`

```python
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Blog
from .serializers import BlogSerializer

class BlogListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Blog.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Items per page
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
```

**5. Add the URL for the View:**

In your `urls.py`:

```python
from django.urls import path
from .views import BlogListView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
]
```

**6. Test the API:**

Start your server and test the endpoint `/blogs/`. By default:

- You’ll get the first page of results.
- You can navigate pages using the `page` query parameter (e.g., `/blogs/?page=2`).

If you're using custom pagination with a `page_size_query_param`, you can also control the page size dynamically (e.g., `/blogs/?page=2&page_size=20`).

This approach keeps your API efficient and user-friendly!

#### b. Filtering

For filtering, we can use `django-filter`, a powerful library in Django that integrates seamlessly with Django Rest Framework (DRF) to provide advanced filtering capabilities for your API views. It allows developers to filter querysets dynamically based on query parameters provided in API requests.

**Key Features of `django-filter`**

- Integration with DRF: Works out of the box with DRF's generic views and viewsets.
- Declarative Filtering: Allows you to declare filters in a class-based structure, similar to Django forms or serializers.
- Support for Complex Lookups: Provides filtering for common lookups like exact, contains, startswith, lte, gte, etc.
- Custom Filters: You can create custom filtering logic to handle special cases.
- Automatic Parameter Validation: Ensures the filter parameters are valid, reducing errors.

**Some common filters provided by `django-filter`**

- `CharFilter`: Filters based on string fields.
- `NumberFilter`: Filters based on numeric fields.
- `BooleanFilter`: Filters based on boolean fields.
- `DateFilter` / `DateTimeFilter`: Filters based on date or datetime fields.
- `RangeFilter`: Filters within a range (e.g., price range).
- `MultipleChoiceFilter`: Filters based on multiple values (e.g., a list of categories).

**Steps to Filter with django-filter**

1. **Install `django-filter`**:

   ```bash
   pip install django-filter
   ```

2. **Update `settings.py`**:

   ```python
   INSTALLED_APPS=[
    ...
    "django_filters",
   ]

   REST_FRAMEWORK = {
       'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
   }
   ```

3. **Define Model**:

   ```python
    from django.db import models
    from django.contrib.auth.models import User
    from django.utils.text import slugify
    from django.urls import reverse


    class Category(models.Model):
        name = models.CharField(max_length=100, unique=True)
        slug = models.SlugField(max_length=100, unique=True, blank=True)

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)
            super().save(*args, **kwargs)

        def __str__(self):
            return self.name


    class Product(models.Model):
        name = models.CharField(max_length=200)
        slug = models.SlugField(unique=True)
        description = models.TextField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        stock = models.PositiveIntegerField()
        available = models.BooleanField(default=True)
        category = models.ForeignKey(
            Category, related_name="products", on_delete=models.CASCADE
        )
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name
   ```

4. **Define Filter**:
   Create a FilterSet class for your model. This class defines the fields you want to filter on and the types of filters.

   ```python
    from django_filters import rest_framework as filters
    from .models import Product


    class ProductFilter(filters.FilterSet):
        price = filters.RangeFilter()  # Allows filtering by a price range
        name = filters.CharFilter(
            lookup_expr="icontains"
        )  # Case-insensitive search for product name
        category = filters.CharFilter(
            field_name="category__name", lookup_expr="icontains"
        )  # Category name filter

        class Meta:
            model = Product
            fields = ["price", "name", "category"]
   ```

5. **Integrate the FilterSet in Your View**:

   ```python
   from rest_framework import generics
   from django_filters.rest_framework import DjangoFilterBackend
   from .models import Product
   from .serializers import ProductSerializer
   from .filters import ProductFilter

   class ProductListView(generics.ListAPIView):
       queryset = Product.objects.all()
       serializer_class = ProductSerializer
       filter_backends = [DjangoFilterBackend]
       filterset_class = ProductFilter
   ```

6. **Configure url for the FilterSet View**:

   In myapp/urls.py

   ```python
   from django.urls import path
   from .views import ProductListView

   urlpatterns = [
       path('products/', ProductListView.as_view(), name='product-list'),
   ]
   ```

   In project/urls.py

   ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('myapp.urls')),  # Replace 'myapp' with your app's name
    ]

   ```

#### c. Searching

### SearchFilter in Django REST Framework

The `SearchFilter` is a powerful filtering backend provided by Django REST Framework (DRF) that allows users to perform search operations on API endpoints. It enables filtering of querysets based on specific query parameters passed by the client.

---

#### How It Works

The `SearchFilter` looks for a query parameter (by default, `search`) in the URL, and filters the queryset based on the specified fields. These fields are defined in the `search_fields` attribute of the view or viewset.

---

#### Steps to Use SearchFilter

1. **Import the SearchFilter**  
   Import `SearchFilter` from `rest_framework.filters`.

2. **Add SearchFilter to the View or ViewSet**  
   Specify the filter backend and define the fields to be searched.

3. **Configure search fields**  
   Use the `search_fields` attribute to define which model fields should be searched.

---

#### Example

```python
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from myapp.models import Product
from myapp.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'category__name']

# Example URL:
# GET /products/?search=laptop
```

In this example:

- The `ProductViewSet` is configured with `SearchFilter`.
- The `search_fields` specify that the API should search in the `name`, `description`, and the related `category` model's `name` field.
- A search query like `/products/?search=laptop` will return all products whose `name`, `description`, or related category name contains the word "laptop".

---

#### Using Complex Lookups

You can also use advanced search configurations:

- `@` for full-text search (PostgreSQL).
- `=` for exact match.
- `^` for starts-with queries.

For example:

```python
search_fields = ['^name', '=category__name', '@description']
```

- `^name` searches for products whose `name` starts with the query.
- `=category__name` matches the exact category name.
- `@description` uses full-text search (requires PostgreSQL).

---

#### Customizing the Search Parameter

By default, `SearchFilter` uses `search` as the query parameter. To customize it, override the `SEARCH_PARAM` setting in your Django settings file:

```python
# settings.py
REST_FRAMEWORK = {
    'SEARCH_PARAM': 'q',  # Custom search parameter
}
```

Now, the client can use `/products/?q=laptop` instead of `/products/?search=laptop`.

---

#### Advantages of SearchFilter

1. **Easy to Implement**: Requires minimal configuration.
2. **Flexible**: Supports searching across multiple fields.
3. **Optimized**: Works seamlessly with Django ORM, including related fields.

---

#### Limitations

1. **Performance**: Searching across large datasets may be slow if fields are not indexed.
2. **Limited Customization**: For complex search logic, you may need to use a custom filter backend.

---

#### Tips for Optimizing SearchFilter

1. **Database Indexing**: Ensure fields in `search_fields` are indexed for better performance.
2. **Pagination**: Use pagination to limit the number of results returned.
3. **Custom Filters**: For complex queries, write a custom filter backend.

---

## C. Advanced API Development

### 1. **Implementing CRUD Operations in APIs**

CRUD refers to the fundamental operations of persistent storage—Create, Read, Update, and Delete. In DRF, these are implemented using serializers, views, and routers.

#### Example: CRUD with a Model `Book`

**Model Definition**

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

**Serializer**

```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

**Views**

- **Class-Based Views (CBVs):**

```python
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

- **Viewsets and Routers:**

```python
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

```python
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
```

---

### 2. **Versioning and Throttling APIs**

#### **a. Versioning**

Versioning in Django REST Framework (DRF) is a way to manage changes in your API over time, ensuring backward compatibility while introducing new features or updates. It allows clients to specify which version of the API they want to interact with.

As your application evolves, you might need to introduce changes to your API endpoints, request/response structures, or data representations. However, existing clients might depend on the current API structure. Versioning helps maintain a balance between introducing new features and supporting existing clients.

**Types of Versioning**

1. **URL Path Versioning**:

URL path versioning is a common approach in Django Rest Framework (DRF) to handle API versioning. It involves including the version number in the URL path, allowing clients to specify which version of the API they want to use. Here's how you can implement it:

---

**Steps for URL Path Versioning in DRF**

1. **Set Up the DRF Project**
   Ensure you have a DRF project set up. If not, you can start with:

   ```bash
   pip install djangorestframework
   ```

2. **Define Versioned URLs**
   Include the version number as part of the URL path. For example:

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('v1/resource/', views.ResourceViewV1.as_view(), name='resource_v1'),
       path('v2/resource/', views.ResourceViewV2.as_view(), name='resource_v2'),
   ]
   ```

3. **Create Version-Specific Views**
   Create separate views for different API versions. For example:

   ```python
   from rest_framework.views import APIView
   from rest_framework.response import Response

   class ResourceViewV1(APIView):
       def get(self, request):
           return Response({"message": "This is version 1 of the API."})

   class ResourceViewV2(APIView):
       def get(self, request):
           return Response({"message": "This is version 2 of the API."})
   ```

4. **Optional: Use a Versioning Scheme**
   DRF provides built-in support for versioning schemes. You can enable `URLPathVersioning` in your settings:

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
       'DEFAULT_VERSION': 'v1',
       'ALLOWED_VERSIONS': ['v1', 'v2'],
   }
   ```

   Update your URLs to reflect the version placeholder:

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('<str:version>/resource/', views.ResourceView.as_view(), name='resource'),
   ]
   ```

   Modify the view to handle versions dynamically:

   ```python
   class ResourceView(APIView):
       def get(self, request, version):
           if version == 'v1':
               return Response({"message": "This is version 1 of the API."})
           elif version == 'v2':
               return Response({"message": "This is version 2 of the API."})
           else:
               return Response({"error": "Unsupported API version."}, status=400)
   ```

5. **Test Your API**
   Test the different versions of your API by accessing URLs like:
   - `http://localhost:8000/v1/resource/`
   - `http://localhost:8000/v2/resource/`

---

##### **Advantages of URL Path Versioning**

- **Clarity**: Version is explicitly visible in the URL.
- **Cache-Friendly**: Easier to manage caching and CDN configurations per version.
- **Backward Compatibility**: Allows clients to continue using older versions while new features are added in updated versions.

##### **Considerations**

- Avoid proliferating versions unnecessarily. Deprecate old versions when no longer needed.
- Ensure proper documentation for each version to guide API consumers.

---

2. **Query Parameter Versioning**:

Query parameter versioning is another approach to versioning APIs in Django Rest Framework (DRF). Instead of specifying the version in the URL path, the version is passed as a query parameter. For example:  
`http://localhost:8000/resource/?version=v1`

**Implement Query Parameter Versioning**

1. **Set Up DRF for Query Parameter Versioning**
   Enable query parameter versioning in your DRF settings:

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
       'DEFAULT_VERSION': 'v1',  # The default version to use if none is provided
       'ALLOWED_VERSIONS': ['v1', 'v2'],  # Specify supported versions
       'VERSION_PARAM': 'version',  # The query parameter name (default is "version")
   }
   ```

2. **Modify the Views**
   Use the `request.version` attribute to handle version-specific logic in your views:

   ```python
   from rest_framework.views import APIView
   from rest_framework.response import Response

   class ResourceView(APIView):
       def get(self, request):
           if request.version == 'v1':
               return Response({"message": "This is version 1 of the API."})
           elif request.version == 'v2':
               return Response({"message": "This is version 2 of the API."})
           else:
               return Response({"error": "Unsupported API version."}, status=400)
   ```

3. **Define the URLs**
   Create a single route without including the version in the URL path:

   ```python
   from django.urls import path
   from .views import ResourceView

   urlpatterns = [
       path('resource/', ResourceView.as_view(), name='resource'),
   ]
   ```

4. **Test Your API**
   Use query parameters to access different versions of the API:
   - `http://localhost:8000/resource/?version=v1`
   - `http://localhost:8000/resource/?version=v2`

---

**Advantages of Query Parameter Versioning**

1. **Non-Intrusive URLs**: Keeps URLs clean without embedding version information in the path.
2. **Flexibility**: Allows clients to switch versions dynamically by changing the query parameter value.
3. **Backward Compatibility**: Similar to path versioning, older versions remain accessible.

---

**Considerations**

1. **Visibility**: Query parameters might not be as visible or intuitive to API consumers as path-based versioning.
2. **Caching**: May require careful cache configuration since different versions share the same path.
3. **Validation**: Ensure strict validation for allowed versions to prevent misuse of the API.

---

**Which to Choose: Path vs. Query Parameter Versioning?**

- **Path Versioning**: Better for APIs with a long lifecycle or public-facing APIs, as it's more explicit.
- **Query Parameter Versioning**: Ideal for internal APIs or APIs with fewer consumers, where simplicity is preferred.

---

3. **Host Name Versioning**:
   **host name versioning** is a technique to differentiate versions of your API based on the hostname of the request. This approach allows you to serve different versions of your API from different hostnames or subdomains, such as:

- `api.v1.example.com` for version 1
- `api.v2.example.com` for version 2

This is useful when you want to provide versioning without relying on URL paths (`/v1/resource`) or query parameters (`?version=1`).

**Steps to Implement Host Name Versioning in DRF**

1. **Enable Versioning in DRF**:
   Set up DRF to use a custom versioning scheme based on the hostname.

2. **Define a Custom Versioning Class**:
   Create a custom versioning class that extracts the version from the hostname.

3. **Update Settings**:
   Configure DRF to use the custom versioning class.

---

**1. Create a Custom Versioning Class**

Create a file, e.g., `versioning.py` in your app:

```python
from rest_framework.versioning import BaseVersioning
from django.core.exceptions import NotFound

class HostNameVersioning(BaseVersioning):
    def determine_version(self, request, *args, **kwargs):
        # Extract the hostname from the request
        host = request.get_host()

        # Define mapping of hostnames to versions
        version_map = {
            'api.v1.example.com': 'v1',
            'api.v2.example.com': 'v2',
        }

        # Get the version based on the hostname
        version = version_map.get(host)

        if not version:
            raise NotFound(f"API version not found for host: {host}")

        return version
```

**2. Update DRF Settings**

In your `settings.py`, specify the versioning scheme:

```python
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'myapp.versioning.HostNameVersioning',
    'DEFAULT_VERSION': 'v1',  # Optional: default version
    'ALLOWED_VERSIONS': ['v1', 'v2'],  # Optional: list of allowed versions
}
```

**3. Version-Specific Views**

You can handle version-specific behavior in your views:

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class ExampleView(APIView):
    def get(self, request, *args, **kwargs):
        version = request.version  # Extract version from the request
        if version == 'v1':
            return Response({'message': 'This is version 1 of the API'})
        elif version == 'v2':
            return Response({'message': 'This is version 2 of the API'})
        return Response({'message': 'Unknown version'}, status=400)
```

**4. Routing and Host Configuration**

Configure your DNS or reverse proxy (e.g., Nginx) to route requests to the appropriate hostname. For example:

- `api.v1.example.com` points to the DRF app.
- `api.v2.example.com` points to the same app but processes requests differently based on the version extracted from the hostname.

---

**Advantages of Host Name Versioning**

1. **Clear Separation**: Each version has a dedicated hostname, making it easy to manage.
2. **Backward Compatibility**: Older clients can continue to use the older version hostname.
3. **No URL Changes**: Avoids cluttering URLs with version information.

---

4. **Header Versioning**:

   - The version is specified in the request headers.
   - Example: `Version: 1.0`.

   ```python
   # settings.py
   REST_FRAMEWORK = {
       'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.HeaderVersioning',
   }
   ```

   ```http
   GET /resource/ HTTP/1.1
   Version: 1.0
   ```

**Implementing Versioning**

1. **Set Default Versioning**:
   Define the default versioning strategy in your `settings.py`.

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
       'DEFAULT_VERSION': '1.0',  # Default version if none is specified
   }
   ```

2. **Accessing Version in Views**:
   Use the `request.version` attribute in your views to handle version-specific logic.

   ```python
   from rest_framework.response import Response
   from rest_framework.views import APIView

   class ExampleView(APIView):
       def get(self, request, *args, **kwargs):
           if request.version == '1.0':
               data = {"message": "Response for version 1.0"}
           elif request.version == '2.0':
               data = {"message": "Response for version 2.0"}
           else:
               data = {"message": "Default version response"}
           return Response(data)
   ```

3. **Custom Versioning**:
   You can define your own versioning class by extending `BaseVersioning`.

   ```python
   from rest_framework.versioning import BaseVersioning

   class CustomVersioning(BaseVersioning):
       def determine_version(self, request, *args, **kwargs):
           return request.headers.get('X-Custom-Version', '1.0')
   ```

   ```python
   # settings.py
   REST_FRAMEWORK = {
       'DEFAULT_VERSIONING_CLASS': 'path.to.CustomVersioning',
   }
   ```

---

**Best Practices**

- **Deprecate Old Versions Gradually**: Provide a clear deprecation policy for older versions.
- **Documentation**: Clearly document the available API versions and their differences.
- **Testing**: Test each version independently to avoid breaking changes.
- **Consistency**: Use the same versioning scheme across all endpoints.

By using versioning in DRF, you can maintain a scalable and flexible API while accommodating future changes effectively.

#### **b. Throttling**

Throttling in Django Rest Framework (DRF) is a mechanism to control the rate of requests that a client can make to an API. This is useful to prevent abuse, ensure fair usage, and optimize server performance.

**Steps to Implement Throttling in DRF:**

1. **Understand DRF's Throttling Classes**:
   DRF provides built-in throttling classes:

   - **`AnonRateThrottle`**: Limits the rate of requests for anonymous users.
   - **`UserRateThrottle`**: Limits the rate of requests for authenticated users.
   - **Custom Throttle Classes**: Allows you to define custom throttling logic.

2. **Enable Throttling in DRF Settings**:
   Add or update the `DEFAULT_THROTTLE_CLASSES` and `DEFAULT_THROTTLE_RATES` settings in the `settings.py` file:

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_THROTTLE_CLASSES': [
           'rest_framework.throttling.AnonRateThrottle',
           'rest_framework.throttling.UserRateThrottle',
       ],
       'DEFAULT_THROTTLE_RATES': {
           'anon': '5/min',  # 5 requests per minute for anonymous users
           'user': '10/min',  # 10 requests per minute for authenticated users
       }
   }
   ```

3. **Apply Throttling to Specific Views**:
   Throttling can be applied globally (using the settings above) or on specific views using the `throttle_classes` attribute.

   Example:

   ```python
   from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
   from rest_framework.views import APIView
   from rest_framework.response import Response

   class ExampleView(APIView):
       throttle_classes = [AnonRateThrottle, UserRateThrottle]

       def get(self, request, *args, **kwargs):
           return Response({"message": "This is a throttled view!"})
   ```

4. **Customize Throttle Rates**:
   You can define custom throttle rates by subclassing one of DRF's throttling classes:

   ```python
   from rest_framework.throttling import UserRateThrottle

   class BurstRateThrottle(UserRateThrottle):
       rate = '20/min'

   class SustainedRateThrottle(UserRateThrottle):
       rate = '100/day'
   ```

   Then, use these custom throttle classes in your views:

   ```python
   class CustomThrottleView(APIView):
       throttle_classes = [BurstRateThrottle, SustainedRateThrottle]

       def get(self, request, *args, **kwargs):
           return Response({"message": "Custom throttling applied!"})
   ```

5. **Override Throttle Behavior** (Optional):
   To create a fully custom throttle logic, subclass `BaseThrottle` and override its `allow_request` and `wait` methods:

   ```python
   from rest_framework.throttling import BaseThrottle

   class CustomThrottle(BaseThrottle):
       def allow_request(self, request, view):
           # Custom logic to allow or deny the request
           return True  # Example: Always allow

       def wait(self):
           # Return the number of seconds to wait before the next request
           return None
   ```

6. **Testing Throttling**:
   Test the implementation by making requests to your API and ensuring that requests exceeding the allowed rate return a `429 Too Many Requests` response.

   Example Response:

   ```json
   {
     "detail": "Request was throttled. Expected available in 10 seconds."
   }
   ```

**Summary of Key Points:**

- Use `AnonRateThrottle` for anonymous users and `UserRateThrottle` for authenticated users.
- Configure rates in `DEFAULT_THROTTLE_RATES`.
- Apply throttling globally or at the view level.
- Extend or override throttling classes for custom behavior.

By following these steps, you can efficiently manage API usage and protect your system from misuse.

**Custom Throttle Classes:**

```python
from rest_framework.throttling import SimpleRateThrottle

class CustomRateThrottle(SimpleRateThrottle):
    scope = 'custom'
    rate = '5/min'
```

---

### 3. **Deploying REST APIs with Django**

#### a. Configure deployment settings:

---

**1. Set `DEBUG` to `False`**
In `settings.py`:

```python
DEBUG = False
```

> **Why?** In production, `DEBUG` must be disabled to prevent sensitive information from being displayed in error pages.

---

**2. Configure `ALLOWED_HOSTS`**
Add the hostnames or IP addresses of your server:

```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', '127.0.0.1']
```

> **Why?** This prevents HTTP Host header attacks.

---

**3. Use a Secure `SECRET_KEY`**

Generate a secure `SECRET_KEY` and keep it hidden. Do not hardcode it into `settings.py`. Instead, load it from environment variables:

```python
import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-secret-key')
```

Store the secret key securely (e.g., using `.env` files or cloud secrets management tools).

---

**4. Set Up Database Configuration**

For production, use a database like PostgreSQL. Example using `dj-database-url`:

Install the package:

```bash
pip install dj-database-url psycopg2-binary
```

Update `settings.py`:

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='postgres://user:password@localhost:5432/dbname')
}
```

> **Why?** SQLite is not suitable for production due to concurrency issues.

---

**5. Configure Static and Media Files**

Set up static files for production using `whitenoise` or a CDN.

Install `whitenoise`:

```bash
pip install whitenoise
```

Update `MIDDLEWARE` and settings:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Other middlewares...
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Whitenoise settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Run the `collectstatic` command during deployment:

```bash
python manage.py collectstatic
```

> **Why?** This ensures static files are served efficiently.

---

**6. Set Up Secure Headers**

Enable HTTPS and security headers in production:

```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

> **Why?** This protects against various security vulnerabilities.

---

**7. Configure Logging**

Set up logging for monitoring errors:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'error.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

> **Why?** Logs are essential for debugging and monitoring.

---

**8. Use Environment Variables**

Avoid hardcoding sensitive data in your code. Use a library like `python-decouple` or `.env` files.

Install:

```bash
pip install python-decouple
```

Create a `.env` file:

```
DJANGO_SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

Update `settings.py`:

```python
from decouple import config

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}
```

---

**9. Set Up Gunicorn/WSGI Server**

Use a WSGI server like Gunicorn to serve your Django app.

Install:

```bash
pip install gunicorn
```

Run:

```bash
gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000
```

---

**10. Use a Reverse Proxy (Nginx)**

Configure Nginx to proxy requests to Gunicorn and handle static/media files.

---

**11. Enable Caching**

Use caching for better performance. For example, with Redis:

Install:

```bash
pip install django-redis
```

Configure:

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}
```

---

**12. Monitor and Scale**

- Use monitoring tools like Sentry or New Relic.
- Use a load balancer for scaling.

---

#### b. Deploy DRF project to a specific platform:

1. **Prepare the Project for Production:**

   - Set up production settings (e.g., `DEBUG=False`, `ALLOWED_HOSTS`, `DATABASES`).
   - Use `gunicorn` or `uwsgi` as the WSGI server.

2. **Serve Static Files:**

   ```bash
   python manage.py collectstatic
   ```

3. **Deploy Using Gunicorn and Nginx:**

   - Install `gunicorn`: `pip install gunicorn`.
   - Configure Nginx to proxy requests to Gunicorn.

4. **Deploy to a Cloud Platform:**
   - Use platforms like AWS, Heroku, or DigitalOcean.
   - Example with Heroku:
     ```bash
     heroku create
     git push heroku main
     ```
