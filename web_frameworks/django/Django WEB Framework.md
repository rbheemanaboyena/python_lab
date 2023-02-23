# Django WEB Framework

Django is a high-level web framework written in Python that allows you to quickly build web applications by providing a set of tools and libraries that handle common web development tasks, such as URL routing, database interaction, form handling, authentication, and more. Here are some key concepts and features of Django:

1. Model-View-Controller (MVC) Architecture: Django follows a similar pattern called Model-View-Template (MVT), which separates the code into three main components: models, views, and templates. Models define the data structure and interact with the database, views handle requests and generate responses, and templates render the HTML.
2. Object-Relational Mapping (ORM): Django provides an ORM that allows you to interact with the database using Python code, rather than writing SQL queries directly. This makes it easier to work with the database and reduces the risk of SQL injection attacks.
3. Admin Interface: Django comes with a built-in admin interface that allows you to manage your application's data through a web-based interface. You can create, read, update, and delete records in the database without writing any code.
4. URL Routing: Django provides a powerful URL routing system that allows you to map URLs to views and pass parameters between them. This makes it easy to create complex, dynamic websites with multiple pages and forms.
5. Template Engine: Django's template engine allows you to separate the presentation logic from the business logic in your code. You can define templates that define the HTML structure and use template tags and filters to insert dynamic data into the page.
6. Security Features: Django provides several built-in security features, such as password hashing, cross-site request forgery (CSRF) protection, and clickjacking protection. This makes it easier to build secure web applications that protect users' data and prevent attacks.

### Framework Folder Structure

![Untitled](diagrams/django_file_struture.png))

### Creating Sample Applications

**Python virtual environment** 

A virtual environment is a self-contained directory that contains a specific version of Python and all the packages and dependencies required for a particular project. Virtual environments are useful when you need to work on multiple projects with different dependencies, or when you want to isolate a project's dependencies from the global Python environment.

```python
#creating virtual env
python -m venv <env_name>

#activate virtual env
source <env_name>/bin/activate

#deactivate
deactivate
```

**Installing Django package**

```python
 pip install django
```

**Creating Django Project**

```python
django-admin startproject <project_name>
```

**Creating  app**

```python
python [manage.py](http://manage.py) startapp <app_name>
```

Refers the sample django project in projects dir
