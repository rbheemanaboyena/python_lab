# Python Operations

- Python modes of Execution
    
    python provides two main modes of execution: script mode (batch mode) and interactive mode
    
- Python Constants
    
    In Python, there is no strict definition of a constant. However, you can create variables that should act as constants by naming them in all uppercase letters, as a convention. This makes it clear that their values should not be changed in your code
    
    ```python
    PI = 3.14159265
    
    GRAVITY = 9.8
    
    MAX_ITEMS = 100
    ```
    
    these "constants" can still be changed if needed in your code. If you want to prevent the values of these variables from being changed, you will need to use other means to enforce this, such as by using object-oriented programming techniques to make the variables private and providing accessor methods that return their values
    
- Comments in python
    
    ```python
    # This is a single line comment
    x = 10 # This is also a single line comment
    
    """
    This is a multi-line comment.
    It can span multiple lines and provide a detailed
    description of the code.
    """
    ```
    
- Unicode
    
    In Python 3, improved Unicode support was a major goal, and many changes were made to the way Unicode characters are handled in the language. Here are some of the key improvements in Unicode support in Python 3:
    
    1. Default Encoding: In Python 2, the default encoding for string data is ASCII, which supports only a limited set of characters. In Python 3, the default encoding is UTF-8, which provides support for the full range of Unicode characters. This means that you can include characters from most written languages in your strings without having to worry about encoding issues.
    2. Text Strings: In Python 2, there are two types of string data: **`str`** for binary data and **`unicode`** for Unicode text. In Python 3, the **`str`** type is used for Unicode text, and a new type, **`bytes`**, is used for binary data. This simplifies the handling of string data, making it easier to work with text strings.
    3. Unicode Strings as Literals: In Python 3, you can include Unicode characters in string literals directly in your code. For example:
    
    In Python 2, you had to specify the **`unicode`** type or use escape sequences to include Unicode characters in string literals.
    
    1. Better Error Handling: In Python 3, better error handling has been added for Unicode encoding and decoding. When decoding binary data as text, for example, Python 3 will raise an exception if an invalid character is encountered, instead of silently replacing the character with a question mark (**`?`**) or a similar placeholder, as was the case in Python 2.
- Output function
    
    By default, the **`print`** function adds a newline character at the end of the text it displays, which causes the text to be displayed on a new line. You can change this behavior by passing the **`end`** argument to the **`print`** function:
    
    ```
    print("Hello, World!", end=""
    ```
    
    This will cause the text to be displayed on the same line without a newline character at the end. You can also specify a different string to be used as the separator between multiple items passed to the **`print`** function, using the **`sep`** argument:
    
    ```
    print("Hello", "World!", sep=", ")
    ```
    
    This will cause the text to be displayed as **`Hello, World!`** with a comma and a space between the two items.
    
- Input function
    
    the **`input`**function always returns a string
    
    ```python
    # Display a prompt and accept input
    name = input("Enter your name: ")
    print("Hello, " + name + "!")
    ```
    
- Type Conversion
    
    ```python
    # Integer to String
    num = 123
    string = str(num)
    print("The string is:", string)
    
    # Float to String
    num = 123.456
    string = str(num)
    print("The string is:", string)
    
    # String to Integer
    string = "123"
    num = int(string)
    print("The integer is:", num)
    
    # String to Float
    string = "123.456"
    num = float(string)
    print("The float is:", num)
    
    # List to Tuple
    list = [1, 2, 3, 4, 5]
    tuple = tuple(list)
    print("The tuple is:", tuple)
    
    # Tuple to List
    tuple = (1, 2, 3, 4, 5)
    list = list(tuple)
    print("The list is:", list)
    
    # Set to List
    set = {1, 2, 3, 4, 5}
    list = list(set)
    print("The list is:", list)
    
    # Dictionary to List
    dict = {1: "one", 2: "two", 3: "three"}
    list = list(dict.keys())
    print("The list is:", list)
    ```
    
- Type(),Id() Functions
    
    **`type()`** function in Python is used to find the type of an object. For example:
    
    ```python
    pythonCopy code
    num = 123
    print(type(num)) # <class 'int'>
    
    string = "hello world"
    print(type(string)) # <class 'str'>
    
    list = [1, 2, 3, 4, 5]
    print(type(list)) # <class 'list'>
    
    tuple = (1, 2, 3, 4, 5)
    print(type(tuple)) # <class 'tuple'>
    
    set = {1, 2, 3, 4, 5}
    print(type(set)) # <class 'set'>
    
    dict = {1: "one", 2: "two", 3: "three"}
    print(type(dict)) # <class 'dict'>
    ```
    
    **`id()`** function returns the unique identifier of an object in memory. For example:
    
    ```python
    pythonCopy code
    num1 = 123
    num2 = 123
    print(id(num1)) # 140725080343072
    print(id(num2)) # 140725080343072
    ```
    
- Escape Sequences
    - **`\n`**: newline character, used to represent a line break
    - **`\t`**: tab character, used to represent a tab space
    - **`\\`**: backslash character, used to represent a literal backslash
    - **`\'`**: single quote character, used to represent a literal single quote within a string enclosed in single quotes
    - **`\"`**: double quote character, used to represent a literal double quote within a string enclosed in double quotes
    - **`\r`**: carriage return character, used to represent a return to the beginning of the line