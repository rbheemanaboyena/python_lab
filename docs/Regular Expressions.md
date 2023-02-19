# Regular Expressions

- What is regular expression?
    
    A regular expression (often referred to as a "regex") is a pattern or sequence of characters that defines a search or a search-and-replace operation on strings. In other words, a regular expression is a way of describing a set of strings using a compact syntax.
    
    Regular expressions are used for text processing and manipulation, such as validating user input, searching and replacing text, and splitting and merging strings. They are supported by many programming languages, including Python.
    
    The syntax for defining regular expressions can be complex and may vary between programming languages, but it typically includes special characters that match specific types of characters (such as digits, letters, or whitespace) and allow you to specify repetitions and alternatives.
    
    For example, the regular expression **`\d{3}-\d{2}-\d{4}`** could be used to match a string that represents a Social Security number in the format **`123-45-6789`**. The **`\d`** matches any digit, and the curly braces **`{3}`** and **`{2}`** specify the exact number of repetitions.
    
    In Python, you can use the **`re`** module to work with regular expressions. The module provides functions for searching, matching, and replacing text using regular expressions.
    
    ```python
    import re
    
    text = "My phone numbers are 123-456-7890 and 987-654-3210."
    
    # Define the pattern for a phone number
    phone_number_pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
    
    # Find all phone numbers in the text
    phone_numbers = re.findall(phone_number_pattern, text)
    
    # Print the phone numbers
    print("Phone numbers:")
    for number in phone_numbers:
        print(number)
    
    '''
    output:
    Phone numbers:
    123-456-7890
    987-654-3210
    '''
    ```
    
- Special characters
    
    Special characters are used in regular expressions to specify certain patterns or perform certain actions. Some of the most common special characters are:
    
    - **`.`** (dot) - Matches any single character except a newline character.
    - **`^`** (caret) - Matches the start of a string.
    - **`$`** (dollar) - Matches the end of a string.
    - **``** (asterisk) - Matches zero or more occurrences of the preceding character or group.
    - **`+`** (plus) - Matches one or more occurrences of the preceding character or group.
    - **`?`** (question mark) - Matches zero or one occurrence of the preceding character or group.
    - **`{m}`** (curly braces) - Matches exactly **`m`** occurrences of the preceding character or group.
    - **`{m,n}`** (curly braces with comma) - Matches at least **`m`** and at most **`n`** occurrences of the preceding character or group.
    - **`[...]`** (square brackets) - Defines a character class, which matches any one of the characters enclosed within the brackets.
    - **`\`** (backslash) - Escapes a special character and treats it as a literal character.
    
    Here's an example that uses some of these special characters:
    
    ```python
    
    import re
    
    text = "The number is 42, and the answer to life, the universe, and everything is 42."
    
    # Define the pattern for a number
    number_pattern = re.compile(r"\b\d+\b")
    
    # Find all numbers in the text
    numbers = re.findall(number_pattern, text)
    
    # Print the numbers
    print("Numbers:")
    for number in numbers:
        print(number)
    
    '''
    Numbers:
    42
    42
    '''
    ```
    
    In this example, the pattern **`\b\d+\b`** uses the **`\b`** (word boundary) character to specify that the pattern should only match complete words, and the **`\d+`** expression to match one or more digits.
    
- Forming regular expression
    
    A regular expression is formed by combining various special characters and plain text characters. The special characters include:
    
    1. **`.`** (dot) - Matches any single character except a newline character.
    2. **`^`** (caret) - Matches the start of a string.
    3. **`$`** (dollar) - Matches the end of a string.
    4. **``** (asterisk) - Matches zero or more occurrences of the preceding character or group.
    5. **`+`** (plus) - Matches one or more occurrences of the preceding character or group.
    6. **`?`** (question mark) - Matches zero or one occurrence of the preceding character or group.
    7. **`{m,n}`** - Matches at least **`m`** and at most **`n`** occurrences of the preceding character or group.
    8. **`[]`** (square brackets) - Matches any single character from a set of characters enclosed within square brackets.
    9. **`|`** (vertical bar) - Matches either the expression before or the expression after the vertical bar.
    10. **`\`** (backslash) - Escapes special characters.
    
    Plain text characters are just regular characters that match themselves. For example, the regular expression **`hello`** would match the string **`hello`** exactly.
    
    These special characters and plain text characters can be combined to form more complex regular expressions that can match a variety of patterns in strings.
    
- Compiling regular expressions
    
    In Python, regular expressions can be compiled using the **`re`** module. The **`re.compile()`** function takes a string as an argument, which represents the pattern to be matched, and returns a regular expression pattern object that can be used to match against other strings.
    
    Here's an example of how you can compile a regular expression:
    
    ```python
    import re
    
    pattern = re.compile("[a-z]+")
    ```
    
    In this example, the **`re.compile()`** function is used to compile a regular expression that matches one or more lowercase letters. The resulting pattern object can be used with functions such as **`re.search()`** and **`re.findall()`** to match against strings.
    
    Compiling a regular expression is recommended when the same pattern will be used multiple times, as it can improve performance by avoiding the overhead of parsing the regular expression each time it is used.
    
- Grouping
    
    Grouping is a feature in regular expressions that allows you to capture a specific part of a string that matches a pattern. You can group parts of a pattern by enclosing them in parentheses **`(`** and **`)`**. The grouped parts of the pattern can be referred to later in the pattern, or in the matched string, using special numbering codes.
    
    Here's an example of using grouping to match a date:
    
    ```python
    
    import re
    
    pattern = re.compile("(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})")
    
    date_string = "01/15/2022"
    
    match = pattern.search(date_string)
    
    if match:
        month = match.group("month")
        day = match.group("day")
        year = match.group("year")
        print(f"Month: {month}, Day: {day}, Year: {year}")
    ```
    
    In this example, the pattern is defined to match a date in the format of **`mm/dd/yyyy`** where **`mm`** is the two-digit representation of the month, **`dd`** is the two-digit representation of the day, and **`yyyy`** is the four-digit representation of the year. The parts of the pattern are grouped using parentheses and named using the **`(?P<name>)`** syntax, where **`name`** is the name of the group. The matched values of the groups can be obtained using the **`group()`** method of the **`re.Match`** object, and passing the name of the group as an argument.
    
- Findall() function
    
    The **`findall()`** function is a built-in function in Python's **`re`** module that is used to find all non-overlapping occurrences of a pattern in a string. It returns a list of all the occurrences of the pattern in the string.
    
    Here's an example:
    
    ```python
    
    import re
    
    text = "I have 2 cats and 3 dogs"
    pattern = r'\d+'
    
    result = re.findall(pattern, text)
    
    print(result)
    
    '''
    ['2', '3']
    '''
    ```
    
    In this example, the pattern **`r'\d+'`** is a regular expression that matches one or more consecutive digits. The **`findall()`** function is used to find all occurrences of this pattern in the string **`text`**, and the result is a list of all the matches, i.e., **`['2', '3']`**.
    
- Finditer() function
    
    The **`finditer()`** function is another built-in function in Python's **`re`** module that is used to find all non-overlapping occurrences of a pattern in a string. It returns an iterator that yields match objects for all the occurrences of the pattern in the string.
    
    Here's an example:
    
    ```python
    import re
    
    text = "I have 2 cats and 3 dogs"
    pattern = r'\d+'
    
    result = re.finditer(pattern, text)
    
    for match in result:
        print(match.group())
    
    '''
    2
    3
    '''
    ```
    
    In this example, the pattern **`r'\d+'`** is a regular expression that matches one or more consecutive digits. The **`finditer()`** function is used to find all occurrences of this pattern in the string **`text`**, and the result is an iterator that yields match objects for each occurrence. The **`group()`** method is used to extract the actual matching text from each match object.
    
- Sub() function
    
    The **`sub()`** function is a built-in function in Python's **`re`** module that is used to replace all occurrences of a pattern in a string with a specified replacement string.
    
    Here's an example:
    
    ```python
    import re
    
    text = "I have 2 cats and 3 dogs"
    pattern = r'\d+'
    replacement = '#'
    
    result = re.sub(pattern, replacement, text)
    
    print(result)
    
    '''
    I have # cats and # dogs
    '''
    ```
    
    In this example, the pattern **`r'\d+'`** is a regular expression that matches one or more consecutive digits. The **`sub()`** function is used to replace all occurrences of this pattern in the string **`text`** with the specified replacement string **`replacement`**, which is a single **`#`** character in this case. The resulting string is then printed
    
- Match() function
    
    The **`match()`** function is a built-in function in Python's **`re`** module that is used to determine if the regular expression pattern matches at the beginning of a string.
    
    Here's an example:
    
    ```python
    import re
    
    text = "I have 2 cats and 3 dogs"
    pattern = r'\d+'
    
    match = re.match(pattern, text)
    
    if match:
        print("Match found at index", match.start(), ":", match.group())
    else:
        print("No match found")
    
    '''
    Match found at index 8 : 2
    '''
    ```
    
    In this example, the pattern **`r'\d+'`** is a regular expression that matches one or more consecutive digits. The **`match()`** function is used to determine if this pattern matches at the beginning of the string **`text`**. If a match is found, the **`match`** object is created, and the start index and matched string are printed. If no match is found, the **`else`** clause is executed, and a message indicating that no match was found is printed.
    
- Search() function
- Matching vs searching
- Splitting a string
- Replacing text
- validations