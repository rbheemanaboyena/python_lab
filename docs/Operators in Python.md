# Operators in Python

- Arithmetic Operators
    
    ```python
    x = 5
    y = 2
    
    # Addition
    print(x + y) # 7
    
    # Subtraction
    print(x - y) # 3
    
    # Multiplication
    print(x * y) # 10
    
    # Division
    print(x / y) # 2.5
    
    # Floor Division
    print(x // y) # 2
    
    # Modulus
    print(x % y) # 1
    
    # Exponentiation
    print(x ** y) # 25
    
    '''
    math module to perform mathamatical operations
    '''
    ```
    
- Comparison Operators
    
    ```python
    x = 5
    y = 2
    
    # Equal to
    print(x == y) # False
    
    # Not equal to
    print(x != y) # True
    
    # Greater than
    print(x > y) # True
    
    # Less than
    print(x < y) # False
    
    # Greater than or equal to
    print(x >= y) # True
    
    # Less than or equal to
    print(x <= y) # False
    ```
    
- Logical Operators
    
    ```python
    x = True
    y = False
    
    # Logical and
    print(x and y) # False
    
    # Logical or
    print(x or y) # True
    
    # Logical not
    print(not x) # False
    print(not y) # True
    ```
    
- Assignment  and Short Hand Assignment Operators
    
    ```python
    a = 10
    b = 20
    
    # Equal to operator
    c = a + b
    print("a + b = ", c)
    
    # Add and assign operator
    a += b
    print("a after adding and assigning b: ", a)
    
    # Subtract and assign operator
    a -= b
    print("a after subtracting and assigning b: ", a)
    
    # Multiply and assign operator
    a *= b
    print("a after multiplying and assigning b: ", a)
    
    # Divide and assign operator
    a /= b
    print("a after dividing and assigning b: ", a)
    
    # Modulo and assign operator
    a %= b
    print("a after modulo and assigning b: ", a)
    
    # Exponent and assign operator
    a **= b
    print("a after exponent and assigning b: ", a)
    
    # Floor division and assign operator
    a //= b
    print("a after floor division and assigning b: ", a)
    
    '''
    output:
    a + b =  30
    a after adding and assigning b:  30
    a after subtracting and assigning b:  10
    a after multiplying and assigning b:  200
    a after dividing and assigning b:  10.0
    a after modulo and assigning b:  10.0
    a after exponent and assigning b:  1e+20
    a after floor division and assigning b:  1
    '''
    ```
    
- Bitwise Operators
    
    ```python
    a = 10
    b = 4
    
    # Bitwise AND
    print("a & b: ", a & b)
    
    # Bitwise OR
    print("a | b: ", a | b)
    
    # Bitwise XOR
    print("a ^ b: ", a ^ b)
    
    # Bitwise NOT
    print("~a: ", ~a)
    
    # Left shift
    print("a << 2: ", a << 2)
    
    # Right shift
    print("a >> 2: ", a >> 2)
    
    '''
    output 
    a & b:  0
    a | b:  14
    a ^ b:  14
    ~a:  -11
    a << 2:  40
    a >> 2:  2
    '''
    ```
    
- Membership Operators
    
    Membership operators in Python are used to check whether a value is a member of a sequence such as strings, lists, tuples, or dictionaries. There are two membership operators in Python
    
    ```python
    fruits = ['apple', 'banana', 'cherry']
    
    if 'apple' in fruits:
        print("apple is in the list of fruits")
    else:
        print("apple is not in the list of fruits")
    
    if 'grapes' not in fruits:
        print("grapes are not in the list of fruits")
    else:
        print("grapes are in the list of fruits")
    ```
    
- Identity Operators
    
    The identity operators in Python are **`is`** and **`is not`**These operators are used to compare the identity of two objects, rather than their values.
    
    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    print(a is b)  # False
    print(a is c)  # True
    print(a is not b)  # True
    print(a is not c)  # False
    ```