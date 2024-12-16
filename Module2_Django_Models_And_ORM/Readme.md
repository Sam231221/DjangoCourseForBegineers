## Module 2: Django Models and ORM (Object Relational Mapping)

### Introduction to Django Models

#### Defining Models and Fields

Django models represent the structure of your database, defining the data schema for your application. Models are Python classes that map to database tables. Each attribute in a model represents a database field.

Example:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

#### Using Django’s ORM to Interact with Databases

Django’s ORM allows developers to interact with the database without writing SQL queries. It provides Python methods to perform operations such as creating, retrieving, updating, and deleting records.

Example:

- **Create:** `Product.objects.create(name="Laptop", price=1000.00)`
- **Retrieve:** `Product.objects.all()`
- **Update:** `product = Product.objects.get(id=1); product.price = 900; product.save()`
- **Delete:** `product.delete()`

#### Creating and Applying Migrations

Migrations are Django’s way of propagating model changes to the database schema.

1. **Create Migration:** `python manage.py makemigrations`
2. **Apply Migration:** `python manage.py migrate`
3. **View Migrations:** `python manage.py showmigrations`

#### Querying Data from the Database (CRUD Operations)

- **Create:** `Product.objects.create(name="Smartphone", price=700.00)`
- **Read:**
  - Retrieve all: `Product.objects.all()`
  - Retrieve specific: `Product.objects.get(id=1)`
- **Update:**
  ```python
  product = Product.objects.get(id=1)
  product.price = 800
  product.save()
  ```
- **Delete:**
  ```python
  product = Product.objects.get(id=1)
  product.delete()
  ```

#### Relationships in Models (One-to-One, One-to-Many, Many-to-Many)

- **One-to-One Relationship:**
  ```python
  class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      bio = models.TextField()
  ```
- **One-to-Many Relationship:**

  ```python
  class Category(models.Model):
      name = models.CharField(max_length=100)

  class Product(models.Model):
      category = models.ForeignKey(Category, on_delete=models.CASCADE)
      name = models.CharField(max_length=100)
  ```

- **Many-to-Many Relationship:**

  ```python
  class Author(models.Model):
      name = models.CharField(max_length=100)

  class Book(models.Model):
      title = models.CharField(max_length=200)
      authors = models.ManyToManyField(Author)
  ```

### Django ORM Advanced

#### Filters, Exclude, and Aggregations

- **Filters:** Narrow down the QuerySet.
  ```python
  products = Product.objects.filter(price__gte=500)
  ```
- **Exclude:** Exclude specific records.
  ```python
  products = Product.objects.exclude(name="Smartphone")
  ```
- **Aggregations:** Perform calculations on data.
  ```python
  from django.db.models import Avg
  avg_price = Product.objects.aggregate(Avg('price'))
  ```

#### Advanced Lookups and Complex Queries

Lookups are defined using `__` (doubleunderscore).

#### Some lookups:

```python
 __    -> double slash activates lookup
 __lte -> Less than or equal
 __gte -> Greater than or equal
 __lt  -> Less than
 __gt  -> Greater than

```

They’re specified as keyword arguments to the [\*\*`QuerySet`](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet)** methods [**`filter()`**](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.filter), [**`exclude()`**](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude)
 and [**`get()`\*\*](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.get).

```python
from datetime import date

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

		def __str__(self):
			return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

		def __str__(self):
			return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

		def __str__(self):
			return self.headline
```

Syntax: **field\_\_lookuptype=value**

```jsx
Entry.objects.filter((pub_date__lte = "2006-01-01"));
```

translates (roughly) into the following SQL:

```jsx
**SELECT** * **FROM** blog_entry **WHERE** pub_date <= '2006-01-01';
```

### ForeignKey attribute lookup

The field specified in a lookup has to be the name of a model field. There’s one exception though, in case of a [**`ForeignKey`**](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey) you can specify the field name suffixed with **`_id`**. In this case, the value parameter is expected to contain the raw value of the foreign model’s primary key.

For example:

```python
**>>>** Entry.objects.filter(blog_id=4)
```

If you pass an invalid keyword argument, a lookup function will raise **`TypeError`**.

The database API supports about two dozen lookup types; a complete reference can be found in the [field lookup reference](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups).

#### Here’s some of the more common lookups you’ll probably use:

[\*\*`exact`](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#std:fieldlookup-exact) :\*\* An “exact” match

For example:

```python
**>>>** Entry.objects.get(headline__exact="Cat bites dog")
```

[\*\*`iexact`](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#std:fieldlookup-iexact) :\*\* A case-insensitive match. So, the query:

```python
**>>>** Blog.objects.get(name__iexact="beatles blog")
'''
Would match a **`Blog`** titled **`"Beatles Blog"`**, **`"beatles blog"`**, or even **`"BeAtlES blOG"`**.
'''
```

[\*\*`contains`](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#std:fieldlookup-contains) :\*\* Case-sensitive containment test.

For example:

```python
Entry.objects.get(headline__contains='Lennon')
```

For example:

```python
Entry.objects.get(headline__contains='Lennon')
```

### **Chaining filters[¶](https://docs.djangoproject.com/en/4.0/topics/db/queries/#chaining-filters-1)**

The result of refining a [**`QuerySet`**](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet) is itself a [**`QuerySet`**](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet), so it’s possible to chain refinements together. For example:

```jsx
**>>>** Entry.objects.filter(
**...**     headline__startswith='What'
**...** ).exclude(
**...**     pub_date__gte=datetime.date.today()
**...** ).filter(
**...**     pub_date__gte=datetime.date(2005, 1, 30)
**...** )
```

**QuerySets are lazy**
The act of creating a QuerySet doesn’t involve any database activity.
You can stack filters together all day long, and Django won’t actually run the query
until the QuerySet is evaluated. Take a look at this example:

```
>>> q = Entry.objects.filter(headline__startswith="What")
>>> q = q.filter(pub_date__lte=datetime.date.today())
>>> q = q.exclude(body_text__icontains="food")
>>> print(q)
```

Though this looks like three database hits, in fact it hits the database only once, at
the last line (print(q)). In general, the results of a QuerySet aren’t fetched from the
database until you “ask” for them. When you do, the QuerySet is evaluated by accessing
the database. For more details on exactly when evaluation takes place, see When
QuerySets are evaluated.

**`gt` : G**reater than.

Example:

```python
Entry.objects.filter(id__gt=4)
```

**`gte` :**Greater than or equal to.

**`lt` :** Less than.

**`lte`:** Less than or equal to.

**`startswith` :**Case-sensitive starts-with.

Example:

```python
Entry.objects.filter(headline__startswith='Lennon')
```

SQL equivalent:

**`SELECT** ... **WHERE** headline **LIKE** 'Lennon%';`

> **SQLite doesn’t support case-sensitive `LIKE` statements; `startswith` acts like `istartswith` for SQLite.**

**`istartswith` :** Case-insensitive starts-with.

Example:

```python
Entry.objects.filter(headline__istartswith='Lennon')
```

SQL equivalent:

**`SELECT** ... **WHERE** headline **ILIKE** 'Lennon%';`

**`endswith` :** Case-sensitive ends-with.

Example:

```python
Entry.objects.filter(headline__endswith='Lennon')
```

SQL equivalent:

**`SELECT** ... **WHERE** headline **LIKE** '%Lennon';`

**SQLite users**

SQLite doesn’t support case-sensitive **`LIKE`** statements; **`endswith`** acts like **`iendswith`** for SQLite. Refer to the [database note](https://docs.djangoproject.com/en/4.0/ref/databases/#sqlite-string-matching) documentation for more.

### **`iendswith`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#iendswith)**

Case-insensitive ends-with.

Example:

`Entry.objects.filter(headline__iendswith='Lennon')`

SQL equivalent:

**`SELECT** ... **WHERE** headline **ILIKE** '%Lennon'`

**SQLite users**

When using the SQLite backend and non-ASCII strings, bear in mind the [database note](https://docs.djangoproject.com/en/4.0/ref/databases/#sqlite-string-matching) about string comparisons.

### **`range`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#range)**

Range test (inclusive).

Example:

```python
import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
Entry.objects.filter(pub_date__range=(start_date, end_date))
```

<aside>
💡 You can use `range` anywhere you can use `BETWEEN` in SQL — for dates, numbers and even characters.
</aside>

### **`date` :**

For datetime fields, casts the value as date. Allows chaining additional field lookups. Takes a date value.

Example:

```python
Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))
```

(No equivalent SQL code fragment is included for this lookup because implementation of the relevant query varies among different database engines.)

When [**`USE_TZ`**](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-USE_TZ) is **`True`**, fields are converted to the current time zone before filtering. This requires [time zone definitions in the database](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#database-time-zone-definitions).

### **`year`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#year)**

For date and datetime fields, an exact year match. Allows chaining additional field lookups. Takes an integer year.

Example:

```python
Entry.objects.filter(pub_date__year=2005)
Entry.objects.filter(pub_date__year__gte=2005)
```

SQL equivalent:

**`SELECT** ... **WHERE** pub_date **BETWEEN** '2005-01-01' **AND** '2005-12-31';
**SELECT** ... **WHERE** pub_date >= '2005-01-01';`

### **`iso_year`**

For date and datetime fields, an exact ISO 8601 week-numbering year match. Allows chaining additional field lookups. Takes an integer year.

Example:

```python
Entry.objects.filter(pub_date__iso_year=2005)
Entry.objects.filter(pub_date__iso_year__gte=2005)
```

(The exact SQL syntax varies for each database engine.)

When [**`USE_TZ`**](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-USE_TZ) is **`True`**, datetime fields are converted to the current time zone before filtering. This requires [time zone definitions in the database](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#database-time-zone-definitions).

### **`month`**

For date and datetime fields, an exact month match. Allows chaining additional field lookups. Takes an integer 1 (January) through 12 (December).

Example:

```python
Entry.objects.filter(pub_date__month=12)
Entry.objects.filter(pub_date__month__gte=6)
```

### **`day`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#day)**

For date and datetime fields, an exact day match. Allows chaining additional field lookups. Takes an integer day.

Example:

```python
Entry.objects.filter(pub_date__day=3)
Entry.objects.filter(pub_date__day__gte=3)
```

(The exact SQL syntax varies for each database engine.)

Note this will match any record with a pub_date on the third day of the month, such as January 3, July 3, etc.

When [**`USE_TZ`**](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-USE_TZ) is **`True`**, datetime fields are converted to the current time zone before filtering. This requires [time zone definitions in the database](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#database-time-zone-definitions).

### **`week`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#week)**

For date and datetime fields, return the week number (1-52 or 53) according to [ISO-8601](https://en.wikipedia.org/wiki/ISO-8601), i.e., weeks start on a Monday and the first week contains the year’s first Thursday.

Example:

```python
Entry.objects.filter(pub_date__week=52)
Entry.objects.filter(pub_date__week__gte=32, pub_date__week__lte=38)
```

### **`week_day`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#week-day)**

For date and datetime fields, a ‘day of the week’ match. Allows chaining additional field lookups.

Takes an integer value representing the day of week from 1 (Sunday) to 7 (Saturday).

Example:

```python
Entry.objects.filter(pub_date__week_day=2)
Entry.objects.filter(pub_date__week_day__gte=2)
```

Note this will match any record with a **`pub_date`** that falls on a Monday (day 2 of the week), regardless of the month or year in which it occurs. Week days are indexed with day 1 being Sunday and day 7 being Saturday.

### **`iso_week_day`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#iso-week-day)**

For date and datetime fields, an exact ISO 8601 day of the week match. Allows chaining additional field lookups.

Takes an integer value representing the day of the week from 1 (Monday) to 7 (Sunday).

Example:

```python
Entry.objects.filter(pub_date__iso_week_day=1)
Entry.objects.filter(pub_date__iso_week_day__gte=1)
```

(No equivalent SQL code fragment is included for this lookup because implementation of the relevant query varies among different database engines.)

Note this will match any record with a **`pub_date`** that falls on a Monday (day 1 of the week), regardless of the month or year in which it occurs. Week days are indexed with day 1 being Monday and day 7 being Sunday.

### **`quarter`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#quarter)**

For date and datetime fields, a ‘quarter of the year’ match. Allows chaining additional field lookups. Takes an integer value between 1 and 4 representing the quarter of the year.

Example to retrieve entries in the second quarter (April 1 to June 30):

```python
Entry.objects.filter(pub_date__quarter=2)
```

(No equivalent SQL code fragment is included for this lookup because implementation of the relevant query varies among different database engines.)

### **`time`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#time)**

For datetime fields, casts the value as time. Allows chaining additional field lookups. Takes a [**`datetime.time`**](https://docs.python.org/3/library/datetime.html#datetime.time) value.

Example:

```python
Entry.objects.filter(pub_date__time=datetime.time(14, 30))
Entry.objects.filter(pub_date__time__range=(datetime.time(8), datetime.time(17)))
```

### **`hour`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#hour)**

For datetime and time fields, an exact hour match. Allows chaining additional field lookups. Takes an integer between 0 and 23.

Example:

```python
Event.objects.filter(timestamp__hour=23)
Event.objects.filter(time__hour=5)
Event.objects.filter(timestamp__hour__gte=12)
```

#### **`minute`**

For datetime and time fields, an exact minute match. Allows chaining additional field lookups. Takes an integer between 0 and 59.

Example:

```python
Event.objects.filter(timestamp__minute=29)
Event.objects.filter(time__minute=46)
Event.objects.filter(timestamp__minute__gte=29)
```

#### **`second`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#second)**

For datetime and time fields, an exact second match. Allows chaining additional field lookups. Takes an integer between 0 and 59.

Example:

```python
Event.objects.filter(timestamp__second=31)
Event.objects.filter(time__second=2)
Event.objects.filter(timestamp__second__gte=31)
```

SQL equivalent:

**`SELECT** ... **WHERE** **EXTRACT**('second' **FROM** **timestamp**) = '31';
**SELECT** ... **WHERE** **EXTRACT**('second' **FROM** **time**) = '2';
**SELECT** ... **WHERE** **EXTRACT**('second' **FROM** **timestamp**) >= '31';`

(The exact SQL syntax varies for each database engine.)

When [**`USE_TZ`**](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-USE_TZ) is **`True`**, datetime fields are converted to the current time zone before filtering. This requires [time zone definitions in the database](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#database-time-zone-definitions).

#### **`isnull`[¶](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#isnull)**

Takes either **`True`** or **`False`**, which correspond to SQL queries of **`IS NULL`** and **`IS NOT NULL`**, respectively.

Example:

`Entry.objects.filter(pub_date__isnull=**True**)`

#### 1.2: **LookUps that span relationships[¶](https://docs.djangoproject.com/en/4.0/topics/db/queries/#lookups-that-span-relationships-1)**

```python
from datetime import date

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

		def __str__(self):
			return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

		def __str__(self):
			return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

		def __str__(self):
			return self.headline
```

Django offers a powerful and intuitive way to “follow” relationships in lookups, taking care of the SQL **`JOIN`**s for you automatically, behind the scenes.

> **To span a relationship, use the field name of related fields across models, separated by double underscores, until you get to the field you want.**

For **ForeignKey()**

This example retrieves all **`Entry`** objects with a **`Blog`** whose **`name`** is **`'Beatles Blog'`**:

```python
**>>>** Entry.objects.filter(blog__name='Beatles Blog')
```

This spanning can be as deep as you’d like.

For **ManytoManyField()**

It works backwards, too. While it [**`can be customized`**](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.related_query_name), by default you refer to a “reverse” relationship in a lookup using the lowercase name of the model.

This example retrieves all **`Blog`** objects which have at least one **`Entry`** whose **`headline`** contains **`'Lennon'`**:

```python
**>>>** Blog.objects.filter(entry__headline__contains='Lennon')
```

If you are filtering across multiple relationships and one of the intermediate models doesn’t have a value that meets the filter condition, Django will treat it as if there is an empty (all values are **`NULL`**), but valid, object there. All this means is that no error will be raised. For example, in this filter:

```python
Blog.objects.filter(entry__authors__name='Lennon')
```

(if there was a related **`Author`** model), if there was no **`author`** associated with an entry, it would be treated as if there was also no **`name`** attached, rather than raising an error because of the missing **`author`**. Usually this is exactly what you want to have happen. The only case where it might be confusing is if you are using [**`isnull`**](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#std:fieldlookup-isnull). Thus:

```python
Blog.objects.filter(entry__authors__name__isnull=True)
```

will return **`Blog`** objects that have an empty **`name`** on the **`author`** and also those which have an empty **`author`** on the **`entry`**. If you don’t want those latter objects, you could write:

```python
Blog.objects.filter(entry__authors__isnull=**False**, entry__authors__name__isnull=**True**)
```

### **Spanning multi-valued relationships[¶](https://docs.djangoproject.com/en/4.0/topics/db/queries/#spanning-multi-valued-relationships)**

When spanning a [**`ManyToManyField`**](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ManyToManyField) or a reverse [**`ForeignKey`**](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey) (such as from **`Blog`** to **`Entry`**), filtering on multiple attributes raises the question of whether to require each attribute to coincide in the same related object. We might seek blogs that have an entry from 2008 with *“Lennon”* in its headline, or we might seek blogs that merely have any entry from 2008 as well as some newer or older entry with *“Lennon”* in its headline.

To select all blogs containing at least one entry from 2008 having *“Lennon”* in its headline (the same entry satisfying both conditions), we would write:

```python
Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
```

Otherwise, to perform a more permissive query selecting any blogs with merely *some* entry with *“Lennon”* in its headline and *some* entry from 2008, we would write:

```python
Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
```

When you try to filter the Model instance by field that has foriegn key.

```python
class Profile(models.Model):
Gender_Choices = [
("Male", "Male"),
("Female", "Female"),
]
username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
first_name = models.SlugField(max_length=10, null=True)
second_name = models.CharField(max_length=10, null=True)
```

### **`in`**

In a given iterable; often a list, tuple, or queryset. It’s not a common use case, but strings (being iterables) are accepted.

Examples:

```python

Entry.objects.filter(id__in=[1, 3, 4])
#Entry.objects.filter(id__in=1) #Error:int is not iterable
Entry.objects.filter(headline__in='abc')
```

You can also use a queryset to dynamically evaluate the list of values instead of providing a list of literal values:

```python
inner_qs = Blog.objects.filter(name__contains='Cheddar')
entries = Entry.objects.filter(blog__in=inner_qs)
```

#Error1
Profile.objects.get(username=="testuser")
Traceback (most recent call last):
File "<console>", line 1, in <module>
NameError: name 'username' is not defined

#Error2
Profile.objects.filter(username\_\_icontains="testuser")
django.core.exceptions.FieldError: Related Field got invalid lookup: icontaines

#Error3
Profile.objects.get(username="testuser")
ValueError: Field 'id' expected a number but got 'testuser'.

**Solution**

retrieves a `Profile` \***\*obj with a `User` whose `username`  is **`'testuser'`\*\*
:
search for the Profile obj that is associated with username 'testuser'

```python
Profile.objects.get(username__username__contains="testuser")
'''
here first username refers to the field of Profile
second refers to the field of User.
'''
```

**Complex queries using `Q` objects:**

```python
    from django.db.models import Q
    products = Product.objects.filter(Q(price__gte=500) & Q(name__icontains="phone"))
```

#### QuerySets API

In short, A **`QuerySet`** is a list of objects of certain class that can be `constructed`, `filtered`, `iterated`, `sliced`, and generally passed around without actually hitting the database. No database activity actually occurs until you do something to evaluate the queryset.

#### **1: `QuerySet` methods: `get()` Vs `filter()`**

Note that there is a difference between using [**`get()`**](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.get), and using [**`filter()`**](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.filter) with a slice of **`[0]`**. If there are no results that match the query, [**`get()`**](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.get) will raise a **`DoesNotExist`** exception. This exception is an attribute of the model class that the query is being performed on - so in the code above, if there is no **`Entry`** object with a primary key of 1, Django will raise **`Entry.DoesNotExist`**.

Similarly, Django will complain if more than one item matches the [**`get()`**](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.get) query. In this case, it will raise [**`MultipleObjectsReturned`**](https://docs.djangoproject.com/en/4.0/ref/exceptions/#django.core.exceptions.MultipleObjectsReturned), which again is an attribute of the model class itself.

#### **2: QUERIES THAT RETURNS A SINGLE MODEL INSTANCE**

```python
from .models import *

#(1)Returns first customer in table
firstCustomer = Customer.objects.first()

#(2)Returns last customer in table
lastCustomer = Customer.objects.last()

#(3)Returns single customer by name
customerByName = Customer.objects.get(name='Peter Piper')


```

#### **3: QUERIES THAT RETURNS MULTIPLE INSTANCES OF MODEL**

```python
 #1)Returns all customers from customer table
  customers = Customer.objects.all()

#2)Return by chaining attributes
  getp=Parentmodel.objects.all().filter(age=24)
  print(getp)

#3)Order/Sort Objects by id
#very useful for listing item according to price
	leastToGreatest = Parentmodel.objects.all().order_by('age')
	greatestToLeast = Parentmodel.objects.all().order_by('-age')
	lisbyid=Parentmodel.objects.all().order_by('id') #ascending order

#(4) Returns all childmodels with parent(attribute) of "Sapana"
	childFilteredbyParent = Childmodel.objects.filter(parent__name="Sapana")
"""
Note:parent is a field of Childmodel that is pointing to Parentmodel.
reate a query that references a related model using __ (two underscores) (a.k.a. "follow notation") to indicate a field in the related model.
"""

#(5)Exclude specific models from table
	getPModel=Parentmodel.objects.exclude(age=24)

#(6)return model by Fields look up  (highly used in search engine)
	Customer.objects.filter(name__icontains="sam")
'''
icontains is a case-sensitive.
<QuerySet [<Customer: samir>, <Customer: sambhav>]>'''

#(7) return models from 0 to 3
getPModel=Parentmodel.objects.all()[0:3]
'''
<QuerySet [<Parentmodel: Sapana>, <Parentmodel: Pawan>, <Parentmodel: Samir>]>
'''

#(8) returns only those customer who's name attribute is not null
customer = Customer.objects.filter(name__isnull=False)
'''
<QuerySet [<Post: Photoshop Blend modes>]>
'''

```

#### Managing and Interacting with Databases in Django

- **Custom Managers:** Extend the default manager to add custom query methods.

  ```python
  class ProductManager(models.Manager):
      def expensive_products(self):
          return self.filter(price__gte=1000)

  class Product(models.Model):
      name = models.CharField(max_length=100)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      objects = ProductManager()
  ```

- **Raw SQL:** Execute raw SQL queries when necessary.
  ```python
  from django.db import connection
  with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM product")
      results = cursor.fetchall()
  ```

#### Model RelationShip in Advanced

Django models operate by default on relational database systems (RDBMS) and thus they also support relationships amongst one another. In the simplest terms, database relationships are used to associate records on the basis of a key or id, resulting in improved data maintenance, query performance and less duplicate data, among other things.

Django models support the same three relationships supported by relational database systems: One to many, many to many and one to one.

## 1.**One to many relationship**

A one to many relationship implies that one model record can have many other model records associated with itself. For example, a `Parent` model record can have many `Child` model records associated with it and yet an `Child` belongs to a single `Parent` record.

To define a one to many relationship in Django models, you use the `ForeignKey` data type on the model that has the many records (e.g. on the `Child` model). Listing 7-22 illustrates a sample of a one to many Django relationship.

### **Listing 7-22. One to many Django model relationship**

```
class Parentmodel(models.Model):
	name = models.CharField(max_length=200, null=True)
	age = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return str(self.name)

class Childmodel(models.Model):
	parent = models.ForeignKey(Parentmodel,on_delete=models.CASCADE,null=True)
	name = models.CharField(max_length=200, null=True)
	age = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return str(self.name)

```

The first Django model in listing 7-22 is `Parent` and has the `name` field. Next, in listing 7-22 is the `Child`  model which has a `parent` field, that itself has the `models.ForeignKey(Parent)` definition. The `models.ForeignKey()` definition creates the one to many relationship, where the first argument `Parent` indicates the relationship model.

In addition to the database level benefits of creating a one to many relationship (e.g. improved data maintenance), Django models also provide an API to simplify the access of data related to this kind of relationship which is explained in the next chapter on [CRUD records across Django model relationships](https://www.webforefront.com/django/relationshipmodelrecords.html).

### Operations with `set.` syntax

```python
accessPModel = Parentmodel.objects.get(name="Sapana")

#1)Returns all child related to one single Parent model
    getCModel=accessPModel.childmodel_set.all()
    #childmodel is a second model wriiten in lowercase.

#2)Return total number of Childmodels.
	  getCModel=accessPModel.childmodel_set.count()

#3)Returns all the child of parents witha age 21
		getCModel=accessPModel.childmodel_set.filter(age=21)

#4)Fetch Child records that match a filter for the Menu
    getc = accessPModel.childmodel_set.filter(name__startswith='Whole')

#(5)Exclude specific models from table
		getCModel=accessPModel.childmodel_set.exclude(age=21)

#(6)return model by Fields look up  (highly used in search engine)
		getc = accessPModel.childmodel_set.filter(name__icontains="sam")

```

**CRUD OPERATION WITH `_set` syntax**

The reverse `_set` syntax is used to perform read operations parting from models that don't have an explicit relationship field toward the model that has the relationship field. It's also possible to use the same `_set` syntax to execute other database operation (e.g. Create, Update , Delete), a

```python

getp=Parentmodel.objects.get(name__icontains="Pawan")

# Sets an Child directly to the Parent
	getp.childmodel_set.create(name="Sambhav Malla",age=19)

# Create an Item separately and then add it to the Menu
	newchild = Childmodel(name='Sampada Malla',age=14)
	getp.childmodel_set.add(newchild,bulk=False)
'''
NOTE: bulk=False is necessary for new_menu_item to be saved by the Item model manager first. it isn't possible to call new_menu_item.save() directly because it lacks a menu instance
'''
# Create copy of childs for later
	child_items = [bi for bi in getp.childmodel_set.all()]

# Clear child items from Parent model
	 getp.childmodel_set.clear()

'''
NOTE: This requires the ForeignKey definition to have null=True
 (e.g. models.ForeignKey(Menu, null=True)) so the key is allowed to be turned null
  otherwise the error 'RelatedManager' object has no attribute 'clear' is thrown
'''

# Reassign Item set from copy of breakfast items
	getp.childmodel_set.set(child_items)

# Clear a single child item from Parent
	child_one = Childmodel.objects.get(name='Sambhav Malla')
	getp.childmodel_set.remove(child_one)

'''
NOTE: This requires the ForeignKey definition to have null=True
(e.g. models.ForeignKey(Menu, null=True)) so the key is allowed to be turned null
Otherwise the error 'RelatedManager' object has no attribute 'remove' is thrown
'''

# Delete the Parent Instance along with its associated child elements
	getp.delete()
'''
# NOTE: This requires the ForeignKey definition to have blank=True
and on_delete=models.CASCADE (e.g. models.ForeignKey(Menu, blank=True, on_delete=models.CASCADE))
'''
```

<aside>
⚠️ **Note:** The add(), create(), remove(), clear() and set() relationship methods all apply database changes immediately for all types of related fields. This means there's no need to call save() on either end of the relationship.

</aside>

## 2.**Many to many relationship**

A many to many relationship implies that many records can have many other records associated amongst one another. For example, `Store` model records can have many `Amenity` records, just as `Amenity` records can belong to many `Store` records. To define a many to many relationship in Django models you use the `ManyToManyField` data type. Listing 7-23 illustrates a sample of a many to many Django relationship.

### **Listing 7-23. Many to many Django model relationship**

```
#2.Many to many relationship
class Book(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.name)

class Stationary(models.Model):
    name = models.CharField(max_length=30, null=True)
    books = models.ManyToManyField(Book, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)

```

The first Django model in listing 7-23 is `Book` and has the `name` and `description` fields. Next, in listing 7-23 is the `Stationary` Django model which has the `books` field, that itself has the `models.ManyToManyField(Book,blank=True)` definition. The `models.ManyToManyField()` definition creates the many to many relationship via a *junction table[[5]](https://www.webforefront.com/django/setuprelationshipsdjangomodels.html#footnote-5)*, where the first argument `Book` indicates the relationship model and the optional `blank=True` argument allows a `Stationary` record to be created without the need of an `books` value.

In this case, the junction table created by Django is used to hold the relationships between the `Book` and `Store` records through their respective keys.

Although you don't need to manipulate the junction table directly, for reference purposes, Django uses the syntax `<model_name>_<model_field_with_ManyToManyField>` to name it.

In addition to the database level benefits of creating a many to many relationship (e.g. improved data maintenance), Django models also provide an API to simplify the access of data related to this kind of relationship, which is explained in the next chapter on [CRUD records across Django model relationships](https://www.webforefront.com/django/relationshipmodelrecords.html).

**FORWARD QUERING**, **CRUD OPERATION WITH `_set` syntax**

```python

book1= Book.objects.get(name='Physics')

# Fetch all Stationary that contains 'Physics' Book
book1.stationary_set.all()

# Get the total no of Stationary that contains 'Physics' Book
book1.stationary_set.count()

# Fetch Store records that match a filter with the Wifi Amenity
book1.stationary.filter(name__endswith='Diego')

# Create a Store directly with the Wifi Amenity
book1.stationary.create(name='Uptown Gallery',address='1240 University Ave...')
#NOTE: Django also supports the get_or_create() and update_or_create() operations

# Create a Store separately and then add the Wifi Amenity to it
stationary1 = Stationary(name='Midtown Books',address='844 W Washington St...')
stationary1.save()
book1.stationary_set.add(stationary1)

# Create copy of breakfast items for later
books_in_staty = [ws for ws in book1.stationary_set.all()]

# Clear all the book records in the junction table for all Stationary Instances.
book1.stationary_set.clear()

# Reassign Wifi set from copy of Store elements
book1.stationary_set.set(books_in_staty)

#Remove the book from Stationary Instance
store_to_remove_book = Stationary.objects.get(name__startswith='Newroad')
book1.stationary_set.remove(store_to_remove_book)

# Delete the Book along with its associated junction table records for Stationary.
book1.delete()

#Return all the books that stationary has.
stat1 = Stationary.objects.get(id=1)
stat1.books.all()

```

**Backward Quering**

```python
#Return all the books that stationary has.
stat1 = Stationary.objects.get(id=1)
stat1.books.all()    #books is a attribute
```

## 3.**One to one relationship**

A one to one relationship implies that one record is associated with another record. If you're familiar with object-orientated programming, a one to one relationship in RDBMS is similar to object-oriented inheritance that uses the *is a* rule (e.g. a Car object *is a* Vehicle object).

For example, generic `Item` model records can have a one to one relationship to `Drink` model records, where the latter records hold information specific to drinks (e.g. caffeine content) and the former records hold generic information about items (e.g. price). To define a one to one relationship in Django models you use the `OneToOneField` data type. Listing 7-24 illustrates a sample of a one to one Django relationship.

### **Listing 7-24 One to one Django model relationship**

```
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    calories = models.IntegerField()
    price = models.FloatField()

class Drink(models.Model):
    item = models.OneToOneField(Item,on_delete=models.CASCADE,primary_key=True)
    caffeine = models.IntegerField()

```

The first Django model in listing 7-24 is `Item` which is similar to the one presented in [listing 7-22](https://www.webforefront.com/django/setuprelationshipsdjangomodels.html#listing-7-22), except the version in listing 7-24 has the additional `calories` and `price` fields. Next, in listing 7-24 is the `Drink` model which has the `item` field, that itself has the `models.OneToOneField(Amenity,on_delete=models.CASCADE,primary_key=True)` definition.

The `models.OneToOneField()` definition creates the one to one relationship, where the first argument `Item` indicates the relationship model. The second argument `on_delete=models.CASCADE` tells Django that in case the relationship record is deleted (i.e. the `Item`) its other record (i.e. the `Drink`) also be deleted, this last argument prevents orphaned data. Finally, the `primary_key=True` tells Django to use the relationship id (i.e. `Drink.id`) as the primary key instead of using a separate and default column `id`, a technique that makes it easier to track relationships.

In addition to the database level benefits of creating a one to one relationship (e.g. improved data maintenance), Django models also provide an API to simplify the access of data related to this kind of relationship, which is explained in the next chapter on [CRUD records across Django model relationships](https://www.webforefront.com/django/relationshipmodelrecords.html).

**CRUD OPERATION WITH `_set` syntax**

```
from django.contrib.auth.models import User

class Customer(models.Model):  #
	user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE,
         null=True, blank=True)
	name = models.CharField(max_length=100, null=True)
	email = models.CharField(max_length=100, null=True)
  age = models.IntegerField()
	class Meta:
		ordering=('user',)#Descending order . -user for ascending order

	def __str__(self):
		return self.name

# Get User instance named Mocha
user1 = User.objects.get(name='Sam')

# Access the Customer element and its fields through its base User Model
user1.profile.email

# Get Customer objects through User with age field less than 20
User.objects.filter(customer__age__lt=20)

# Delete the User and its associated Customer instance
user1.delete()

'''
 NOTE: This deletes the associated Drink record due to the
 on_delete=models.CASCADE in the OneToOneField definition
'''

# Query a Customer through an User property
Customer.objects.get(user__name='Sam')
```

## **Options for relationship model data types**

Previously you explored [Django data types and their many options](https://www.webforefront.com/django/modeldatatypesandvalidation.html) to customize how they handle data, such as : limiting values, allowing empty and null values, establishing predetermined values and enforcing DDL rules. In this section you'll learn about the options available for Django relationship model data types.

**Note** Options described in the [general purpose model data type section](https://www.webforefront.com/django/modeldatatypesandvalidation.html) (e.g. blank, unique) are applicable to relationship model data types unless noted.

### **Data integrity options: on_delete**

```python
class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
```

All model relationships create dependencies between one another, so an important behavior to define is what happens to the other party when one party is removed. The `on_delete` option is designed for this purpose, to determine what to do with records on the other side of a relationship when one side is removed.

For example, if an `Item` model has a `menu` `ForeignKey()` field pointing to a `Menu` model (a one to many relationship: an `Item` always belong to one `Menu`, and a `Menu` has many `Items`), what happens to `Item` model records if their related `Menu` model instance is deleted ? Are the `Item` model records also deleted ?

The `on_delete` option is available for all three relationship model data types and supports the following values:

- `on_delete=models.CASCADE` (Default).- Automatically deletes related records when the related instance is removed (e.g. if the `Menu` *Breakfast* instance is deleted, all `Item` records referencing the `Menu` *Breakfast* instance are also deleted)
- `on_delete=models.PROTECT`.- Prevents a related instance from being removed (e.g. if the `menu` field on `Item` uses `ForeignKey(Menu,on_delete=models.PROTECT)`, any attempt to remove `Menu` instances referenced by `Item` instances are blocked).
- `on_delete=models.SET_NULL`.- Assigns NULL to related records when the related instance is removed, note this requires the field to also use the `null=True` option (e.g. if the `Menu` *Breakfast* instance is deleted, all `Item` records referencing the `Menu` *Breakfast* instance are assigned NULL to their `menu` field value).
- `on_delete=models.SET_DEFAULT`.- Assigns a default value to related records when the related instance is removed, note this requires the field to also use a `default` option value (e.g. if the `Menu` *Breakfast* instance is deleted, all `Item` records referencing the `Menu` *Breakfast* instance are assigned a default `Menu` instance to their `menu` field value).
- `on_delete=models.SET`.- Assigns a value set through a callable to related records when the related instance is removed (e.g. if the `Menu` *Breakfast* instance is deleted, all `Item` records referencing the `Menu` *Breakfast* instance are assigned an instance to their `menu` field value set through a callable function).
- `on_delete=models.DO_NOTHING`.- No action is taken when related records are removed. This is generally a bad relational database practice, so by default, databases will generate an error since you're leaving orphaned records with no value, null or otherwise. If you use this value, you must ensure the database table does not enforce referential integrity.

### **Reference options: self, literal strings and parent_link**

Model relationships sometimes have recursive relationships. This is a common scenario in one to many relationship models with parent-child relationships. For example, a `Category` model can have a `parent` field which in itself is another `Category` model or a `Person` model can have a `relatives` field which in itself are other `Person` models. To define this type of relationship you must use the `'self'` keyword to reference the same model, as shown in listing 7-25.

### **Listing 7-25 One to many Django model relationship with self-referencing model**

```
from django.db import models

class Category(models.Model):
    menu = models.ForeignKey('self')

class Person(models.Model):
    relatives = models.ManyToManyField('self')

```

Although model relationship data types typically express their relationships through model object references (e.g. `models.ForeignKey(Menu)`), it's also valid to use literal strings to reference models (e.g. `models.ForeignKey('Menu')`). This technique is helpful when the model definition order does not allow you to reference model objects that are not yet in scope and is a technique often referred to as model 'lazy-loading'.

The `parent_link=True` option is an exclusive option for one to one relationships (i.e the `models.OneToOneField` data type) used when inheriting model classes, to help indicate the child class field should be used as a link to the parent class.

### **Reverse relationships: related_name, related_query_name and symmetrical**

When you use relationship model data types, Django automatically establishes the reverse relationship between data types with the the `_set` reference. This mechanism is illustrated in listing 7-26.

### **Listing 7-26 One to many Django model relationship with reverse relationship references**

```
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.FloatField(blank=True,null=True)

breakfast = Menu.objects.get(name='Breakfast')

# Direct access
all_items_with_breakfast_menu = Item.objects.filter(menu=breakfast)

# Reverse access through instance
same_all_items_with_breakfast_menu = breakfast.item_set.all()

```

As you can see in listing 7-26, there are two routes between a Django relationship. The direct route involves using the model with the relationship definition, in this case, `Item` gets all the `Item` records with a `Menu` *Breakfast* instance. To do this, you use `Item` and filter on the `menu ForeignKey` reference (e.g. `Item.objects.filter(menu=breakfast)`).

But it's also possible to use a `Menu` instance (e.g. `breakfast` in listing 7-26) and get all `Item` records with a `menu` instance, this is called a reverse relationship or path. As you can see in the listing 7-26, the reverse relationship uses the `<model_instance>.<related_model>_set` syntax (e.g. `breakfast.item_set.all()` to get all `Item` records with a the `breakfast` instance).Now that you know what a reverse relationship is, let's explore the options associated with this term.

The `related_name` option allows you to customize the name or disable a reverse model relationship. Renaming a reverse relationship provides more intuitive syntax over the `_set` syntax from listing 7-26, where as disabling a reverse relationship is helpful when a related model is used in other contexts and blocking access to a reverse relationship is required for accessibility reasons.

For example, in listing 7-26 the reverse relationship uses the `breakfast.item_set.all()` syntax, but if you change the field to `models.ForeignKey(...related_name='menus')`, you can use the reverse relationship `breakfast.menus.all()` syntax. To disable a reverse relationship you can use the `+` (plus sign) on the `related_name` value (e.g. `models.ForeignKey(...related_name='+')`).

Reverse relationships are also available as part of queries, as illustrated in listing 7-27.

### **Listing 7-27 One to many Django model relationship with reverse relationship queries**

```
# Based on models fromlisting 7-26

# Direct access, Item records with price higher than 1
Items.objects.filter(price__gt=1)

# Reverse access query, Menu records with Item price higher than 1
Menu.objects.filter(item__price__gt=1)

```

Notice how the `Menu` query in listing 7-27 uses the `item` reference to filter all `Menu` records via its `Item` relationship. By default, reverse relationship queries use the name of the model, so in this case, the related `Menu` model is `Item`, therefore the query field is `item`. However, if you define the `related_name` option on a field this value takes precedence. For example, with `models.ForeignKey(...related_name='menus')` the reverse query in listing 7-27 becomes `Menu.objects.filter(menus__price__gt=1)`, all of which takes us to the `related_query_name` option.

The `related_query_name` option is used to override the `related_name` option value for cases where you want the reverse query to have a different field value. For example, with `models.ForeignKey(...related_name='menus',related_query_name='onlyitemswith')` the reverse relationship reference for menus is [listing 7-26](https://www.webforefront.com/django/setuprelationshipsdjangomodels.html#listing-7-26) would still work, but the reverse relationship query from [listing 7-27](https://www.webforefront.com/django/setuprelationshipsdjangomodels.html#listing-7-27) would change to `Menu.objects.filter(onlyitemswith__price__gt=1)`.

Covering an edge-case for many to many relationships is the `symmetrical` option. If you create a many to many relationship that references itself -- as illustrated in [listing 7-25](https://www.webforefront.com/django/setuprelationshipsdjangomodels.html#listing-7-25) with the `'self'` syntax -- Django assumes the relationship is symmetrical (e.g. all `Person` instances are `relatives` and therefore requires no reverse relationships since it would be redundant) thus self referencing many to many relationships forgoe adding a `_set` reverse relationship to the field. You can use `symmetrical=False` to force Django to maintain the reverse relationship.

**Tip** The next chapter covers [Django model relationship queries](https://www.webforefront.com/django/relationshipmodelrecords.html) in greater detail.

### **Database options: to_field, db_constraint, swappable, through, through_fields and db_table**

By default, Django model relationships are established on the primary key of a model which in itself defaults to a model's `id` field. For example, the field `menu = models.ForeignKey(Menu)` stores the `id` from a `Menu` instance as the relationship reference. You can override this default behavior with the `to_field` option and specify a different field on which to establish the relationship reference. Note that if you assign a `to_field` value, this field must be set with `unique=True`.

By default, Django follows relational database conventions and constrains relationships at the database level. The `db_constraint` option -- which defaults to `True` -- allows you to bypass this constraint by assigning it a `False` value. Setting `db_constraint=False` should only by used when you know beforehand the data relationships in a database is broken and doesn't require constraint checking at the database level.

The `swappable` option is intended to influence migrations for models that contain relationships and are swappable with other models. Unless you implement a very sophisticated model hierarchy with model swapping features, this option is primarily intended for Django's built-in `User` model which uses a relationship and is often swapped out for custom user models. The chapter on [user management contains more details on this swappable model option](https://www.webforefront.com/django/customusermodel.html) .

Specific to many to many model relationships (i.e. the `models.ManyToManyField` data type) the `through`, `through_fields &` `db_table` options, influence the junction table used in these type of relationships. If you wan't to change the default name for a many to many junction table, you can use the `db_table` option to specify a custom junction table name.

By default, a junction table for a many to many relationship stores a minimum amount of information: an id for the relationship and the id's for each of the model relationships. It's possible to specify a separate model to operate as a junction table and store additional information about the many to many relationship (e.g. `through=MyCustomModel` uses the `MyCustomTable` model as the many to many junction table). If you define a `through` option, then it's also necessary to use the `through_fields` to tell Django which fields in the new model are used to store references for the model relationships.

### **Form values: limit_choices_to**

When Django models with relationships are used in the context of forms, it can be useful and even necessary to delimit the amount of displayed relationships. For example, if you use an `Item` model with a relationship to a `Menu` model, displaying the entire set of `Item` records as forms (e.g. in the Django admin) can be impractical if you have hundreds of `Item` records.

The `limit_choices_to` can be used on a relationship model type to filter the amount of displayed records in forms. The `limit_choices_to` can declare an in-line reference field filter (e.g. `limit_choices_to={'in_stock':True}`) or a callable that performs more complex logic (e.g. `limit_choices_to=my_complex_method_limit_picker`).
