# Python Tutorial website

## Getting Started

install Django

```bash
pip install django
```

start a project a new project

```bash
django-admin startproject mysite
```

create a main

```bash
cd mysite
py manage.py startapp main
```

run the server to check if every think is working

```bash
py manage.py runserver
```

![boilerplat](reademeimages/boilerplate.PNG)

## Routes

Add the below code to the urls.py to create a route for the emply url

```python
from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.homepage, name="homepage"),
```

## Create Models

create a model, a tutorial table, we need to edit the file models.py

```python
from django.db import models

# Create your models here.


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published")

    def __str__(self):
        return self.tutorial_title

```

then we need to make migration then we migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

## Admin Page

Create and admin page, for that we need an admin user

```bash
python manage.py createsuperuser
```

provide username, email and password.
Type in the url http://127.0.0.1:8000/admin, and type the username and password

![djangoadmin](reademeimages/djangoadmin.PNG)

Add the models to the admin page

```python
from django.contrib import admin
from .models import Tutorial
# Register your models here.

admin.site.register(Tutorial)
```

## Views and Templates

Install a text editor called tinymce4-lite

```bash
pip install django-tinymce4-lite
```

![texteditor](reademeimages/texteditor.PNG)

modify the view to show the models

```python
<head>
  {% load static %} <link href="{%static 'tinymce/css/prism.css'%}"
  rel="stylesheet"
</head>
<body>
  {% for tut in tutorials %}
  <p>{{tut.tutorial_title}}</p>
  <p>{{tut.tutorial_published}}</p>
  <p>{{tut.tutorial_content|safe}}</p>
  {% endfor %}
</body>
<script src="{% static 'tinymce/js/prism.js' %}"></script>
```

## Styling and CSS
