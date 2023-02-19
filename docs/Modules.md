# Modules

- What is a module?
    
    A module in Python is a single file that contains Python code, such as variables, functions, and classes. The purpose of a module is to organize code into reusable, self-contained units. A module can be imported into other Python scripts or modules to make the code it contains available for use in those scripts or modules. This allows you to reuse code across multiple projects, and to organize complex projects into smaller, more manageable components.
    
    Modules are typically stored in files with a **`.py`** extension, and can be imported using the **`import`** statement. For example, if you have a module named **`mymodule`** stored in a file named **`mymodule.py`**, you can import it into another Python script as follows:
    
    ```python
    import mymodule
    ```
    
    Once the module is imported, you can access the variables, functions, and classes it contains using the module name as a prefix. For example, if the module **`mymodule`** contains a function named **`myfunction`**, you can call it as follows:
    
    ```python
    mymodule.myfunction()
    ```
    
    Modules are a fundamental part of Python and are used to organize and reuse code in a modular and reusable way. By breaking your code into modules, you can write more readable and maintainable code, and make it easier to reuse code across multiple projects.
    
- Different types of module
    1. Built-in modules: These are modules that are included with the standard Python distribution. Examples of built-in modules include **`os`**, **`sys`**, **`math`**, and **`random`**. These modules provide a wide range of functionality, from accessing the operating system to performing mathematical operations and generating random numbers.
    2. User-defined modules: These are modules that you create yourself, using your own code. User-defined modules can be imported into other Python scripts and modules just like built-in modules. This allows you to organize and reuse your own code in a modular and reusable way.
    
    Additionally, there are other types of modules, such as third-party modules, which are modules that are created and maintained by other individuals or organizations and can be installed using tools like pip. These modules can provide additional functionality that is not included in the standard Python distribution.
    
    In summary, there are several types of modules in Python, including built-in modules, user-defined modules, and third-party modules, each of which can provide different types of functionality for your Python programs.
    
- Creating user defined module
    
    A user-defined module in Python can be created by writing your own Python code in a file with a **`.py`** extension. The code in the file can include variables, functions, and classes, just like in any other Python script.
    
    Here's an example of a simple user-defined module:
    
    ```python
    # mymodule.py
    
    def say_hello():
        print("Hello from mymodule!")
    
    def say_goodbye():
        print("Goodbye from mymodule!")
    ```
    
    Once you have created the module, you can import it into other Python scripts or modules using the **`import`** statement. For example:
    
    ```python
    import mymodule
    mymodule.say_hello()
    mymodule.say_goodbye()
    ```
    
    When you run this code, you will see the following output:
    
    ```python
    Hello from mymodule!
    Goodbye from mymodule!
    ```
    
    In this way, you can create your own modules to organize and reuse your own code in a modular and reusable way. This can help you write more readable and maintainable code, and make it easier to reuse code across multiple projects.
    
- Setting path
    
    The **`PYTHONPATH`** environment variable can be used to set the search path for Python modules, which determines the directories in which Python will look for modules when you use the **`import`** statement.
    
    You can set the **`PYTHONPATH`** environment variable in the following ways:
    
    1. In Windows, you can set the **`PYTHONPATH`** environment variable from the Command Prompt or from the System Properties window.
        
        To set it from the Command Prompt, enter the following command:
        
        ```python
        setx PYTHONPATH "directory_path1;directory_path2;..."
        ```
        
        To set it from the System Properties window, follow these steps:
        
        - Right-click on the Computer icon on the desktop, and select Properties.
        - Select Advanced system settings.
        - In the System Properties window, select the Advanced tab.
        - Click on the Environment Variables button.
        - In the Environment Variables window, under System Variables, scroll down and find the PYTHONPATH variable.
        - Select the PYTHONPATH variable, and click the Edit button.
        - Add the directory paths to the PYTHONPATH variable, separated by semicolons.
    2. In Unix and Linux, you can set the **`PYTHONPATH`** environment variable in your shell profile file, such as **`.bashrc`** or **`.bash_profile`**. You can add the following lines to your shell profile file:
        
        ```python
        export PYTHONPATH="directory_path1:directory_path2:..."
        ```
        
        After setting the **`PYTHONPATH`** environment variable, you need to restart your shell or restart your computer for the changes to take effect.
        
        By setting the **`PYTHONPATH`** environment variable, you can specify the directories in which Python will look for modules, making it easier to import and use your own modules or third-party modules that are not installed in the standard Python library.
        
- From … import
    
    The **`from ... import`** statement in Python is used to import specific elements (e.g. functions, classes, or variables) from a module into the current namespace. This allows you to use the imported elements directly, without having to qualify them with the module name.
    
    Here's an example that demonstrates how to use the **`from ... import`** statement:
    
    ```python
    
    # mymodule.py
    
    def say_hello():
        print("Hello from mymodule!")
    
    def say_goodbye():
        print("Goodbye from mymodule!")
    
    # main.py
    
    from mymodule import say_hello
    
    say_hello()
    ```
    
    When you run this code, you will see the following output:
    
    ```python
    Hello from mymodule!
    ```
    
    Note that, with the **`from ... import`** statement, you can import only specific elements from a module, whereas with the **`import`** statement, you import the entire module into the current namespace. The **`from ... import`** statement is useful when you only need to use a few elements from a module, as it makes your code more concise and readable.
    
    However, it's important to use the **`from ... import`** statement with caution, as it can lead to naming conflicts if you import elements with the same names as elements already in the current namespace. In such cases, it's best to use the **`import`** statement and qualify the imported elements with the module name.
    
- Module Aliases
    
    In Python, you can use module aliases to give a module a different name in your code. This can be useful when you want to import a module with a long or difficult-to-remember name, or when you want to avoid naming conflicts with other modules that have the same name.
    
    Here's an example that demonstrates how to use module aliases:
    
    ```python
    import mymodule as mm
    
    mm.say_hello()
    ```
    
    In this example, the **`import`** statement creates an alias **`mm`** for the **`mymodule`** module. This means that you can use the **`mm`** alias to access the functions and variables in the **`mymodule`** module, instead of using the full name **`mymodule`**.
    
    You can use any name as a module alias, as long as it's a valid Python identifier. Just replace the **`as`** keyword with the name you want to use as the alias, like this:
    
    ```python
    import mymodule as my_module
    
    my_module.say_hello()
    ```
    
    Using module aliases can make your code more readable and easier to maintain, as it allows you to use short and descriptive names for your modules.
    
- Reloading a module
    
    In Python, you can use the **`reload`** function from the **`importlib`** module to reload a module that has already been imported. This can be useful when you're developing and testing a module, as it allows you to make changes to the module and see the results of those changes without having to restart your program.
    
    Here's an example that demonstrates how to reload a module:
    
    ```python
    import mymodule
    
    mymodule.say_hello()
    
    # change mymodule.py
    
    # reload mymodule
    import importlib
    importlib.reload(mymodule)
    
    mymodule.say_hello()
    ```
    
    In this example, the **`mymodule`** module is imported and its **`say_hello`** function is called. Then, the contents of **`mymodule.py`** are changed, and the **`mymodule`** module is reloaded using the **`reload`** function from the **`importlib`** module. Finally, the **`say_hello`** function is called again, and you can see that the changes to the **`mymodule`** module have taken effect.
    
    Note that the **`reload`** function is only available in Python 3, and it only works on modules that have been imported using the **`import`** statement. If you use the **`from ... import`** statement to import specific elements from a module, you cannot reload those elements using the **`reload`** function.
    
- Dir function
    
    The **`dir`** function in Python is a built-in function that returns a list of all the names defined in a given object. This includes all the attributes (such as functions, variables, and modules) and methods (functions that are associated with an object) of an object.
    
    For example, you can use the **`dir`** function to inspect the attributes of a module:
    
    ```python
    import math
    
    print(dir(math))
    
    '''
    output:
    ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
    '''
    
    #return only functions
    functions = [func for func in dir(math) if callable(getattr(math, func))]
    
    print(functions)
    
    ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nextafter', 'perm', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc', 'ulp']
    ```
    
    This will print a list of all the names defined in the **`math`** module, including functions such as **`sqrt`**, **`cos`**, and **`sin`**, and constants such as **`pi`** and **`e`**.
    
    You can also use the **`dir`** function to inspect the attributes of an object, such as a list or a string:
    
    ```python
    my_list = [1, 2, 3]
    
    print(dir(my_list))
    '''
    ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    '''
    
    my_string = "hello, world"
    
    print(dir(my_string))
    '''
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    '''
    ```
    
    This will print a list of all the methods and attributes associated with the list and string objects, including methods such as **`append`** and **`count`**, and attributes such as **`reverse`** and **`capitalize`**.
    
    Note that the **`dir`** function only returns the names of the attributes and methods of an object, not their values. To see the values of an object's attributes, you need to use the dot (**`.`**) operator to access them directly.
    
- Standard Modules
    - math
        
        The **`math`** module is a built-in module in Python that provides access to a wide range of mathematical functions and constants. To use the **`math`** module, you first need to import it using the **`import`** statement:
        
        ```python
        import math
        ```
        
        Here are some of the commonly used functions and constants in the **`math`** module:
        
        ### **Functions**
        
        - **`math.ceil(x)`**: Returns the smallest integer greater than or equal to **`x`**.
        - **`math.floor(x)`**: Returns the largest integer less than or equal to **`x`**.
        - **`math.sqrt(x)`**: Returns the square root of **`x`**.
        - **`math.pow(x, y)`**: Returns **`x`** raised to the power of **`y`**.
        - **`math.exp(x)`**: Returns the exponential of **`x`** (e^x).
        - **`math.log(x)`**: Returns the natural logarithm of **`x`**.
        - **`math.sin(x)`**, **`math.cos(x)`**, **`math.tan(x)`**: Returns the sine, cosine, and tangent of **`x`**.
        - **`math.asin(x)`**, **`math.acos(x)`**, **`math.atan(x)`**: Returns the inverse sine, cosine, and tangent of **`x`**.
        - **`math.degrees(x)`**: Converts radians to degrees.
        - **`math.radians(x)`**: Converts degrees to radians.
            
            ```python
            import math
            
            # ceil function
            x = 4.3
            print(math.ceil(x))  # Output: 5
            
            # floor function
            x = 4.9
            print(math.floor(x))  # Output: 4
            
            # square root function
            x = 16
            print(math.sqrt(x))  # Output: 4.0
            
            # power function
            x = 2
            y = 3
            print(math.pow(x, y))  # Output: 8.0
            
            # exponential function
            x = 2
            print(math.exp(x))  # Output: 7.3890560989306495
            
            # logarithm function
            x = 10
            print(math.log(x))  # Output: 2.302585092994046
            
            # trigonometric functions
            x = math.pi / 4
            print(math.sin(x))  # Output: 0.7071067811865475
            print(math.cos(x))  # Output: 0.7071067811865476
            print(math.tan(x))  # Output: 0.9999999999999999
            
            # inverse trigonometric functions
            x = 0.7071067811865476
            print(math.asin(x))  # Output: 0.7853981633974484
            print(math.acos(x))  # Output: 0.7853981633974483
            print(math.atan(x))  # Output: 0.6154797086703874
            
            # degree and radian conversion
            x = 45
            print(math.radians(x))  # Output: 0.7853981633974483
            print(math.degrees(x))  # Output: 2578.3100780887044
            
            # constants
            print(math.pi)  # Output: 3.141592653589793
            print(math.e)  # Output: 2.718281828459045
            ```
            
        
        ### **Constants**
        
        - **`math.pi`**: The mathematical constant pi (3.141592...).
        - **`math.e`**: The mathematical constant e (2.718281...).
            
            ```python
            import math
            
            radius = 2
            circumference = 2 * math.pi * radius
            print(circumference)  # Output: 12.566370614359172
            ```
            
    - data and time
        - Date &DateTime Class
            
            In Python, the **`datetime`**module provides classes for working with dates and times. The **`date`**class represents a date, and the **`datetime`**class represents a date and time.
            
            ****Using the `date` Class**
            
            ```python
            from datetime import date
            
            # create a date object
            d = date(2022, 2, 19)
            print(d)  # Output: 2022-02-19
            
            # get today's date
            today = date.today()
            print(today)  # Output: the current date in YYYY-MM-DD format
            
            # format a date as a string
            formatted_date = d.strftime("%d-%m-%Y")
            print(formatted_date)  # Output: 19-02-2022
            
            # get the year, month, and day of a date
            year = d.year
            month = d.month
            day = d.day
            print(year, month, day)  # Output: 2022 2 19
            
            # get the weekday of a date (Monday is 0 and Sunday is 6)
            weekday = d.weekday()
            print(weekday)  # Output: 5 (Saturday)
            
            # create a new date object by replacing the year, month, or day
            new_date = d.replace(year=2023)
            print(new_date)  # Output: 2023-02-19
            ```
            
            ****Using the `datetime` Class**
            
            ```python
            from datetime import datetime
            
            # create a datetime object
            dt = datetime(2022, 2, 19, 12, 30, 0, 0)
            print(dt)  # Output: 2022-02-19 12:30:00
            
            # get the current datetime
            now = datetime.now()
            print(now)  # Output: the current datetime in YYYY-MM-DD HH:MM:SS.mmmmmm format
            
            # format a datetime as a string
            formatted_dt = dt.strftime("%d-%m-%Y %H:%M:%S")
            print(formatted_dt)  # Output: 19-02-2022 12:30:00
            
            # get the year, month, day, hour, minute, second, and microsecond of a datetime
            year = dt.year
            month = dt.month
            day = dt.day
            hour = dt.hour
            minute = dt.minute
            second = dt.second
            microsecond = dt.microsecond
            print(year, month, day, hour, minute, second, microsecond)  # Output: 2022 2 19 12 30 0 0
            
            # get the weekday of a datetime (Monday is 0 and Sunday is 6)
            weekday = dt.weekday()
            print(weekday)  # Output: 5 (Saturday)
            
            # create a new datetime object by replacing the year, month, day, hour, minute, second, or microsecond
            new_dt = dt.replace(year=2023)
            print(new_dt)  # Output: 2023-02-19 12:30:00
            ```
            
        - Time and date Objects
            
             The **`datetime`** module provides classes for working with dates and times, including the **`date`**, **`time`**, and **`datetime`** classes. These classes allow you to perform arithmetic operations on dates and times, format them as strings, and convert them between different time zones.
            
            ```python
            import time
            from datetime import datetime, date, time
            
            # measure the time elapsed between two points
            start_time = time.time()
            # some time-consuming operation here
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            
            # get the current date and time
            now = datetime.now()
            print(f"Current date and time: {now}")
            
            # create a date object
            d = date(2022, 2, 19)
            print(f"Date: {d}")
            
            # create a time object
            t = time(12, 30, 0)
            print(f"Time: {t}")
            
            # create a datetime object
            dt = datetime(2022, 2, 19, 12, 30, 0)
            print(f"Datetime: {dt}")
            
            # format a date, time, or datetime object as a string
            formatted_date = d.strftime("%d-%m-%Y")
            formatted_time = t.strftime("%H:%M:%S")
            formatted_datetime = dt.strftime("%d-%m-%Y %H:%M:%S")
            print(f"Formatted date: {formatted_date}")
            print(f"Formatted time: {formatted_time}")
            print(f"Formatted datetime: {formatted_datetime}")
            
            # convert a string to a date, time, or datetime object
            date_string = "19-02-2022"
            time_string = "12:30:00"
            datetime_string = "19-02-2022 12:30:00"
            parsed_date = datetime.strptime(date_string, "%d-%m-%Y").date()
            parsed_time = datetime.strptime(time_string, "%H:%M:%S").time()
            parsed_datetime = datetime.strptime(datetime_string, "%d-%m-%Y %H:%M:%S")
            print(f"Parsed date: {parsed_date}")
            print(f"Parsed time: {parsed_time}")
            print(f"Parsed datetime: {parsed_datetime}")
            ```
            
        - Calendar in Python
            
            the **`calendar`** module provides several functions for working with calendars.
            
            ```python
            import calendar
            
            # print the calendar for a given month and year
            calendar.prmonth(2022, 2)
            
            # determine whether a year is a leap year
            is_leap_year = calendar.isleap(2022)
            print(f"Is 2022 a leap year? {is_leap_year}")
            
            # calculate the number of days in a month
            num_days_in_feb_2022 = calendar.monthrange(2022, 2)[1]
            print(f"Number of days in February 2022: {num_days_in_feb_2022}")
            
            # print the calendar for a given year
            calendar.prcal(2022)
            ```
            
        - The Time Module
            
            The **`time`**module in Python provides various time-related functions.
            
            ```python
            import time
            
            # get the current time in seconds since the epoch
            current_time = time.time()
            print(f"Current time: {current_time}")
            
            # convert a time in seconds since the epoch to a struct_time object
            struct_time = time.localtime(current_time)
            print(f"Local time: {struct_time}")
            
            # format a struct_time object as a string
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
            print(f"Formatted time: {formatted_time}")
            
            # pause the program for a specified number of seconds
            time.sleep(2)
            print("Two seconds have passed.")
            
            # measure the time elapsed between two points
            start_time = time.monotonic()
            # some time-consuming operation here
            end_time = time.monotonic()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            
            # calculate the CPU time used by the current process
            start_cpu_time = time.process_time()
            # some CPU-intensive operation here
            end_cpu_time = time.process_time()
            cpu_time_used = end_cpu_time - start_cpu_time
            print(f"CPU time used: {cpu_time_used:.2f} seconds")
            
            # convert a string representing a time to a struct_time object
            time_string = "2022-02-23 12:34:56"
            struct_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
            print(f"Struct time: {struct_time}")
            
            # convert a struct_time object to a time in seconds since the epoch
            epoch_time = time.mktime(struct_time)
            print(f"Epoch time: {epoch_time}")
            
            # get the current local time as a string
            local_time_string = time.ctime()
            print(f"Local time string: {local_time_string}")
            
            # get the current UTC time as a string
            utc_time_string = time.asctime(time.gmtime())
            print(f"UTC time string: {utc_time_string}")
            ```
            
    - os module
        
        The **`os`** module in Python provides a way to interact with the operating system. It includes functions for performing file and directory operations, process management, and more. Here are some of the commonly used functions in the **`os`** module:
        
        - **`os.name`**: Returns the name of the operating system (e.g. 'posix' or 'nt').
        - **`os.getcwd()`**: Returns the current working directory.
        - **`os.chdir(path)`**: Changes the current working directory to **`path`**.
        - **`os.listdir(path='.')`**: Returns a list of filenames in the directory **`path`**.
        - **`os.mkdir(path[, mode])`**: Creates a directory with the given **`path`** and **`mode`**.
        - **`os.makedirs(path[, mode])`**: Creates a directory and any intermediate directories with the given **`path`** and **`mode`**.
        - **`os.rmdir(path)`**: Removes the directory at the given **`path`**.
        - **`os.removedirs(path)`**: Removes a directory and any intermediate directories with the given **`path`**.
        - **`os.rename(src, dst)`**: Renames a file or directory from **`src`** to **`dst`**.
        - **`os.remove(path)`**: Deletes the file at the given **`path`**.
        - **`os.stat(path)`**: Returns a **`stat_result`** object containing information about the file at the given **`path`**.
        - **`os.environ`**: A dictionary containing the environment variables.
        - **`os.system(command)`**: Runs the command in the system shell.
            
            ```python
            import os
            
            # Get the name of the operating system
            print(os.name)
            
            # Get the current working directory
            print(os.getcwd())
            
            # Change the current working directory
            os.chdir('/path/to/new/dir')
            
            # List the files in the current directory
            print(os.listdir())
            
            # Create a directory
            os.mkdir('new_dir')
            
            # Rename a file
            os.rename('old_file.txt', 'new_file.txt')
            
            # Remove a file
            os.remove('file_to_delete.txt')
            
            # Get information about a file
            file_stat = os.stat('file.txt')
            print('Size:', file_stat.st_size)
            print('Permissions:', oct(file_stat.st_mode))
            
            # Get an environment variable
            print(os.environ.get('HOME'))
            
            # Run a command in the system shell
            os.system('ls -la')
            ```
            
        - shutil module
            
            The **`shutil`** module in Python provides a way to work with files and directories. It includes functions for copying, moving, renaming, and deleting files and directories, as well as archiving and compressing files. Here are some of the commonly used functions in the **`shutil`** module:
            
            - **`shutil.copy(src, dst)`**: Copies the file at **`src`** to **`dst`**.
            - **`shutil.copy2(src, dst)`**: Like **`copy()`**, but also copies the file's metadata.
            - **`shutil.copytree(src, dst[, symlinks=False])`**: Recursively copies the directory tree at **`src`** to **`dst`**.
            - **`shutil.move(src, dst)`**: Moves the file or directory at **`src`** to **`dst`**.
            - **`shutil.rmtree(path[, ignore_errors=False[, onerror=None]])`**: Recursively deletes the directory tree at **`path`**.
            - **`shutil.make_archive(base_name, format[, root_dir=None[, base_dir=None[, verbose=False[, dry_run=False[, owner=None[, group=None[, logger=None]]]]]]])`**: Creates an archive file with the given **`base_name`** and **`format`**.
            - **`shutil.unpack_archive(filename[, extract_dir[, format]])`**: Unpacks the archive file at **`filename`** to **`extract_dir`**.
            - **`shutil.get_archive_formats()`**: Returns a list of supported archive formats.
            - **`shutil.register_archive_format(name, function[, extra_args=None[, description=None]])`**: Registers a new archive format with the given **`name`** and function.
                
                ```python
                import shutil
                
                # Copy a file
                shutil.copy('file1.txt', 'file2.txt')
                
                # Copy a directory tree
                shutil.copytree('dir1', 'dir2')
                
                # Move a file
                shutil.move('file1.txt', 'new_dir/file1.txt')
                
                # Remove a directory tree
                shutil.rmtree('dir1')
                
                # Create a zip archive of a directory tree
                shutil.make_archive('my_archive', 'zip', 'my_directory')
                
                # Extract a zip archive to a directory
                shutil.unpack_archive('my_archive.zip', 'extracted_directory')
                
                # Get a list of supported archive formats
                print(shutil.get_archive_formats())
                ```
                
        - Os
            
            The **`os`** module in Python provides a way to interact with the operating system. It includes functions for working with files and directories, managing processes, and more. Here are some of the commonly used functions in the **`os`** module:
            
            - **`os.getcwd()`**: Returns the current working directory as a string.
            - **`os.chdir(path)`**: Changes the current working directory to the specified **`path`**.
            - **`os.listdir(path='.')`**: Returns a list of files and directories in the specified **`path`**, or the current working directory if **`path`** is not specified.
            - **`os.mkdir(path[, mode])`**: Creates a directory at the specified **`path`**.
            - **`os.makedirs(name[, mode])`**: Recursively creates directories at the specified **`name`**.
            - **`os.rmdir(path)`**: Removes the directory at the specified **`path`**.
            - **`os.removedirs(path)`**: Recursively removes empty directories at the specified **`path`**.
            - **`os.rename(src, dst)`**: Renames the file or directory at **`src`** to **`dst`**.
            - **`os.remove(path)`**: Deletes the file at the specified **`path`**.
            - **`os.path.join(path, *paths)`**: Joins one or more path components together, with the appropriate separator for the current operating system.
            - **`os.path.exists(path)`**: Returns **`True`** if the file or directory at the specified **`path`** exists, otherwise returns **`False`**.
            - **`os.path.isfile(path)`**: Returns **`True`** if the specified **`path`** is a file, otherwise returns **`False`**.
            - **`os.path.isdir(path)`**: Returns **`True`** if the specified **`path`** is a directory, otherwise returns **`False`**.
                
                ```python
                import os
                
                # Get the current working directory
                cwd = os.getcwd()
                print(cwd)
                
                # Change the current working directory
                os.chdir('/path/to/new/directory')
                
                # List the files and directories in the current directory
                files = os.listdir()
                print(files)
                
                # Create a new directory
                os.mkdir('new_directory')
                
                # Rename a file
                os.rename('file1.txt', 'file2.txt')
                
                # Remove a directory and its contents
                os.rmdir('old_directory')
                
                # Check if a file exists
                if os.path.exists('file1.txt'):
                    print('The file exists')
                else:
                    print('The file does not exist')
                ```
                
    - Sys
        
        The **`sys`** module in Python provides access to some variables and functions that interact with the Python interpreter. Here are some of the commonly used functions and variables in the **`sys`** module:
        
        - **`sys.argv`**: A list of command-line arguments passed to the Python script. The first item in the list is the name of the script itself.
        - **`sys.exit([arg])`**: Exit the current Python interpreter with an optional exit code **`arg`**.
        - **`sys.stdin`**: A file-like object that provides input to the Python interpreter. By default, this is the keyboard input.
        - **`sys.stdout`**: A file-like object that represents the standard output stream. By default, this is the console.
        - **`sys.stderr`**: A file-like object that represents the standard error stream. By default, this is also the console.
        - **`sys.path`**: A list of strings that specifies the search path for module files. When a module is imported, Python searches the directories in **`sys.path`** for the module file.
        - **`sys.platform`**: A string that identifies the operating system on which Python is running.
            
            ```python
            import sys
            
            # Get the command-line arguments
            args = sys.argv
            print(args)
            
            # Exit the Python interpreter with an exit code
            sys.exit(1)
            
            # Read input from the user
            input_data = sys.stdin.readline()
            print(input_data)
            
            # Write output to the console
            sys.stdout.write('Hello, world!\n')
            
            # Write error output to the console
            sys.stderr.write('An error occurred\n')
            
            # Get the search path for module files
            search_path = sys.path
            print(search_path)
            
            # Get the operating system
            platform = sys.platform
            print(platform)
            
            '''
            sys.exc_info() is a function in Python's sys module that returns information about the most recent exception that occurred in the current scope. It returns a tuple containing three values:
            
            type: The type of the exception that was raised.
            value: The instance of the exception that was raised.
            traceback: A traceback object that encapsulates the call stack at the point where the exception occurred.
            
            '''
            
            import sys
            
            try:
                # Some code that may raise an exception
                raise ValueError("An error occurred")
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                print(f"Exception type: {exc_type}")
                print(f"Exception value: {exc_value}")
                print("Traceback:")
                traceback_lines = traceback.format_tb(exc_traceback)
                for line in traceback_lines:
                    print(line)
            ```
            
    - random
        
        The **`random`** module in Python provides various functions for generating random numbers and values. Here are some of the commonly used functions in the **`random`** module:
        
        - **`random.random()`**: Returns a random floating-point number between 0 and 1.
        - **`random.randint(a, b)`**: Returns a random integer between **`a`** and **`b`**, inclusive.
        - **`random.choice(seq)`**: Returns a random element from the given sequence **`seq`**.
        - **`random.shuffle(seq)`**: Shuffles the elements of the given sequence **`seq`** in place.
        - **`random.sample(population, k)`**: Returns a new list containing **`k`** unique elements randomly sampled from the given **`population`** sequence.
        
        ```python
        import random
        
        # Generate a random floating-point number between 0 and 1
        print(random.random())
        
        # Generate a random integer between 1 and 10
        print(random.randint(1, 10))
        
        # Choose a random element from a list
        fruits = ["apple", "banana", "cherry", "durian"]
        print(random.choice(fruits))
        
        # Shuffle a list
        random.shuffle(fruits)
        print(fruits)
        
        # Sample 3 unique elements from a list
        sampled = random.sample(fruits, 3)
        print(sampled)
        ```