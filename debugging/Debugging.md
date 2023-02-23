# Debugging

Debugging is the process of finding and fixing errors or bugs in software code. In Python, there are several ways to debug your code:

1. Print statements: One of the most basic and simple ways to debug your code is by using print statements. You can print out the value of variables or certain parts of your code to see what's going on.
    
    ```python
    # Example of using print statements to debug a function
    def calculate_total(price, tax_rate):
        print("Price:", price)
        print("Tax Rate:", tax_rate)
        total = price + (price * tax_rate)
        print("Total:", total)
        return total
    
    calculate_total(10.00, 0.10)
    ```
    
2. Debugger: Python comes with a built-in debugger module called "pdb". You can use it to step through your code line by line and check the value of variables at any point in the code.
    
    ```python
    # Example of using the built-in Python debugger (pdb)
    import pdb
    
    def calculate_total(price, tax_rate):
        pdb.set_trace()
        total = price + (price * tax_rate)
        return total
    
    calculate_total(10.00, 0.10)
    ```
    
3. IDEs: Integrated Development Environments (IDEs) like PyCharm, Visual Studio Code, and Spyder come with built-in debuggers that allow you to debug your code with a graphical user interface.
    1. Set a breakpoint by clicking on the left side of the line where you want to stop execution.
    2. Run the code in debug mode by clicking the "Debug" button or pressing "Shift+F9".
    3. When the code reaches the breakpoint, it will pause execution and allow you to inspect variables and step through the code.
4. Logging: Another way to debug your code is by using the logging module. You can add logging statements to your code to see what's happening at different points in your code.
    
    ```python
    # Example of using the logging module
    import logging
    
    def calculate_total(price, tax_rate):
        logging.debug("Price: %s", price)
        logging.debug("Tax Rate: %s", tax_rate)
        total = price + (price * tax_rate)
        logging.debug("Total: %s", total)
        return total
    
    calculate_total(10.00, 0.10)
    ```
    
5. Assertions: You can also use assertions to test that certain conditions are true at different points in your code. If an assertion fails, it will raise an exception and stop your code from running.
    
    ```python
    # Example of using assertions to check for a specific condition
    def calculate_total(price, tax_rate):
        assert price >= 0, "Price should be non-negative"
        assert tax_rate >= 0, "Tax rate should be non-negative"
        total = price + (price * tax_rate)
        return total
    
    calculate_total(-10.00, 0.10)
    ```