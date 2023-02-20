# Data Structures/collections

- Numbers
    
     In Python, you can use the **`int`** (integer) and **`float`** (floating point) data types to represent numerical values.
    
- Strings
    
    Strings are sequences of characters, used to represent text. Strings are defined using quotes, either single **`'`** or double **`"`**. For example: **`"hello, world!"`** 
    
    In Python, strings are immutable, which means that once a string is created, its contents cannot be changed. However, you can create new strings from existing strings by concatenating them, slicing them, or using other string operations.
    
    Here are some common string operations in Python:
    
    - Concatenation: Two or more strings can be joined together to create a new string using the **`+`** operator. For example:
        
        ```python
        string1 = "Hello"
        string2 = "World"
        string3 = string1 + " " + string2
        print(string3) # "Hello World"
        ```
        
    - Slicing: You can extract a portion of a string by using slicing. For example:
        
        ```python
        string = "Hello, World!"
        print(string[0:5]) # "Hello"
        print(string[7:12]) # "World"
        
        print(string[:5]) # "Hello"
        print(string[7:]) # "World!"
        
        print(string[-1]) # "!"
        print(string[-6:-1]) # "World"
        
        print(string[::-1]) # "!dlroW ,olleH"
        
        print(string[::-2]) #!lo olH
        ```
        
    - Indexing: You can access individual characters within a string using indexing. For example:
        
        ```python
        string = "Hello, World!"
        print(string[0]) # "H"
        print(string[7]) # "W"
        ```
        
    - Length: You can find the length of a string using the **`len()`** function. For example:
        
        ```python
        string = "Hello, World!"
        print(len(string)) # 13
        ```
        
    - Formatting: You can use string formatting to insert values into a string. For example:
        
        ```python
        name = "John"
        age = 30
        string = "My name is {} and I am {} years old".format(name, age)
        print(string) # "My name is John and I am 30 years old"
        ```
        
    - String Comparison
        
        ```python
        string1 = "hello"
        string2 = "world"
        
        print(string1 == string2) # False
        print(string1 != string2) # True
        print(string1 > string2) # False
        print(string1 < string2) # True
        ```
        
    - String splitting and joining
        
        ```python
        string = "Hello World"
        words = string.split()
        print(words)  # ['Hello', 'World']
        
        string = "apple,banana,cherry,dates"
        fruits = string.split(',')
        print(fruits)  # ['apple', 'banana', 'cherry', 'dates']
        
        words = ['Hello', 'World']
        string = ' '.join(words)
        print(string)  # Hello World
        ```
        
    - Finding Sub Strings
        
        ```python
        string = "Hello World"
        substring = "Hello"
        
        result = substring in string
        print(result)  # True
        
        result = string.find(substring)
        print(result)  # 0
        ```
        
    - String Case Change
        
        ```python
        string = "Hello World"
        uppercase_string = string.upper()
        print(uppercase_string)  # HELLO WORLD
        
        lowercase_string = string.lower()
        print(lowercase_string)  # hello world
        
        title_case_string = string.title()
        print(title_case_string)  # Hello World
        
        swapped_case_string = string.swapcase()
        print(swapped_case_string)  # hELLO wORLD
        ```
        
    - String methods
        - **`len()`**: Returns the length of the string
        - **`lower()`**: Converts all characters in the string to lowercase
        - **`upper()`**: Converts all characters in the string to uppercase
        - **`str.strip()`**: Returns a copy of the string with leading and trailing whitespace stripped
        - **`str.replace(old, new)`**: Returns a copy of the string with all occurrences of **`old`** replaced with **`new`**
        - **`str.split(sep)`**: Returns a list of substrings by splitting the string at occurrences of **`sep`**
        - **`str.join(iterable)`**: Returns a string concatenated with elements of **`iterable`** separated by the string itself
        - **`str.find(sub)`**: Returns the index of the first occurrence of **`sub`** in the string, or -1 if not found
        - **`str.count(sub)`**: Returns the number of occurrences of **`sub`** in the string
        - **`str.startswith(prefix)`**: Returns **`True`** if the string starts with **`prefix`**, **`False`** otherwise
        - **`str.endswith(suffix)`**: Returns **`True`** if the string ends with **`suffix`**, **`False`** otherwise
- Lists
    
    Lists are ordered collections of elements that can be of any data type, including other lists. Lists are defined using square brackets **`[]`** and the elements are separated by commas. For example: **`[1, 2, 3, 4]`**
    
    - List properties
        1. Mutability: Lists are mutable, meaning their elements can be changed after they are created.
        2. Ordering: Lists maintain the order of their elements, so the first element of a list is always at index 0, the second element is at index 1, and so on.
        3. Indexing: Lists can be indexed just like strings, so you can access individual elements using square brackets.
        4. Nesting: Lists can contain any type of object, including other lists, so you can create nested data structures.
        5. Iterability: Lists are iterable, meaning you can loop over their elements using for loops.
        6. Dynamic Size: Lists can grow or shrink in size dynamically as you add or remove elements, so you don't have to specify the size of a list when you create it.
    - List indexing and slicing
        
        ```python
        # creating a list of numbers
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # accessing the first element using indexing
        print(numbers[0])
        
        # accessing the last element using negative indexing
        print(numbers[-1])
        
        # slicing the list to get a sub-list
        print(numbers[2:5]) # prints [3, 4, 5]
        
        # slicing the list to get every second element
        print(numbers[::2]) # prints [1, 3, 5, 7, 9]
        ```
        
    - List Operations
        1. Concatenation: You can concatenate two lists by using the **`+`** operator.
        2. Repetition: You can repeat a list by using the  * operation 
        3. Membership: You can check if an element is present in a list using the **`in`** operator.
        4. Length: You can find the length of a list using the **`len()`** function.
        5. Indexing: You can access elements in a list by their index. Indexing starts from 0.
        6. Slicing: You can slice a list to get a specific range of elements.
        7. Modifying: You can modify elements in a list by assigning values to them.
        8. Adding elements: You can add elements to a list using various methods such as **`append()`**, **`insert()`**, **`extend()`**.
        9. Removing elements: You can remove elements from a list using various methods such as **`remove()`**, **`pop()`**, **`clear()`**.
        10. Sorting: You can sort a list using the **`sort()`** method.
        11. Reversing: You can reverse a list using the **`reverse()`** method.
    - List addresses
        
        In Python, a list is an ordered collection of elements that can be of different data types, including other lists. The elements in a list are stored in memory, and each element is assigned a unique address. This address is used to access and manipulate the elements in the list. The first element in a list is assigned the address 0, the second element is assigned the address 1, and so on. This allows us to access and manipulate specific elements in the list by using their addresses, also known as indexing.
        
    - Different ways of creating lists
        
        ```python
        my_list = [1, 2, 3, 4, 5]
        
        my_list = list([1, 2, 3, 4, 5])
        
        my_list = list(range(1, 6))
        
        my_list = [i for i in range(1, 6)]
        ```
        
    - Nested Lists
        
        ```python
        nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        print(nested_list[1])  # Output: [4, 5, 6]
        print(nested_list[1][1])  # Output: 5
        
        nested_list[1][1] = 10
        print(nested_list)  # Output: [[1, 2, 3], [4, 10, 6], [7, 8, 9]]
        ```
        
    - List of functions and Methods
        1. len(list): This function returns the number of elements in a list.
        2. max(list): This function returns the maximum value in a list of numbers.
        3. min(list): This function returns the minimum value in a list of numbers.
        4. sum(list): This function returns the sum of all the numbers in a list.
        5. sorted(list)
        
        **Methods**
        
        1. **`append()`** - This method appends an element to the end of the list.
            
            ```python
            my_list = [1, 2, 3]
            print(dir(my_list))
            ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
            
            fruits = ['apple', 'banana', 'cherry']
            fruits.append('orange')
            print(fruits)
            ['apple', 'banana', 'cherry', 'orange']
            ```
            
        2. ``ex**tend()**` - This method extends the list by adding all the elements of an iterable (e.g. list, tuple, etc.) to the end of the list.
            
            ```python
            fruits = ['apple', 'banana', 'cherry']
            more_fruits = ['orange', 'grapes']
            fruits.extend(more_fruits)
            print(fruits)
            ['apple', 'banana', 'cherry', 'orange', 'grapes']
            ```
            
        
        3.  **`insert()`** - This method inserts an element at a specified index in the list.
        
            ```python
            fruits = ['apple', 'banana', 'cherry']
            fruits.insert(1, 'orange')
            print(fruits)
            ['apple', 'orange', 'banana', 'cherry']
            ```
        
        1.  **`remove()`** - This method removes the first occurrence of a specified element in the list.
            
            ```python
            fruits = ['apple', 'banana', 'cherry', 'orange']
            fruits.remove('banana')
            print(fruits)
            ['apple', 'cherry', 'orange']
            ```
            
        2.  **`pop()`** - This method removes the element at the specified index in the list. If no index is specified, it removes the last element of the list.
            
            ```python
            fruits = ['apple', 'banana', 'cherry', 'orange']
            fruits.pop(1)
            'banana'
            print(fruits)
            ['apple', 'cherry', 'orange']
            ```
            
        3.  **`index()`** - This method returns the index of the first occurrence of a specified element in the list.
            
            ```python
            fruits = ['apple', 'banana', 'cherry', 'orange']
            fruits.index('banana')
            1
            ```
            
        4. **`count()`** - This method returns the number of times a specified element appears in the list.
            
            ```python
            fruits = ['apple', 'banana', 'cherry', 'orange', 'banana']
            fruits.count('banana')
            2
            ```
            
        5. **`sort()`** - This method sorts the elements of the list in ascending order.
            
            ```python
            fruits = ['cherry', 'orange', 'banana', 'apple']
            fruits.sort()
            print(fruits)
            ['apple', 'banana', 'cherry', 'orange']
            ```
            
        6. **`reverse()`** - This method reverses the order of the elements in the list.
            
            ```python
            fruits = ['apple', 'banana', 'cherry', 'orange']
            fruits.reverse()
            print(fruits)
            ['orange', 'cherry', 'banana', 'apple']
            ```
            
- Tuples
    
    Tuples are ordered collections of elements, similar to lists, but they are immutable, meaning that their elements cannot be changed once they are created. you need to create a new tuple with the desired elements. Tuples are defined using parentheses **`()`** and the elements are separated by commas.
    
     For example: **`(1, 2, 3, 4)`**
    
    - Tuple properties
        1. Immutable: Tuples are immutable, which means that once a tuple is created, its elements cannot be changed. In contrast, lists are mutable and can be modified after creation.
        2. Indexing and Slicing: Tuples can be indexed and sliced just like lists, but because they are immutable, you cannot modify their elements.
        3. Faster than lists: Tuples are generally faster than lists because they are immutable and therefore do not need to be resized.
        4. Use parentheses instead of square brackets: Tuples are created using parentheses () instead of square brackets [].
        5. Can contain different data types: Tuples can contain elements of different data types, just like lists.
    - Tuple indexing and slicing
        
        same as list 
        
    - Different ways of creating tuples
        
        ```python
        t = (1, 2, 3)
        
        t = 1,
        
        l = [1, 2, 3]
        t = tuple(l)
        ```
        
    - Tuple Operations
        1. Concatenation: Just like strings, we can concatenate two or more tuples using the **`+`** operator.
        2. Repetition: We can repeat the elements of a tuple by using the **``** operator.
        3. Indexing: Just like lists, we can access the elements of a tuple by using the index operator **`[]`**.
        4. Slicing: We can extract a portion of a tuple by using slicing just like we do for lists.
        5. Membership: We can check if a particular element exists in a tuple or not, using the **`in`** operator.
        6. Iteration: We can iterate over the elements of a tuple using a for loop.
    - Tuple Addresses
        
        In Python, when you assign a tuple to a variable, the variable refers to the memory location where the tuple is stored. You can access this memory location using the **`id()`**
         function in Python, which returns a unique identifier for an object.
        
    - Nested Tuples
        
        ```python
        tuple1 = (1, 2, 3, (4, 5, 6))
        ```
        
    - Tuple Functions and Methods
        
        Functions are same as list
        
        1. **`count()`** method - returns the number of occurrences of a given element in the tuple
            
            ```python
            
            t = (1, 2, 3, 2, 4, 2)
            print(t.count(2))
            3
            ```
            
        2. **`index()`** method - returns the index of the first occurrence of a given element in the tuple
            
            ```python
            
            t = (1, 2, 3, 4, 5)
            print(t.index(3))
            2
            ```
            
    - Differences b/w List and Tuple
        1. Mutability: Lists are mutable, meaning you can change their contents by adding, removing, or modifying elements. Tuples are immutable, meaning once you create a tuple, you cannot change its contents.
        2. Syntax: Lists are created with square brackets [ ], while tuples are created with parentheses ( ).
        3. Performance: Because tuples are immutable, accessing and manipulating elements in a tuple is faster than in a list. Lists are more dynamic, which makes them slower to work with.
        4. Built-in Functions: Lists have more built-in functions than tuples, as lists are more commonly used. For example, lists have a **`sort`** method, while tuples do not.
        5. Usages: Lists are generally used when you need to store a collection of items that can be changed dynamically. Tuples are used when you need to store a collection of items that cannot be changed and that need to be stored efficiently.
- Dictionaries
    
    Dictionaries are unordered collections of key-value pairs, where each key maps to a value. Dictionaries are defined using curly braces **`{}`** and the elements are separated by commas. The keys and values are separated by colons.
    
     For example: **`{"apple": 1, "banana": 2, "cherry": 3}`**
    
    - Dictionary properties
        1. Mutable: Dictionaries are mutable data types, meaning that their values can be changed after they are created.
        2. Key-Value Pairs: Dictionaries consist of key-value pairs, where the keys are unique and used to access the values.
        3. Unordered: Dictionaries do not have any inherent order, so the elements in a dictionary are not stored in any specific order.
        4. Indexing: Dictionaries are indexed by keys, not by numbers.
        5. Built-in functions: Python provides several built-in functions for dictionaries, such as len(), keys(), values(), items(), and more.
        6. Dynamic Typing: The keys and values in a dictionary can be of any data type, and the data type of a value can change dynamically.
        7. Nested dictionaries: Dictionaries can contain other dictionaries as values. This can be used to create complex data structures.
    - Dictionary Creation
        
        There are several ways to create a dictionary in Python:
        
        1. Using curly braces **`{}`**
            
            ```python
            # empty dictionary
            dict_1 = {}
            
            # dictionary with values
            dict_2 = {'name': 'John', 'age': 32, 'gender': 'Male'}
            ```
            
        2. Using the **`dict()`** constructor:
            
            ```python
            # empty dictionary
            dict_1 = dict()
            
            # dictionary with values
            dict_2 = dict(name='John', age=32, gender='Male')
            ```
            
        3. Using the **`zip()`** function:
            
            ```python
            keys = ['name', 'age', 'gender']
            values = ['John', 32, 'Male']
            
            dict_2 = dict(zip(keys, values))
            
            dict = {key: value for key, value in zip(keys, values)}
            ```
            
        4. load  yaml
            
            YAML (Yet Another Markup Language) is a human-readable data serialization format that is often used for configuration files, data exchange between systems, and data storage. In Python, the PyYAML library provides support for parsing and generating YAML. To load a YAML file in Python, you would typically do the following:
            
            ```python
            import yaml
            
            with open("file.yaml", "r") as stream:
                try:
                    data = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
            ```
            
        5. load .ini
            
            In Python, you can load the data from an .ini file using the **`configparser`** module. The **`configparser`** module provides functionality to read and write the data in the .ini file format. Here's an example of how you can read the data from an .ini file:
            
            ```python
            import configparser
            
            config = configparser.ConfigParser()
            config.read("config.ini")
            
            print(config.sections())
            print(config["DEFAULT"]["Compression"])
            ```
            
            In this example, we first import the **`configparser`** module, then create an instance of the **`ConfigParser`** class. The **`read`** method is used to read the data from the .ini file. The **`sections`** method returns a list of all the sections in the .ini file, and you can access the values in a section using the square bracket notation, as shown in the example.
            
        6. load  json 
            
            JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. Python provides the **`json`** module to work with JSON data. You can use the **`json.load()`** function to load a JSON file and convert it into a Python object (such as a dictionary). For example:
            
            ```python
            import json
            
            with open("data.json", "r") as file:
                data = json.load(file)
            
            print(data)
            ```
            
            This will load the data from the file **`data.json`** and store it in the **`data`** object, which will be a Python dictionary. You can then access the data in the same way as you would access a dictionary.
            
        7. load from pandas data frame to dict 
        
        Note: In a dictionary, keys must be unique and of immutable data types (such as strings, numbers, or tuples), while values can be of any data type.
        
    - Dictionary Operations
        1. Accessing values: You can access the values of a dictionary by using the key as an index. For example, if you have a dictionary **`d`** with key **`"name"`** and value **`"John"`**, you can access the value by using **`d["name"]`**.
        2.  Adding/Updating values: You can add a new key-value pair to a dictionary by using the assignment operator. For example, **`d["age"] = 25`** adds the key **`"age"`** with value **`25`** to the dictionary **`d`**. If the key already exists, its value will be updated with the new value.
        3. Deleting values: You can delete a key-value pair from a dictionary by using the **`del`** statement. For example, **`del d["age"]`** deletes the key **`"age"`** and its associated value from the dictionary **`d`**.
        4. Checking if a key exists: You can check if a key exists in a dictionary by using the **`in`** operator. For example, **`if "name" in d:`** checks if the key **`"name"`** exists in the dictionary **`d`**.
        5. Getting keys and values: You can get the keys and values of a dictionary using the **`keys()`** and **`values()`** methods respectively. For example, **`keys = d.keys()`** gets a list of all the keys in the dictionary **`d`**, and **`values = d.values()`** gets a list of all the values in the dictionary **`d`**.
        6.  Looping through a dictionary: You can loop through a dictionary using a **`for`** loop. For example, **`for key in d:`** loops through all the keys in the dictionary **`d`**. You can also use the **`items()`** method to loop through both the keys and values of a dictionary. For example, **`for key, value in d.items():`** loops through both the keys and values of the dictionary **`d`**.
    - Dictionary Addresses
        
        In Python, dictionaries are implemented as hash tables and do not have a definite order. So, it doesn't make sense to talk about the memory addresses of individual items in a dictionary. However, you can get the memory address of the entire dictionary object using the **`id()`**function. This will give you the unique identifier for the object in memory, which can be useful in certain cases.
        
    - Nested Dictionaries
        
        ```python
        person = {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA"
            }
        }
        
        print(person["address"]["city"])  # Output: Anytown
        ```
        
    - Dictionary Methods
        1. **`clear()`**: This method removes all the items from the dictionary.
            
            ```python
            
            dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
            dict1.clear()
            print(dict1)
            # Output: {}
            ```
            
        2. **`copy()`**: This method returns a shallow copy of the dictionary
            
            ```python
            dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
            dict2 = dict1.copy()
            print(dict2)
            # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
            ```
            
        3. **`fromkeys()`**: This method returns a new dictionary with specified keys and values.
            
            ```python
            dict1 = dict.fromkeys(['name', 'age', 'city'], 'Unknown')
            print(dict1)
            # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}
            ```
            
        4. **`get()`**: This method returns the value of the specified key. If the key does not exist, it returns None.
            
            ```python
            dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
            value = dict1.get('name')
            print(value)
            # Output: John
            ```
            
        5. **`items()`**: This method returns a view of the dictionary's items as key-value pairs.
            
            ```python
            dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
            items = dict1.items()
            print(items)
            # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
            ```
            
        6. **`keys()`**: This method returns a view of the dictionary's keys.
            
            ```python
            
            dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
            keys = dict1.keys()
            print(keys)
            # Output: dict_keys(['name', 'age', 'city'])
            ```
            
        7. **`pop()`**: This method removes the specified key and returns its value.
            
            ```python
            
            dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
            value = dict1.pop('age')
            print(dict1)
            # Output: {'name': 'John', 'city': 'New York'}
            ```
            
        8. **`popitem()`**: This method removes and returns an arbitrary key-value pair from the dictionary.
            
            ```python
            
            dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
            item = dict1.popitem()
            print(dict1)
            # Output: {'name': 'John', 'age': 30}
            ```
            
        
        The **`setdefault()`** method in Python is a dictionary method that allows you to set a default value for a key in the dictionary. If the key does not exist in the dictionary, then it is added with the default value. If the key already exists, then the value for that key remains unchanged. Here's an example:
        
        ```python
        my_dict = {'a': 1, 'b': 2}
        print(my_dict.setdefault('c', 3))   # 3
        print(my_dict)                       # {'a': 1, 'b': 2, 'c': 3}
        print(my_dict.setdefault('a', 4))   # 1
        print(my_dict)                       # {'a': 1, 'b': 2, 'c': 3}
        ```
        
    - insertion and Deletion of elements
        
        ```python
        # Adding elements to the dictionary
        dict1 = {}
        dict1['name'] = 'John'
        dict1['age'] = 30
        print(dict1) # Output: {'name': 'John', 'age': 30}
        
        dict2 = {'country': 'USA'}
        dict1.update(dict2)
        print(dict1) # Output: {'name': 'John', 'age': 30, 'country': 'USA'}
        
        # Deleting elements from the dictionary
        del dict1['age']
        print(dict1) # Output: {'name': 'John', 'country': 'USA'}
        
        age = dict1.pop('age', 'Age not found')
        print(age) # Output: Age not found
        ```
        
- Sets
    
    Sets are unordered and unchangeable collections of unique elements. Sets are defined using curly braces **`{}`** or the **`set()`** function and the elements are separated by commas. 
    
    For example: **`{1, 2, 3, 4}`**
    
    - Set properties
        1. Unordered: Sets do not have a specific order, and the items stored in a set may appear in a different order each time the set is accessed.
        2. Unchangeable: Once a set is created, its elements cannot be changed. You can add or remove elements from a set, but you cannot modify elements.
        3. Unique elements: A set can only have unique elements. If you try to add an element that already exists in the set, the set will not change.
        4. Mutable: Sets are mutable, meaning they can be changed after they are created. You can add or remove elements from a set.
        5. Dynamic size: The size of a set is dynamic, meaning it can grow or shrink as elements are added or removed.
        6. Supports operations: Sets support various operations, such as union, intersection, difference, and symmetric difference.
    - Set Creation
        
        ```python
        # Using the set() constructor
        s = set([1, 2, 3, 4, 5])
        print(s)  # Output: {1, 2, 3, 4, 5}
        
        # Using curly braces
        s = {1, 2, 3, 4, 5}
        print(s)  # Output: {1, 2, 3, 4, 5}
        ```
        
    - Set Operations
        1. Union: Combine two sets and return a set that contains all the elements from both sets, without duplicates. This is done using the **`union`** method or the **`|`** operator.
        2. Intersection: Return a set that contains elements that exist in both sets. This is done using the **`intersection`** method or the **`&`** operator.
        3. Difference: Return a set that contains elements that exist in one set but not in the other. This is done using the **`difference`** method or the **``** operator.
        4. Symmetric Difference: Return a set that contains elements that exist in one set or the other, but not both. This is done using the **`symmetric_difference`** method or the **`^`** operator.
        5. Subset: Check if one set is a subset of another set. This is done using the **`issubset`** method.
        6. Superset: Check if one set is a superset of another set. This is done using the **`issuperset`** method.
        7. Disjoint: Check if two sets have no elements in common. This is done using the **`isdisjoint`** method.
        
        ```python
        >>> A = {1, 2, 3}
        >>> B = {2, 3, 4}
        >>> A.union(B)
        {1, 2, 3, 4}
        >>> A.intersection(B)
        {2, 3}
        >>> A.difference(B)
        {1}
        >>> A.symmetric_difference(B)
        {1, 4}
        >>> B.issubset(A)
        False
        >>> A.issuperset(B)
        False
        >>> A.isdisjoint(B)
        False
        ```
        
    - Set Functions
        1. **`len(set)`**: This function returns the number of elements in a set.
        2. **`set.copy()`**: This function returns a shallow copy of the set.
        3. **`set.difference(set2)`**: This function returns a set that contains the difference between two sets.
        4. **`set.intersection(set2)`**: This function returns a set that contains the intersection between two sets.
        5. **`set.issubset(set2)`**: This function returns a Boolean value indicating whether a set is a subset of another set.
        6. **`set.issuperset(set2)`**: This function returns a Boolean value indicating whether a set is a superset of another set.
        7. **`set.union(set2)`**: This function returns a set that contains the union of two sets.
        8. **`set.symmetric_difference(set2)`**: This function returns a set that contains the symmetric difference between two sets.
        9. **`set.pop()`**: This function removes and returns a randomly chosen element from a set.
        10. **`set.clear()`**: This function removes all elements from a set.
        
        ```python
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        
        # Union
        print(s1 | s2) # Output: {1, 2, 3, 4, 5}
        
        # Intersection
        print(s1 & s2) # Output: {3}
        
        # Difference
        print(s1 - s2) # Output: {1, 2}
        
        # Symmetric Difference
        print(s1 ^ s2) # Output: {1, 2, 4, 5}
        
        # Length
        print(len(s1)) # Output: 3
        
        # Minimum and Maximum
        print(min(s1)) # Output: 1
        print(max(s1)) # Output: 3
        
        # Sum
        print(sum(s1)) # Output: 6
        
        # Sorted
        print(sorted(s1)) # Output: [1, 2, 3]
        
        # Any and All
        print(any(s1)) # Output: True
        print(all(s1)) # Output: True
        ```
        
    - Set Addresses
        
        sets are objects and are stored in memory as references, which means that the reference to the set object is stored in memory, not the actual set. This is why when you assign a set to a variable, you are actually assigning a reference to the set object in memory, not the set itself.
        
        For example, consider the following code:
        
        ```python
        a = {1, 2, 3}
        b = a
        print(id(a))
        print(id(b))
        
        '''
        140716508384552
        140716508384552
        '''
        ```
        
        In this example, **`a`** and **`b`** are both references to the same set object in memory, which is why their memory addresses (obtained using the **`id`** function) are the same.
        
    - Set Methods
        1. **`add`**: This method is used to add an element to a set.
            
            ```python
            >>> s = set([1, 2, 3, 4, 5])
            >>> s.add(6)
            >>> print(s)
            {1, 2, 3, 4, 5, 6}
            ```
            
        2. **`clear`**: This method is used to remove all the elements from the set.
            
            ```python
            >>> s = set([1, 2, 3, 4, 5])
            >>> s.clear()
            >>> print(s)
            set()
            ```
            
        3. **`copy`**: This method is used to create a shallow copy of the set.
            
            ```python
            >>> s = set([1, 2, 3, 4, 5])
            >>> s_copy = s.copy()
            >>> print(s_copy)
            {1, 2, 3, 4, 5}
            ```
            
        4. **`difference`**: This method returns the difference of two or more sets.
            
            ```python
            >>> s1 = set([1, 2, 3, 4, 5])
            >>> s2 = set([4, 5, 6, 7, 8])
            >>> s3 = s1.difference(s2)
            >>> print(s3)
            {1, 2, 3}
            ```
            
        5. **`difference_update`**: This method updates the set with the difference of two or more sets.
            
            ```python
            >>> s1 = set([1, 2, 3, 4, 5])
            >>> s2 = set([4, 5, 6, 7, 8])
            >>> s1.difference_update(s2)
            >>> print(s1)
            {1, 2, 3}
            ```
            
        6. **`discard`**: This method removes the specified element from the set.
            
            ```python
            >>> s = set([1, 2, 3, 4, 5])
            >>> s.discard(3)
            >>> print(s)
            {1, 2, 4, 5}
            ```
            
        7. **`intersection`**: This method returns the intersection of two or more sets.
            
            ```python
            >>> s1 = set([1, 2, 3, 4, 5])
            >>> s2 = set([4, 5, 6, 7, 8])
            >>> s3 = s1.intersection(s2)
            >>> print(s3)
            {4, 5}
            ```
            
        8. **`intersection_update`**: This method updates the set with the intersection of two or more sets.
            
            ```python
            >>> s1 = set([1, 2, 3, 4, 5])
            >>> s2 = set([4, 5, 6, 7, 8])
            >>> s1.intersection_update(s2)
            >>> print(s1)
            {4, 5}
            ```
            
    - Insertion and Deletion operation
        
        the insertion and deletion of elements in a set can be performed using the following methods:
        
        1. add() method: This method is used to add an element to the set.
            
            ```python
            # Example
            s = set([1, 2, 3])
            s.add(4)
            print(s)
            # Output: {1, 2, 3, 4}
            ```
            
        2. remove() method: This method is used to remove an element from the set. If the element is not present in the set, it raises a KeyError.
            
            ```python
            # Example
            s = set([1, 2, 3, 4])
            s.remove(4)
            print(s)
            # Output: {1, 2, 3}
            ```
            
        3. discard() method: This method is used to remove an element from the set. If the element is not present in the set, it does not raise any error.
            
            ```python
            # Example
            s = set([1, 2, 3, 4])
            s.discard(4)
            print(s)
            # Output: {1, 2, 3}
            ```
            
        4. pop() method: This method is used to remove and return an arbitrary element from the set. If the set is empty, it raises a KeyError.
            
            ```python
            # Example
            s = set([1, 2, 3, 4])
            x = s.pop()
            print(x)
            print(s)
            # Output:
            # 1
            # {2, 3, 4}
            ```
