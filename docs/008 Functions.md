# Functions

- Defining a function and calling
    
    Defining a function in Python is done using the **`def`** keyword, followed by the name of the function, a set of parentheses **`()`** containing any input parameters the function should accept, and a colon **`:`** to indicate the start of the function body. The code within the function body should be indented, and is executed whenever the function is called. Here's an example function that takes two arguments and returns their sum
    
    ```python
    def add_numbers(a, b):
        result = a + b
        return result
    
    #calling a function 
    sum = add_numbers(3, 4)
    print(sum)  # Output: 7
    ```
    
- Properties of Function
    1. **Encapsulation**: Functions allow you to encapsulate a block of code and give it a name, making your code more organized and readable.
        
        ```python
        def calculate_area(length, width):
            area = length * width
            return area
        
        # Call the function to calculate the area
        rectangle_area = calculate_area(10, 20)
        print("Area of the rectangle is:", rectangle_area)
        ```
        
    2. **Reusability**: Functions can be called multiple times from different parts of your code, allowing you to reuse code and avoid redundant code.
        
        ```python
        rectangle1_area = calculate_area(10, 20)
        rectangle2_area = calculate_area(15, 25)
        
        print("Area of Rectangle 1 is:", rectangle1_area)
        print("Area of Rectangle 2 is:", rectangle2_area)
        ```
        
    3. **Abstraction**: Functions can hide the underlying details of a process, allowing you to provide a simple interface that can be used by others without requiring them to understand the underlying implementation.
        
        ```python
        '''
        Consider the following example, where a function named calculate_interest is defined to calculate the interest on a given amount of money. The details of how the interest is calculated are hidden from the user:
        '''
        def calculate_interest(principal, rate, years):
            interest = principal * rate * years
            return interest
        
        # Call the function to calculate interest
        interest = calculate_interest(10000, 0.05, 2)
        print("Interest amount is:", interest)
        ```
        
    4. **Modularity**: Functions enable you to break down a large problem into smaller, more manageable parts, making it easier to develop and maintain your code.
        
        ```python
        def calculate_square_root(number):
            return number ** 0.5
        
        def calculate_square(number):
            return number ** 2
        
        def calculate_result(number):
            square = calculate_square(number)
            square_root = calculate_square_root(number)
            result = square + square_root
            return result
        
        # Call the main function to calculate the result
        result = calculate_result(10)
        print("Result:", result)
        ```
        
    5. **Input and Output**: Functions can accept input in the form of arguments and return output in the form of return values.
        
        ```python
        def add_numbers(a, b):
            result = a + b
            return result
        
        # Call the function and print the result
        sum = add_numbers(3, 4)
        print("Sum:", sum)
        ```
        
    6. **Scope**: Variables defined within a function are local to the function and cannot be accessed from outside the function, unless they are explicitly passed as arguments or returned as outputs.
        
        ```python
        def calculate_area(length, width):
            area = length * width
            return area
        
        # Try to access the variable 'area' outside the function
        try:
            print(area)
        except NameError:
            print("Variable 'area' is not defined outside the function.")
        ```
        
    7. **Lazy Evaluation**: Functions are only executed when they are called, allowing you to delay the execution of code until it is actually needed.
        
        ```python
        def print_message():
            print("Hello World!")
        
        # Function is not executed yet
        
        # Call the function to execute it
        print_message()
        # Output: Hello World!
        ```
        
    8. **Error handling**: Functions can be designed to handle errors, making it easier to catch and debug problems in your code.
        
        ```python
        def divide(a, b):
            try:
                result = a / b
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
                result = None
            return result
        
        # Call the function and catch the error
        result = divide(10, 0)
        if result is None:
            print("The result is not defined.")
        else:
            print("Result:", result)
        # Output: Error: Cannot divide by zero.
        #         The result is not defined.
        ```
        
- Categories of Functions
    1. Built-in functions: These are the functions that come pre-installed with Python and can be used without importing any modules. Examples include print(), len(), max(), min(), etc.
    2. User-defined functions: These are the functions that are defined by the user and can be used to perform custom tasks.
        
        ```python
        def calculate_area(length, width):
            area = length * width
            return area
        
        # Call the function to calculate the area
        rectangle_area = calculate_area(10, 20)
        print("Area of the rectangle is:", rectangle_area)
        ```
        
    3. Anonymous functions or Lambda functions: These are small, single-line functions that do not have a name. They are also called “lambda functions”.
        
        ```python
        double = lambda x: x * 2
        print(double(5)) # Output: 10
        ```
        
    4. Higher-order functions: These are functions that accept other functions as arguments or return functions as output.
        
        ```python
        def apply_operation(func, x):
            return func(x)
        
        double = lambda x: x * 2
        result = apply_operation(double, 5)
        print(result) # Output: 10
        ```
        
    5. Recursive functions: These are functions that call themselves until a certain condition is met.
        
        ```python
        def factorial(n):
            if n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        
        result = factorial(5)
        print(result) # Output: 120
        ```
        
    6. Generator functions: These are functions that return a generator object, allowing you to iterate over a series of values.
        
        ```python
        def fibonacci_series(n):
            a, b = 0, 1
            for i in range(n):
                yield a
                a, b = b, a + b
        
        for number in fibonacci_series(5):
            print(number)
        # Output: 0
        #         1
        #         1
        #         2
        #         3
        
        def split_df(df, n):
            for i in range(0, df.shape[0], n):
                yield df[i:i + n]
                
        for batch in split_df(csv_data[cols][:50], batch_size):
            pass
        
        ```
        
    7. A nested function is a function that is defined inside another function. Nested functions are also known as inner function
        
        ```python
        def outer_function(x):
            def inner_function(y):
                return x + y
            return inner_function
        
        add_10 = outer_function(10)
        result = add_10(5)
        print(result) # Output: 15
        ```
        
    8. Decorators: These are special functions that can be used to modify the behavior of another function.
        
        ```python
        def uppercase(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return result.upper()
            return wrapper
        
        @uppercase
        def greet(name):
            return "Hello " + name
        
        print(greet("Rajesh")) # Output: HELLO RAJESH
        ```
        
- Argument types
    
    functions can take different types of arguments. Here are some of the common argument types and examples:
    
    1. **Positional arguments**: These are the most common type of arguments and are passed to a function in the same order as they are defined. Example:
        
        ```python
        
        def greet(name, age):
            print("Hello " + name + ", you are " + str(age) + " years old.")
        
        greet("John", 30) # Output: Hello John, you are 30 years old.
        ```
        
    2. **Keyword arguments**: These arguments are passed to a function using the name of the argument and its value. Example:
        
        ```python
        
        def greet(name, age):
            print("Hello " + name + ", you are " + str(age) + " years old.")
        
        greet(age=30, name="John") # Output: Hello John, you are 30 years old.
        ```
        
    3. **Default arguments**: These are arguments that have a default value specified in the function definition. If a value for the argument is not provided, the default value will be used. Example:
        
        ```python
        
        def greet(name, age=18):
            print("Hello " + name + ", you are " + str(age) + " years old.")
        
        greet("John") # Output: Hello John, you are 18 years old.
        ```
        
    4. **Variable-length arguments**: These are arguments that can take any number of values. There are two types of variable-length arguments:
        - **`args`**: This syntax is used to pass a variable number of positional arguments to a function. Example:
            
            ```python
            
            def greet(*names):
                for name in names:
                    print("Hello " + name)
            
            greet("John", "Jane", "Jim")
            # Output: Hello John
            #         Hello Jane
            #         Hello Jim
            ```
            
        - **`*kwargs`**: This syntax is used to pass a variable number of keyword arguments to a function. Example:
            
            ```python
            def greet(**details):
                for key, value in details.items():
                    print(key + ": " + value)
            
            greet(name="John", age=30, country="USA")
            # Output: name: John
            #         age: 30
            #         country: USA
            ```
            
    
    It's possible to use a combination of different argument types in a function. For example, you can have a function that takes positional arguments, default arguments, and variable-length arguments. However, it's important to keep in mind that positional arguments should always come first, followed by default arguments, and then variable-length arguments.
    
- Variables scope
    
    the term "scope" refers to the part of a program where a variable is accessible. In Python, there are two types of scope: global scope and local scope.
    
    1. **Global scope**: A variable declared in the global scope is accessible from anywhere in the program. A global variable is declared outside of all functions. Example:
        
        ```python
        x = 10 # global variable
        
        def print_x():
            print(x)
        
        print_x() # Output: 10
        ```
        
    2. **Local scope**: A variable declared inside a function is accessible only within that function. It is referred to as a local variable. Example:
        
        ```python
        def print_x():
            x = 20 # local variable
            print(x)
        
        print_x() # Output: 20
        print(x) # Raises a NameError: name 'x' is not defined
        ```
        
    
    If a variable with the same name is declared both in the global scope and in a local scope, the local variable will take precedence and will hide the global variable within the function. To access the global variable from within the function, you need to use the **`global`** keyword. Example:
    
    ```python
    x = 10 # global variable
    
    def modify_x():
        global x
        x = 20
    
    modify_x()
    print(x) # Output: 20
    ```
    
    It's generally a good practice to avoid using global variables, as it can make the code harder to understand and maintain. Instead, you can pass variables to a function as arguments or return values from a function to pass the result to the calling code.
    
- Call by value and Call by Reference
    
    the terms "call by value" and "call by reference" describe two different ways in which arguments are passed to a function.
    
    1. **Call by value**: In call by value, a copy of the argument's value is passed to the function. If the function modifies the argument, the changes will not be reflected in the calling code. This is because the function is operating on a copy of the argument, not the original value. Example:
        
        ```python
        def increment(x):
            x += 1
        
        a = 10
        increment(a)
        print(a) # Output: 10
        ```
        
        In Python, all basic data types (such as numbers, strings, and tuples) are passed to functions using call by value.
        
    2. **Call by reference**: In call by reference, a reference to the argument is passed to the function. This means that if the function modifies the argument, the changes will be reflected in the calling code. Example:
        
        ```python
        def increment(x):
            x[0] += 1
        
        a = [10]
        increment(a)
        print(a) # Output: [11]
        ```
        
        In Python, data structures such as lists, dictionaries, and objects are passed to functions using call by reference.
        
    
    It's important to understand the difference between call by value and call by reference in order to write correct and efficient code. When passing an argument to a function, you need to be aware of whether the argument is being passed by value or by reference, as this will affect how the function can modify the argument and what changes will be visible to the calling code.
    
- Passing collections to function
    
    collections such as lists, dictionaries, and sets can be passed as arguments to a function. When passing a collection to a function, it's important to understand whether the collection is being passed by value or by reference.
    
    1. **Passing lists to a function**: In Python, lists are passed by reference. This means that if a function modifies a list argument, the changes will be reflected in the calling code. Example:
        
        ```python
        def modify_list(lst):
            lst[0] = 100
        
        a = [1, 2, 3]
        modify_list(a)
        print(a) # Output: [100, 2, 3]
        ```
        
    2. **Passing dictionaries to a function**: Like lists, dictionaries are also passed by reference in Python. This means that if a function modifies a dictionary argument, the changes will be reflected in the calling code. Example:
        
        ```python
        
        def modify_dict(dct):
            dct['a'] = 100
        
        a = {'a': 1, 'b': 2}
        modify_dict(a)
        print(a) # Output: {'a': 100, 'b': 2}
        ```
        
    3. **Passing sets to a function**: Sets, like lists and dictionaries, are passed by reference in Python. This means that if a function modifies a set argument, the changes will be reflected in the calling code. Example:
        
        ```python
        def modify_set(st):
            st.add(100)
        
        a = {1, 2, 3}
        modify_set(a)
        print(a) # Output: {1, 2, 3, 100}
        ```
        
    
    When passing a collection to a function, it's important to understand whether the collection is being passed by reference or by value, as this will affect what changes the function can make to the collection and what changes will be visible to the calling code.
    
- Boolean Function
    
    A boolean function is a function that returns a Boolean value, either **`True`** or **`False`**. In Python, a boolean function can be defined using the **`def`** keyword, just like any other function.
    
    Here's an example of a simple boolean function that returns **`True`** if a given number is even, and **`False`** otherwise:
    
    ```python
    def is_even(number):
        return number % 2 == 0
    
    print(is_even(2)) # Output: True
    print(is_even(3)) # Output: False
    ```
    
    Boolean functions can be used in various ways, such as in conditional statements and control structures. For example, you can use a boolean function to determine whether a certain condition is met, and take different actions based on the result:
    
    ```python
    def is_positive(number):
        return number > 0
    
    if is_positive(5):
        print("The number is positive")
    else:
        print("The number is not positive")
    ```
    
    Boolean functions can also be used to filter elements from a list or other collection. For example, you can use a boolean function to create a new list that only contains the elements that satisfy a certain condition:
    
    ```python
    def is_odd(number):
        return number % 2 != 0
    
    numbers = [1, 2, 3, 4, 5]
    odd_numbers = [x for x in numbers if is_odd(x)]
    print(odd_numbers) # Output: [1, 3, 5]
    ```
    
    Boolean functions are a useful tool for expressing and testing conditions in your code, and can help make your code more readable and maintainable.
    
- Filter() and map() functions
    
    the **`filter()`** and **`map()`** functions are two built-in functions that can be used to process and manipulate lists and other iterable objects.
    
    1. **The `filter()` function**: The **`filter()`** function takes two arguments: a function and an iterable. The function is applied to each element in the iterable, and the elements for which the function returns **`True`** are included in the output. The **`filter()`** function returns an object that can be converted to a list or other data type if needed.
        
        Here's an example of using the **`filter()`** function to extract all even numbers from a list:
        
        ```python
        def is_even(x):
            return x % 2 == 0
        
        numbers = [1, 2, 3, 4, 5]
        even_numbers = list(filter(is_even, numbers))
        print(even_numbers) # Output: [2, 4]
        ```
        
    2. **The `map()` function**: The **`map()`** function takes two arguments: a function and an iterable. The function is applied to each element in the iterable, and the result is a new iterable containing the results of the function applied to each element. The **`map()`** function returns a map object that can be converted to a list or other data type if needed.
        
        Here's an example of using the **`map()`** function to square each element in a list:
        
        ```python
        def square(x):
            return x * x
        
        numbers = [1, 2, 3, 4, 5]
        squared_numbers = list(map(square, numbers))
        print(squared_numbers) # Output: [1, 4, 9, 16, 25]
        ```
        
        In Python, the **`filter()`** and **`map()`** functions are often used with lambda expressions, which are anonymous functions that can be created on the fly. For example, here's an equivalent version of the **`filter()`** example above using a lambda expression:
        
        ```python
        numbers = [1, 2, 3, 4, 5]
        even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
        print(even_numbers) # Output: [2, 4]
        ```
        
    
    The **`filter()`** and **`map()`** functions are powerful tools for processing and transforming lists and other iterable objects. They can be used to simplify your code, make it more readable, and improve performance by avoiding the use of for loops and other control structures.
    
- Reduce Function
    
    The **`reduce()`** function is a built-in function in Python that is part of the **`functools`** module. The **`reduce()`** function takes two arguments: a function and an iterable. The function is applied to the first two elements of the iterable, and then the result is combined with the next element, and so on, until all elements have been processed. The result of the final combination is returned.
    
    Here's an example of using the **`reduce()`** function to find the product of all numbers in a list:
    
    ```python
    from functools import reduce
    
    def multiply(x, y):
        return x * y
    
    numbers = [1, 2, 3, 4, 5]
    product = reduce(multiply, numbers)
    print(product) # Output: 120
    ```
    
    In this example, the **`multiply`** function is applied to the first two elements of the **`numbers`** list, which are 1 and 2, to produce the result 2. The result 2 is then combined with the next element 3, to produce 6. This process continues until all elements have been processed. The final result, which is 120, is returned by the **`reduce()`** function.
    
    The **`reduce()`** function can be used to perform a wide range of operations, such as finding the sum or product of a list of numbers, concatenating strings, or computing the factorial of a number. It is a useful tool for processing and reducing data, and can help simplify your code and make it more readable.
    
    Keep in mind that the **`reduce()`** function is not part of the core Python library, so you need to import it from the **`functools`** module before you can use it. Additionally, the **`reduce()`** function is not as commonly used as other functions such as **`map()`** and **`filter()`**, so it may not be immediately familiar to some Python programmers. However, it can be a powerful tool when you need to perform complex data processing tasks.
