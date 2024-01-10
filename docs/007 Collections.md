# Collections

Collections in Python specifically refers to a set of high-level, built-in data structures, The collections module in Python is a module that provides specialized data structures as an extension to the built-in types (lists, tuples, sets, and dictionaries). It offers alternatives and enhancements to the basic data structures, providing more functionality and options for specific use cases.

The **`collections`** module in Python provides alternative data structures that can be used in place of built-in data structures like lists, dictionaries, and tuples. These alternative data structures include:

- **`Counter`**: a dictionary-like object that counts the occurrences of elements in a collection.
- **`defaultdict`**: a subclass of the built-in **`dict`** class that returns a default value when a key is not found in the dictionary.
- **`OrderedDict`**: a dictionary-like object that maintains the order of elements as they are inserted into the dictionary.
- **`deque`**: a double-ended queue that supports efficient insertion and deletion of elements from both ends.
- **`namedtuple`**: a subclass of tuple that allows access to elements by name instead of index.
- **`ChainMap`**: a class that provides a single view of multiple dictionaries.

These data structures can be useful in different situations and can simplify coding by reducing the need to write custom data structures or algorithms.

1. Named Tuple: A Named Tuple is a subclass of tuple that allows you to access its elements by name, instead of only by index. You can create a Named Tuple by using the namedtuple method from the collections module.
    
    ```python
    from collections import namedtuple
    
    Person = namedtuple('Person', ['name', 'age', 'gender'])
    
    person = Person('John', 30, 'Male')
    
    print(person.name) # Output: John
    print(person.age) # Output: 30
    print(person.gender) # Output: Male
    ```
    
2. Deque: A Deque (short for Double-ended Queue) is a queue data structure that allows you to insert or remove elements from both ends of the queue. You can create a Deque by using the deque method from the collections module.
    
    ```python
    from collections import deque
    
    queue = deque()
    
    queue.appendleft(1)
    queue.appendleft(2)
    queue.append(3)
    
    print(queue) # Output: deque([2, 1, 3])
    
    queue.popleft()
    
    print(queue) # Output: deque([1, 3])
    ```
    
3. Counter: A Counter is a dict subclass that counts the occurrences of elements in a collection. You can create a Counter by using the Counter method from the collections module.
    
    ```python
    from collections import Counter
    
    counter = Counter([1, 1, 2, 3, 3, 3])
    
    print(counter) # Output: Counter({3: 3, 1: 2, 2: 1})
    ```
    
4. OrderedDict: An OrderedDict is a dict subclass that remembers the order in which elements are inserted into the dict. You can create an OrderedDict by using the OrderedDict method from the collections module.
    
    ```python
    from collections import OrderedDict
    
    ordered_dict = OrderedDict()
    
    ordered_dict['a'] = 1
    ordered_dict['b'] = 2
    ordered_dict['c'] = 3
    
    print(ordered_dict) # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    ```
    
- **Operations on collections**
    
    Operations on collections refer to various actions that can be performed on data structures such as lists, tuples, and dictionaries. Some of the most common operations on collections include:
    
    1. Indexing: Accessing individual elements of a collection using an index.
    2. Slicing: Accessing a range of elements from a collection.
    3. Concatenation: Joining two or more collections to create a new collection.
    4. Repetition: Creating a new collection by repeating the elements of an existing collection.
    5. Membership testing: Checking if an element is present in a collection.
    6. Counting: Determining the number of times an element appears in a collection.
    7. Sorting: Arranging the elements of a collection in a particular order.
    8. Reversing: Reversing the order of elements in a collection.
    9. Adding/Removing elements: Adding or removing elements from a collection.
    10. Iterating: Looping over the elements of a collection to perform some action on each one.
- **Functions for collections**
    1. **`len(collection)`** returns the number of elements in a collection.
    2. **`max(collection)`** returns the largest element in a collection.
    3. **`min(collection)`** returns the smallest element in a collection.
    4. **`sum(collection)`** returns the sum of elements in a collection.
    5. **`sorted(collection)`** returns a sorted version of the collection.
    6. **`reversed(collection)`** returns a reversed version of the collection.
    7. **`enumerate(collection)`** returns a sequence of tuples containing the index and value of each element in a collection.
    8. **`zip(collection1, collection2)`** returns a sequence of tuples containing elements from both collections, paired together.
    9. **`map(function, collection)`** returns a sequence of values resulting from applying a function to each element in the collection.
    10. **`filter(function, collection)`** returns a sequence of elements for which the function returns True.
- **Methods of collection**
    
    The collections module in Python provides various alternative data structures for managing collections of data. Some of the most commonly used methods for collections are:
    
    1. Counter: It is a subclass of dict and it is used to count the number of occurrences of elements in a list.
        
        ```python
        
        from collections import Counter
        list = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 4, 4, 4, 4, 4]
        counter = Counter(list)
        print(counter)
        '''
        Output: **Counter({4: 6, 1: 3, 2: 3, 3: 3})
        '''**
        ```
        
    2. deque: It is a double-ended queue, which means that you can insert and remove elements from both ends.
        
        ```python
        
        from collections import deque
        queue = deque(["apple", "banana", "cherry"])
        queue.append("date")
        queue.appendleft("fig")
        print(queue)
        '''
        Output: **deque(['fig', 'apple', 'banana', 'cherry', 'date'])
        '''**
        ```
        
    3. namedtuple: It is a subclass of tuple, and it allows you to access the elements in a tuple by name, rather than by index.
        
        ```python
        
        from collections import namedtuple
        Person = namedtuple("Person", "name age gender")
        p1 = Person(name="John", age=32, gender="Male")
        print(p1.name, p1.age, p1.gender)
        #Output: **John 32 Male**
        ```
        
    4. OrderedDict: It is a subclass of dict and it remembers the order of elements in which they were inserted.
        
        ```python
        
        from collections import OrderedDict
        od = OrderedDict()
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4
        print(od)
        
        #Output: **OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])**
        ```
        
    5. **`defaultdict`**:
        
        ```python
        
        from collections import defaultdict
        
        # A defaultdict with default value 0
        numbers = defaultdict(int)
        
        # Setting values
        numbers['one'] = 1
        numbers['two'] = 2
        numbers['three'] = 3
        
        # Accessing values
        print(numbers['one']) # Output: 1
        print(numbers['four']) # Output: 0
        
        ```
        
    6. **`ChainMap`**:
        
        ```python
        
        from collections import ChainMap
        
        # Two dictionaries
        dict1 = {'one': 1, 'two': 2}
        dict2 = {'three': 3, 'four': 4}
        
        # ChainMap of dictionaries
        chain = ChainMap(dict1, dict2)
        
        # Accessing values
        print(chain['one']) # Output: 1
        print(chain['three']) # Output: 3
        
        ```
        
    7. **`UserDict`**:
        
        ```python
        from collections import UserDict
        
        # A custom dictionary class
        class MyDict(UserDict):
            def __setitem__(self, key, value):
                super().__setitem__(key, value + 10)
        
        # Creating an object of custom dictionary
        my_dict = MyDict({'one': 1, 'two': 2})
        
        # Setting values
        my_dict['three'] = 3
        my_dict['four'] = 4
        
        # Accessing values
        print(my_dict['one']) # Output: 11
        print(my_dict['three']) # Output: 13
        
        ```
        
- **Nested collections**
    
    a nested collection refers to a collection (such as a list, tuple, dictionary, or set) that is contained within another collection. For example, you can have a list of dictionaries, a dictionary of lists, or a nested tuple that contains a list. Here are some examples:
    
    1. List of Dictionaries:
        
        ```python
        
        student_records = [{"Name": "John", "Age": 24, "Department": "Computer Science"},{"Name": "Jane", "Age": 26, "Department": "Mechanical Engineering"},{"Name": "Jim", "Age": 28, "Department": "Civil Engineering"}]
        ```
        
    2. Dictionary of Lists:
        
        ```python
        employee_records = {"Sales": ["John", "Jane", "Jim"],
                            "Engineering": ["Jack", "Jill", "Jenny"],
                            "Marketing": ["James", "Jessica", "Johny"]}
        ```
        
    3. Nested Tuple:
        
        ```python
        
        person_details = (("Name", "John"), ("Age", 24),
                          ("Hobbies", ["Reading", "Writing", "Travelling"]))
        
        ```
        
    
    Note that nested collections can be used to store complex data structures and can be useful in various data processing and analysis tasks.
    
- **Differences b/w list tuple and set and Dictionary**
    
    List, Tuple, Set, and Dictionary are all data structures in Python that allow you to store and manipulate collections of data. However, each of these data structures has its own characteristics and usage scenarios, which makes them suitable for different purposes.
    
    The main differences between them are:
    
    1. Lists and Tuples:
    Lists are mutable, which means you can change their contents after they have been created. On the other hand, tuples are immutable, meaning that once created, their contents cannot be changed. This makes tuples suitable for situations where you want to store a fixed set of values that should not be changed, such as coordinates in a 2D plane.
    2. Sets and Dictionaries:
    Sets are collections of unique elements, and they are unordered. This makes them suitable for situations where you want to store unique values or perform mathematical set operations such as union and intersection. Dictionaries, on the other hand, store key-value pairs, and they are ordered. This makes them suitable for situations where you want to store data that can be easily retrieved using a key, such as a database of employee information.
    3. Lists, Tuples, and Dictionaries:
    Lists and tuples are both ordered sequences of elements, while dictionaries are unordered collections of key-value pairs. This means that you can index and slice lists and tuples, but you cannot do so with dictionaries.
