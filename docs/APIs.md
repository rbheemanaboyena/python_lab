# APIs

An API (Application Programming Interface) allows different software systems to communicate with each other. In the case of Python, there are many APIs available that allow developers to access different services and resources, such as web services, databases, or data from other applications.

- APIs vs RESTful APIs
    
    API (Application Programming Interface) and RESTful API are related but distinct concepts.
    
    An API is a general concept that refers to a set of protocols, routines, and tools for building software and applications. An API defines the way in which software components should interact with each other, and it provides a means of accessing the functionality of a software component or system.
    
    On the other hand, a RESTful API is a specific type of API that conforms to the architectural style known as Representational State Transfer (REST). RESTful APIs are designed to take advantage of existing HTTP protocols to provide a simple, lightweight, and scalable means of accessing data and services over the internet.
    
    The key differences between an API and a RESTful API are:
    
    1. Architecture: An API is a general concept, while a RESTful API is a specific type of API that adheres to the REST architectural style.
    2. Protocols: An API can use any number of protocols, while RESTful APIs use HTTP as the underlying protocol.
    3. Data Transfer: An API can transfer data in any format, while RESTful APIs transfer data using HTTP requests and responses in a format such as JSON or XML.
    4. Statelessness: RESTful APIs are stateless, meaning that the server does not maintain any client state between requests. This makes RESTful APIs highly scalable and flexible.
    
    In summary, a RESTful API is a type of API that follows the REST architectural style and uses HTTP as the underlying protocol for data transfer.
    
- Defining an API
    
    In Python, you can define an API by creating a server that provides endpoints that clients can call. An endpoint is a specific URL that provides access to a specific resource or service. There are several frameworks available in Python that make it easy to create a RESTful API, such as Flask and Django. 
    
    - Flask
        - Examples
            
            Here's an example of a simple API defined using Flask:
            
            ```python
            
            from flask import Flask, jsonify
            
            app = Flask(__name__)
            
            @app.route("/")
            def home():
                return "Welcome to my API"
            
            @app.route("/products", methods=["GET"])
            def products():
                products = [
                    {"id": 1, "name": "Product 1"},
                    {"id": 2, "name": "Product 2"},
                    {"id": 3, "name": "Product 3"},
                ]
                return jsonify(products)
            
            if __name__ == "__main__":
                app.run(debug=True)
            
            ```
            
            In this example, we have defined two endpoints: **`"/"`** and **`"/products"`**. The endpoint **`"/"`** returns a simple welcome message, while the endpoint **`"/products"`** returns a list of product objects in JSON format.
            
            When the script is run, the API will be available at **`http://localhost:5000/`**, and you can access the endpoints by making requests to the appropriate URLs.
            
            ```python
            #A simple API to perform arithmetic operations:
            from flask import Flask, request, jsonify
            
            app = Flask(__name__)
            
            @app.route("/math/<operation>", methods=["GET"])
            def perform_operation(operation):
                a = int(request.args.get("a"))
                b = int(request.args.get("b"))
            
                if operation == "add":
                    result = a + b
                elif operation == "subtract":
                    result = a - b
                elif operation == "multiply":
                    result = a * b
                elif operation == "divide":
                    result = a / b
                else:
                    return "Invalid operation", 400
            
                return jsonify({"result": result})
            
            if __name__ == "__main__":
                app.run(debug=True)
            ```
            
            how you can implement a RESTful API with all the main HTTP methods (GET, POST, PUT, DELETE) in Python using the Flask framework
            
            ```python
            from flask import Flask, request
            app = Flask(__name__)
            
            books = [
                {
                    'id': 1,
                    'title': 'The Hitchhiker\'s Guide to the Galaxy',
                    'author': 'Douglas Adams',
                    'published_year': 1979
                },
                {
                    'id': 2,
                    'title': 'The Lord of the Rings',
                    'author': 'J.R.R. Tolkien',
                    'published_year': 1954
                }
            ]
            
            @app.route('/books', methods=['GET'])
            def get_books():
                return {'books': books}, 200
            
            @app.route('/books/<int:book_id>', methods=['GET'])
            def get_book(book_id):
                book = next((book for book in books if book['id'] == book_id), None)
                if book:
                    return {'book': book}, 200
                else:
                    return {'message': 'Book not found'}, 404
            
            @app.route('/books', methods=['POST'])
            def add_book():
                data = request.get_json()
                book = {
                    'id': len(books) + 1,
                    'title': data['title'],
                    'author': data['author'],
                    'published_year': data['published_year']
                }
                books.append(book)
                return {'book': book}, 201
            
            @app.route('/books/<int:book_id>', methods=['PUT'])
            def update_book(book_id):
                book = next((book for book in books if book['id'] == book_id), None)
                if book:
                    data = request.get_json()
                    book.update({
                        'title': data['title'],
                        'author': data['author'],
                        'published_year': data['published_year']
                    })
                    return {'book': book}, 200
                else:
                    return {'message': 'Book not found'}, 404
            
            @app.route('/books/<int:book_id>', methods=['DELETE'])
            def delete_book(book_id):
                book = next((book for book in books if book['id'] == book_id), None)
                if book:
                    books.remove(book)
                    return {'message': 'Book deleted'}, 200
                else:
                    return {'message': 'Book not found'}, 404
            
            if __name__ == '__main__':
                app.run(debug=True)
            ```
            
            Pagination 
            
            ```python
            from flask import Flask, request
            app = Flask(__name__)
            
            books = [
                {
                    'id': 1,
                    'title': 'The Hitchhiker\'s Guide to the Galaxy',
                    'author': 'Douglas Adams',
                    'published_year': 1979
                },
                {
                    'id': 2,
                    'title': 'The Lord of the Rings',
                    'author': 'J.R.R. Tolkien',
                    'published_year': 1954
                },
                # ... more books ...
            ]
            
            @app.route('/books', methods=['GET'])
            def get_books():
                page = request.args.get('page', 1, type=int)
                per_page = request.args.get('per_page', 10, type=int)
                start = (page - 1) * per_page
                end = start + per_page
                return {'books': books[start:end]}, 200
            
            # ... other endpoints ...
            
            if __name__ == '__main__':
                app.run(debug=True)
            
            '''
            In this example, the /books endpoint implements the GET method. The request parameters page and per_page specify the page number and number of items per page, respectively. The start and end indices are calculated based on these parameters to extract a portion of the books list.
            
            You can test this endpoint with different values of page and per_page parameters to see the pagination in action. For example:
            
            http://localhost:5000/books?page=1&per_page=2 will return the first two books.
            http://localhost:5000/books?page=2&per_page=2 will return the next two books.
            '''
            ```
            
            weather_data Example, you can refer here [https://gitlab.com/bheemanaboyena1998/weather_data/-/tree/main](https://gitlab.com/bheemanaboyena1998/weather_data/-/tree/main)
            
            ```python
            from flask import Flask, request, jsonify
            from flask_restx import Api, Resource, fields
            from sqlalchemy import create_engine
            from sqlalchemy.orm import sessionmaker
            from data_ingest import WeatherRecord, WeatherStats, Base
            
            app = Flask(__name__)
            api = Api(app)
            
            # Define the maximum number of items per page
            MAX_ITEMS_PER_PAGE = 50
            
            # Configure database connection
            engine = create_engine("sqlite:///weather_data.db")
            Base.metadata.bind = engine
            DBSession = sessionmaker(bind=engine)
            
            # Define the data models for Swagger documentation
            weather_record_model = api.model(
                "WeatherRecord",
                {
                    "station": fields.String,
                    "date": fields.Date,
                    "max_temp": fields.Float,
                    "min_temp": fields.Float,
                    "precipitation": fields.Float,
                },
            )
            
            weather_stats_model = api.model(
                "WeatherStats",
                {
                    "year": fields.Integer,
                    "station": fields.String,
                    "avg_max_temp": fields.Float,
                    "avg_min_temp": fields.Float,
                    "total_precipitation": fields.Float,
                },
            )
            
            @api.route("/api/weather")
            class WeatherRecords(Resource):
                @api.expect(weather_record_model)
                @api.doc(
                    params={
                        "date": "Filter by date (YYYY-MM-DD)",
                        "station": "Filter by station ID",
                        "page": "Page number",
                        "page_size": "Number of records per page",
                    }
                )
                def get(self):
                    session = DBSession()
                    # Parse query string parameters
                    date = request.args.get("date", None)
                    station = request.args.get("station", None)
                    page = int(request.args.get("page", 1))
                    page_size = int(request.args.get("page_size", 100))
                    # Build query based on query string parameters
                    query = session.query(WeatherRecord)
                    if date:
                        query = query.filter(WeatherRecord.date == date)
                    if station:
                        query = query.filter(WeatherRecord.station == station)
                    query = query.order_by(WeatherRecord.date.asc())
                    query = query.limit(page_size).offset((page - 1) * page_size)
            
                    # Serialize query results and return as JSON
                    results = [row.__dict__ for row in query.all()]
                    results = [
                        {key: value for key, value in row.items() if key != "_sa_instance_state"}
                        for row in results
                    ]
                    session.close()
                    print(results)
                    return jsonify(results)
            
            @api.route("/api/weather/stats")
            class WeatherStat(Resource):
                @api.expect(weather_stats_model)
                @api.doc(
                    params={
                        "year": "Filter by year",
                        "station": "Filter by station ID",
                        "page": "Page number",
                        "page_size": "Number of records per page",
                    }
                )
                def get(self):
                    session = DBSession()
                    # Parse query string parameters
                    year = int(request.args.get("year", 1998))
                    station = request.args.get("station", None)
                    page = int(request.args.get("page", 1))
                    page_size = int(request.args.get("page_size", 100))
            
                    # Build query based on query string parameters
                    query = session.query(WeatherStats)
                    if year:
                        query = query.filter(WeatherStats.year == year)
                    if station:
                        query = query.filter(WeatherStats.station == station)
                    query = query.order_by(WeatherStats.year.asc())
            
                    query = query.limit(page_size).offset((page - 1) * page_size)
            
                    # Serialize query results and return as JSON
                    results = [row.__dict__ for row in query.all()]
                    results = [
                        {key: value for key, value in row.items() if key != "_sa_instance_state"}
                        for row in results
                    ]
                    session.close()
                    return jsonify(results)
            
            # Add Swagger documentation
            api.add_namespace(api.namespace("swagger", description="Swagger UI"))
            
            @api.route("/swagger.json")
            class Swagger(Resource):
                def get(self):
                    return api.as_json()
            
            if __name__ == "__main__":
                app.run(debug=True, port=8080)
            ```
            
    - Django
        
        how you could create a simple API using the Django web framework:
        
        1. Set up your Django project and create a new Django app:
            
            ```bash
            
            $ django-admin startproject myproject
            $ cd myproject
            $ python manage.py startapp api
            ```
            
        2. Install the Django Rest Framework:
            
            ```python
            
            $ pip install djangorestframework
            ```
            
        3. Add 'rest_framework' to your **`INSTALLED_APPS`** in **`settings.py`**:
            
            ```python
            
            INSTALLED_APPS = [    ...    'rest_framework',]
            
            ```
            
        4. Create a serializers.py file in your api app:
            
            ```python
            
            from rest_framework import serializers
            
            class ExampleSerializer(serializers.Serializer):
                name = serializers.CharField(max_length=100)
                email = serializers.EmailField()
            
            ```
            
        5. Create a views.py file in your api app:
            
            ```python
            
            from rest_framework import generics
            from .serializers import ExampleSerializer
            
            class ExampleView(generics.ListCreateAPIView):
                queryset = Example.objects.all()
                serializer_class = ExampleSerializer
            
            ```
            
        6. Create a urls.py file in your api app:
            
            ```python
            
            from django.urls import path
            from .views import ExampleView
            
            urlpatterns = [
                path('example/', ExampleView.as_view(), name='example'),
            ]
            
            ```
            
        7. Add the app's URL patterns to your project's **`urls.py`**:
            
            ```
            
            from django.urls import path, include
            
            urlpatterns = [
                ...
                path('api/', include('api.urls')),
            ]
            
            ```
            
        8. Run the development server:
            
            ```bash
            
            $ python manage.py runserver
            
            ```
            
        
        You should now be able to access the API at **`http://localhost:8000/api/example/`**. The API will allow you to retrieve a list of examples and create new examples.
        
        Note: This is just a basic example to get you started with creating an API using Django and the Django Rest Framework. There are many more features and customization options available, so be sure to check out the Django Rest Framework documentation for more information.
        
- API security
    - API security
        
        API security is the process of protecting APIs from unauthorized access, modification, or degradation of service. API security is important because APIs are becoming increasingly widely used as a means of accessing and exchanging data and services over the internet.
        
        There are several key aspects of API security, including:
        
        1. Authentication: Ensuring that only authorized clients can access the API by verifying the identity of the client. This can be achieved through mechanisms such as API keys, OAuth, or JSON Web Tokens (JWT).
        2. Authorization: Granting access to protected resources based on the client's identity and permissions. This can be achieved by using access control lists (ACLs), role-based access control (RBAC), or attribute-based access control (ABAC).
        3. Data encryption: Protecting sensitive data in transit by encrypting the data before it is transmitted over the network. This can be achieved by using SSL/TLS encryption.
        4. Input validation: Validating the data that is sent to the API to prevent malicious payloads or attacks such as SQL injection or cross-site scripting (XSS).
        5. Rate limiting: Limiting the rate at which clients can access the API to prevent overloading the API and to protect against denial-of-service attacks.
            
            ```python
            from flask import Flask, request
            from functools import wraps
            
            app = Flask(__name__)
            
            def rate_limit(max_per_minute):
                def decorator(func):
                    @wraps(func)
                    def wrapper(*args, **kwargs):
                        client_ip = request.remote_addr
                        limit_key = f"{client_ip}_limit"
                        limit = redis.get(limit_key)
                        if limit and int(limit) >= max_per_minute:
                            return "API rate limit exceeded. Try again in a minute.", 429
                        else:
                            redis.incr(limit_key)
                            redis.expire(limit_key, 60)
                            return func(*args, **kwargs)
                    return wrapper
                return decorator
            
            @app.route("/")
            @rate_limit(max_per_minute=10)
            def index():
                return "Welcome to my API!"
            
            if __name__ == "__main__":
                app.run()
            
            '''
            In this example, the rate_limit function is a decorator that can be applied to any Flask endpoint to limit the number of requests that can be made from the same client IP address. The max_per_minute argument specifies the maximum number of requests that can be made within a one-minute period.
            
            The rate_limit function uses the remote_addr attribute of the request object to get the client's IP address, and it uses the Redis database to store and retrieve the current rate limit for each client. If the client's rate limit has been exceeded, the function returns an error message and a HTTP status code of 429 (Too Many Requests).
            
            This is a simple example of how rate limiting can be implemented in Python using the Flask framework and Redis. In a real-world implementation, you would likely want to use a more robust and scalable solution, such as an API gateway that provides built-in rate limiting functionality.
            '''
            ```
            
        6. Monitoring and logging: Monitoring API usage and logging API requests and responses to detect and respond to security incidents.
        
        These are some of the key aspects of API security, and the specific security measures that are used will depend on the specific requirements and context of the API. Implementing effective API security requires a comprehensive and proactive approach that covers all aspects of API security, from design to deployment and ongoing maintenance.
        
    - Defining API with User name/ password and authentication token
        
        ```python
        from flask import Flask, request, jsonify
        from werkzeug.security import generate_password_hash, check_password_hash
        
        app = Flask(__name__)
        
        # define a list to store the users
        users = [
            {"username": "user1", "password_hash": generate_password_hash("password1")},
            {"username": "user2", "password_hash": generate_password_hash("password2")}
        ]
        
        @app.route("/api/v1/authenticate", methods=["POST"])
        def authenticate():
            username = request.json.get("username")
            password = request.json.get("password")
        
            user = [user for user in users if user["username"] == username]
        
            if not user:
                return "User not found", 404
        
            user = user[0]
        
            if not check_password_hash(user["password_hash"], password):
                return "Incorrect password", 401
        
            # return a token if the user is authenticated
            return jsonify({"token": "abcdefghijklmnopqrstuvwxyz"})
        
        @app.route("/api/v1/data", methods=["GET"])
        def get_data():
            # check if the user is authenticated by checking the presence of the token in the headers
            if "Authorization" not in request.headers:
                return "Authorization header is missing", 401
        
            token = request.headers["Authorization"]
        
            # validate the token by checking if it matches the one returned by the authentication endpoint
            if token != "abcdefghijklmnopqrstuvwxyz":
                return "Invalid token", 401
        
            # return the data if the user is authenticated
            return jsonify({"data": "Here's some data"})
        
        if __name__ == "__main__":
            app.run(debug=True)
        
        '''
        In this example, we have defined two endpoints: /api/v1/authenticate and /api/v1/data. The /api/v1/authenticate endpoint is used to authenticate the user by verifying their username and password. The password is hashed using the generate_password_hash function from the werkzeug.security module. The check_password_hash function is used to compare the hashed password with the one provided by the user. If the authentication is successful, a token is returned.
        
        The /api/v1/data endpoint is used to retrieve some data. Before returning the data, the API checks if the user is authenticated by checking the presence of the Authorization header in the request and the value of the token. If the token is not present or invalid, the API returns an error message.
        
        '''
        ```
        
    - Difference between Authentication and bearer token
        
        Authentication tokens and bearer tokens are related but distinct concepts in the context of API security.
        
        An authentication token is a string of characters that is generated by the server and sent to the client after the client has provided valid credentials. The client then uses the authentication token in subsequent requests to prove its identity and gain access to protected resources.
        
        A bearer token, on the other hand, is a type of authentication token that is used to grant access to protected resources. Bearer tokens are usually sent as an HTTP header in a request and are used to authenticate the client. The client simply presents the bearer token to the server, and the server grants access to protected resources if the bearer token is valid.
        
        The key difference between an authentication token and a bearer token is the way in which they are used to authenticate the client. Authentication tokens are typically used to authenticate the client and prove its identity, while bearer tokens are used to grant access to protected resources.
        
        In summary, a bearer token is a type of authentication token that is used to grant access to protected resources, while an authentication token is a string of characters that is generated by the server and used to prove the client's identity.
        
- Accessing APIs
    
    
- API Design