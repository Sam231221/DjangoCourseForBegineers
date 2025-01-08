## **A. Introduction to REST APIs**

REST (Representational State Transfer) is an architectural style for designing networked applications. REST APIs allow communication between different software systems by using HTTP methods and stateless interactions. They are widely used because they are simple, scalable, and flexible.

**Key Concepts of REST APIs:**

1. **Resources**: In REST, everything is treated as a resource, such as a user, product, or order. Each resource is identified by a unique URL (e.g., `/api/users/1`).
2. **HTTP Methods**:
   - `GET`: Retrieve data from the server.
   - `POST`: Create a new resource.
   - `PUT`/`PATCH`: Update an existing resource.
   - `DELETE`: Remove a resource.
3. **Statelessness**: Each request from a client to the server must contain all the information the server needs to fulfill the request.
4. **JSON/XML**: REST APIs commonly use JSON for data exchange, but XML can also be used.
5. **Status Codes**: Standard HTTP status codes indicate the outcome of a request (e.g., `200 OK`, `404 Not Found`).

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
       'DEFAULT_RENDERER_CLASSES': [
           'rest_framework.renderers.JSONRenderer',
           'rest_framework.renderers.BrowsableAPIRenderer',
       ],
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

#### Function-Based Views

FBVs provide explicit handling of HTTP methods:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def blog_listing_view(request):
    if request.method == 'GET':
        data = {"message": "GET request received"}
        return Response(data)
    elif request.method == 'POST':
        return Response({"message": "POST request received"})
```

#### Class-Based Views

CBVs use DRF's generic views for more structured handling:

```python
from rest_framework.views import APIView

class MyAPIView(APIView):
    def get(self, request):
        return Response({"message": "GET request received"})

    def post(self, request):
        return Response({"message": "POST request received"})
```

#### Using Generic Views

To avoid repetitive code, use DRF's mixins or `GenericAPIView`:

```python
from rest_framework.generics import ListCreateAPIView
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListCreateView(ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

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
