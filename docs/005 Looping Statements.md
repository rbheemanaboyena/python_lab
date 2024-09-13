# Looping Statements

- while loop
    
    ```python
    while condition:
        # code to be executed
    
    count = 0
    while count < 10:
        print(count)
        count = count + 1
    ```
    
- for
    
    ```python
    for variable in iterable:
        # code to be executed
    
    for i in range(10):
        print(i)
    
    fruits = ['apple', 'banana', 'cherry']
    for fruit in fruits:
        print(fruit)
    ```
    
- Range()
    
    The **`range`** function in Python is used to generate a sequence of numbers.
    
    ```python
    range(stop)
    range(start, stop)
    range(start, stop, step)
    
    for i in range(10):
        print(i)
    
    for i in range(5, 15, 2):
        print(i)
    
    numbers = list(range(10))
    print(numbers)
    ```
    
- Nested for loop
    
    ```python
    for i in range(2):
        for j in range(3):
            print(i, j)
    ```
    
- Break Statement
    
    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```
    
- Continue Statement
    
    The **`continue`**statement is used in a loop to skip the current iteration of the loop and move on to the next iteration. When the **`continue`** statement is executed, the rest of the code in the current iteration is skipped, and the next iteration begins.
    
    ```python
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)
    ```
    
- Pass Statement
    
    The **`pass`**statement in Python is a placeholder statement that does nothing. It is used when you need to write a stub for a piece of code that you haven't written yet, or when you want to write a block of code that doesn't do anything.
    
    ```python
    x = 5
    if x > 0:
        pass
    else:
        print("x is not greater than 0")
    
    def my_function():
        pass
    
    class MyClass:
        pass
    
    '''
    the pass statement is used as a placeholder until you are ready to write the actual code for the function or class.
    '''
    ```
