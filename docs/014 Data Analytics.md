# Data Analytics

- Introduction
- pandas module
    - Introduction to Pandas
        
        Pandas is a popular open-source Python library for data manipulation and analysis. It provides easy-to-use data structures and data analysis tools for handling and processing structured data. Pandas is built on top of NumPy, which is another popular Python library for numerical computations.
        
        The two primary data structures in Pandas are Series and DataFrame. A Series is a one-dimensional labeled array capable of holding any data type, including integers, floats, strings, and Python objects. A DataFrame is a two-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or a SQL table.
        
        Pandas provides a wide range of functionalities for data manipulation and analysis, including indexing, slicing, merging, grouping, aggregating, filtering, reshaping, and visualizing data. It also supports handling missing data, time-series data, and text data.
        
        Pandas is widely used in data science, machine learning, and finance for data cleaning, data preprocessing, data exploration, and data analysis. It is a powerful tool for handling and analyzing large and complex datasets.
        
    - Creating Pandas Series
        
        ```python
        import pandas as pd
        
        # create a Series from a list of integers
        s = pd.Series([1, 2, 3, 4, 5])
        print(s)
        
        # create a Series from a list of strings with custom index labels
        s = pd.Series(['apple', 'banana', 'cherry', 'durian', 'elderberry'], index=['a', 'b', 'c', 'd', 'e'])
        print(s)
        
        # create a Series from a dictionary
        d = {'apple': 2, 'banana': 3, 'cherry': 4, 'durian': 5, 'elderberry': 6}
        s = pd.Series(d)
        print(s)
        
        ```
        
    - Creating Data Frames
        
        In Pandas, a DataFrame is a two-dimensional labeled data structure with columns of potentially different types. A DataFrame can be thought of as a spreadsheet or a SQL table. A DataFrame is created using the **`pandas.DataFrame()`**
         constructor, which takes a dictionary, a list of lists, or another DataFrame as an argument.
        
        - Pandas Data Frames from dictionaries
            
            ```python
            import pandas as pd
            
            # create a DataFrame from a dictionary
            data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
                    'age': [25, 30, 35, 40],
                    'gender': ['F', 'M', 'M', 'M']}
            df = pd.DataFrame(data)
            print(df)
            
            '''' 
                  name  age gender
            0     Alice   25      F
            1       Bob   30      M
            2   Charlie   35      M
            3     David   40      M
            
            '''
            ```
            
        - Pandas Data Frames from list
            
            ```python
            # create a DataFrame from a list of lists
            data = [['Alice', 25, 'F'],
                    ['Bob', 30, 'M'],
                    ['Charlie', 35, 'M'],
                    ['David', 40, 'M']]
            df = pd.DataFrame(data, columns=['name', 'age', 'gender'])
            print(df)
            
            '''
                   name  age gender
            0     Alice   25      F
            1       Bob   30      M
            2   Charlie   35      M
            3     David   40      M
            '''
            
            # create a list of dictionaries representing the data
            data = [
                {'name': 'Alice', 'age': 25, 'gender': 'female'},
                {'name': 'Bob', 'age': 30, 'gender': 'male'},
                {'name': 'Charlie', 'age': 35, 'gender': 'male'},
                {'name': 'David', 'age': 40, 'gender': 'male'},
                {'name': 'Eve', 'age': 45, 'gender': 'female'}
            ]
            
            # create a DataFrame from the list of dictionaries
            df = pd.DataFrame(data)
            
            print(df)
            ```
            
        - Pandas Data Frames from series
            
            ```python
            '''
            In Pandas, you can create a DataFrame from one or more Series objects. A DataFrame created from a single Series is a one-column DataFrame, while a DataFrame created from multiple Series can have multiple columns.
            '''
            
            import pandas as pd
            
            # create a Series
            s = pd.Series([1, 2, 3, 4, 5], name='numbers')
            
            # create a DataFrame from the Series
            df = pd.DataFrame(s)
            
            print(df)
            
            '''
            numbers
            0        1
            1        2
            2        3
            3        4
            4        5
            '''
            
            # create three Series
            s1 = pd.Series(['Alice', 'Bob', 'Charlie', 'David'], name='name')
            s2 = pd.Series([25, 30, 35, 40], name='age')
            s3 = pd.Series(['F', 'M', 'M', 'M'], name='gender')
            
            # create a DataFrame from the Series
            df = pd.concat([s1, s2, s3], axis=1)
            
            print(df)
            
            '''
                  name  age gender
            0     Alice   25      F
            1       Bob   30      M
            2   Charlie   35      M
            3     David   40      M
            '''
            ```
            
        - Pandas Data Frames from CSV, Excel
            
            ```python
            import pandas as pd
            
            # create a DataFrame by reading data from a CSV file
            df = pd.read_csv('data.csv')
            
            print(df)
            
            # create a DataFrame by reading data from an Excel file
            df = pd.read_excel('data.xlsx')
            
            print(df)
            ```
            
        - Pandas Data Frames from JSON
            
            ```python
            import pandas as pd
            
            # create a DataFrame by reading data from a JSON file
            df = pd.read_json('data.json')
            
            print(df)
            
            # create a JSON string
            json_str = '{"name": ["Alice", "Bob", "Charlie", "David"], "age": [25, 30, 35, 40], "gender": ["F", "M", "M", "M"]}'
            
            # create a DataFrame from the JSON string
            df = pd.read_json(json_str)
            
            print(df)
            ```
            
        - Pandas Data Frames from Databases
            
            ```python
            import pandas as pd
            import sqlite3
            
            # create a connection to a SQLite database
            conn = sqlite3.connect('example.db')
            
            # create a DataFrame by reading data from a database table
            df = pd.read_sql('SELECT * FROM my_table', conn)
            
            # close the database connection
            conn.close()
            
            print(df)
            ```
            
        - Creating Data Frames from Timedelta
            
            ```python
            import pandas as pd
            
            # create a DataFrame from a list of Timedelta objects
            td_list = [pd.Timedelta(days=3), pd.Timedelta(hours=5), pd.Timedelta(minutes=30)]
            df = pd.DataFrame({'time_delta': td_list})
            print(df)
            
            # create a DataFrame from a dictionary of Timedelta objects
            td_dict = {
                'A': pd.Timedelta(days=2),
                'B': pd.Timedelta(hours=8),
                'C': pd.Timedelta(minutes=45)
            }
            df = pd.DataFrame.from_dict(td_dict, orient='index', columns=['time_delta'])
            print(df)
            
            # create a DataFrame with a Timedelta column and a datetime column
            dates = pd.date_range('2022-02-15', periods=3)
            durations = [pd.Timedelta(days=2), pd.Timedelta(hours=8), pd.Timedelta(minutes=45)]
            df = pd.DataFrame({'date': dates, 'duration': durations})
            print(df)
            ```
            
    - Pandas Data Functionality
        - **Data selection and filtering:** You can select and filter data in a DataFrame using the **`loc`** and **`iloc`** operators. **`loc`** is used to select data by label, while **`iloc`** is used to select data by position. You can also use boolean indexing to filter data based on a condition.
        - **Data aggregation:** You can group data in a DataFrame and perform various aggregations on the groups using the **`groupby()`** method. For example, you can compute the sum, mean, or count of each group.
        - **Data transformation:** You can transform data in a DataFrame using various functions, such as **`apply()`**, **`map()`**, and **`replace()`**. For example, you can apply a function to each row or column of the DataFrame, map values to new values, or replace missing or incorrect values.
        - **Data merging and joining:** You can merge or join two or more DataFrames using the **`merge()`** and **`join()`** functions. These functions allow you to combine data from multiple sources based on common keys.
        - **Data sorting:** You can sort data in a DataFrame using the **`sort_values()`** method. This method allows you to sort the data based on one or more columns in ascending or descending order.
        - **Data visualization:** You can visualize data in a DataFrame using various functions in the **`matplotlib`** library. For example, you can create bar charts, line charts, scatter plots, and many other types of visualizations.
        
        These are just a few examples of the many data functionality in Pandas. Pandas provides a wide range of functions for working with data
        
        ```python
        import pandas as pd
        
        # create a DataFrame
        data = {
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Ella', 'Frank'],
            'age': [25, 30, 35, 40, 20, 45],
            'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
            'country': ['USA', 'Canada', 'UK', 'USA', 'Canada', 'USA'],
            'salary': [50000, 70000, 60000, 80000, 40000, 90000]
        }
        df = pd.DataFrame(data)
        
        # select data by label
        print(df.loc[df['gender'] == 'F'])
        
        # select data by position
        print(df.iloc[2:4, 1:3])
        
        # filter data based on a condition
        print(df[df['salary'] > 60000])
        
        # group data and perform aggregation
        print(df.groupby('country')['salary'].mean())
        
        # apply a function to each row
        df['taxes'] = df['salary'].apply(lambda x: x * 0.25)
        
        # map values to new values
        df['gender'] = df['gender'].map({'F': 'Female', 'M': 'Male'})
        
        # merge two DataFrames
        data2 = {
            'name': ['Bob', 'Charlie', 'David', 'Ella'],
            'dept': ['sales', 'marketing', 'sales', 'finance']
        }
        df2 = pd.DataFrame(data2)
        merged_df = pd.merge(df, df2, on='name')
        
        # sort data
        print(df.sort_values(by=['age', 'salary']))
        
        # visualize data
        df.plot(kind='bar', x='name', y='salary')
        ```
        
    - Pandas Timedelta
        
        In Pandas, **`Timedelta`** represents a duration or elapsed time.
        
        ```python
        import pandas as pd
        
        # create a Timedelta object
        td = pd.Timedelta('1 days 2 hours 30 minutes 10 seconds')
        print(td)
        
        # create a Timedelta object from a number of days
        td = pd.Timedelta(days=3, hours=4, minutes=15, seconds=30)
        print(td)
        
        # add a Timedelta to a date or time
        date = pd.to_datetime('2022-02-17')
        new_date = date + td
        print(new_date)
        
        # subtract two dates to get a Timedelta
        date1 = pd.to_datetime('2022-02-17')
        date2 = pd.to_datetime('2022-02-15')
        td = date1 - date2
        print(td)
        
        # perform arithmetic operations with Timedeltas
        td1 = pd.Timedelta('2 days 3 hours 15 minutes')
        td2 = pd.Timedelta('1 day 5 hours 30 minutes')
        print(td1 + td2)
        print(td1 - td2)
        print(td1 * 2)
        ```
        
    - Pandas Groupings and Aggregations
        
        ```python
        import pandas as pd
        
        # create a sample DataFrame
        df = pd.DataFrame({
            'category': ['A', 'B', 'C', 'A', 'B', 'C'],
            'value': [10, 20, 30, 40, 50, 60]
        })
        
        # group the DataFrame by the 'category' column and compute the sum of 'value'
        grouped = df.groupby('category').sum()
        print(grouped)
        
        # group the DataFrame by multiple columns and compute the mean of 'value'
        df = pd.DataFrame({
            'category': ['A', 'B', 'C', 'A', 'B', 'C'],
            'sub_category': ['X', 'Y', 'Z', 'X', 'Y', 'Z'],
            'value': [10, 20, 30, 40, 50, 60]
        })
        grouped = df.groupby(['category', 'sub_category']).mean()
        print(grouped)
        
        # group the DataFrame by the 'category' column and compute multiple aggregations
        grouped = df.groupby('category').agg({'value': ['sum', 'mean', 'max']})
        print(grouped)
        
        # group the DataFrame by the 'category' column and apply a custom aggregation function
        def custom_agg(x):
            return x.max() - x.min()
        grouped = df.groupby('category').agg({'value': custom_agg})
        print(grouped)
        ```
        
        In the above example code, we create a DataFrame with some sample data, and we demonstrate how to group the data by one or more columns and compute summary statistics or aggregations.
        
        We use the **`groupby`** method to group the DataFrame by one or more columns, and then we use aggregation functions such as **`sum`**, **`mean`**, **`max`**, and **`custom_agg`** to compute summary statistics for each group. We can apply multiple aggregations by passing a dictionary of column names and aggregation functions to the **`agg`** method.
        
        In the second example, we group the DataFrame by multiple columns, and compute the mean of the 'value' column for each group. In the third example, we group the DataFrame by the 'category' column and compute multiple aggregations, such as the sum, mean, and max of the 'value' column.
        
        In the fourth example, we demonstrate how to apply a custom aggregation function to the 'value' column for each group. We define the **`custom_agg`** function to compute the difference between the maximum and minimum values of each group, and we pass this function to the **`agg`** method.
        
    - Creating Functions
        
        you can create your own functions to apply to data in a DataFrame.
        
        ```python
        
        '''
        We then apply this function to the 'age' column of the DataFrame using the apply method. The apply method takes a function as input and applies it to each element of the specified column.
        '''
        import pandas as pd
        
        # create a sample DataFrame
        df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'age': [25, 30, 35, 40, 45],
            'gender': ['female', 'male', 'male', 'male', 'female']
        })
        
        # define a function to categorize ages
        def age_category(age):
            if age < 30:
                return 'young'
            elif age < 40:
                return 'middle-aged'
            else:
                return 'old'
        
        # apply the function to the 'age' column of the DataFrame
        df['age_category'] = df['age'].apply(age_category)
        
        print(df)
        
        '''
             name  age  gender age_category
        0    Alice   25  female        young
        1      Bob   30    male  middle-aged
        2  Charlie   35    male  middle-aged
        3    David   40    male          old
        4      Eve   45  female          old
        '''
        ```
        
    - Converting data frame to Different Formats
        
        we can convert data between different formats using various built-in functions.
        
        1. Converting a DataFrame to a Numpy array:
            
            ```python
            import pandas as pd
            import numpy as np
            
            # create a sample DataFrame
            df = pd.DataFrame({
                'A': [1, 2, 3],
                'B': [4, 5, 6],
                'C': [7, 8, 9]
            })
            
            # convert the DataFrame to a Numpy array
            array = np.array(df)
            
            print(array)
            ```
            
             we create a sample DataFrame and use the **`np.array`** function to convert it to a Numpy array.
            
        2. Converting a Numpy array to a DataFrame:
            
            ```python
            
            import pandas as pd
            import numpy as np
            
            # create a sample Numpy array
            array = np.array([
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9]
            ])
            
            # convert the Numpy array to a DataFrame
            df = pd.DataFrame(array, columns=['A', 'B', 'C'])
            
            print(df)
            ```
            
            we create a sample Numpy array and use the **`pd.DataFrame`** function to convert it to a DataFrame.
            
        3. Converting a DataFrame to a dictionary:
            
            ```python
            
            import pandas as pd
            
            # create a sample DataFrame
            df = pd.DataFrame({
                'name': ['Alice', 'Bob', 'Charlie'],
                'age': [25, 30, 35]
            })
            
            # convert the DataFrame to a dictionary
            dictionary = df.to_dict()
            
            print(dictionary)
            
            ```
            
             we create a sample DataFrame and use the **`to_dict`** method to convert it to a dictionary.
            
        4. converting a DataFrame to a CSV file:
            
            ```python
            
            import pandas as pd
            
            # create a sample DataFrame
            df = pd.DataFrame({
                'name': ['Alice', 'Bob', 'Charlie'],
                'age': [25, 30, 35]
            })
            
            # convert the DataFrame to a CSV file
            df.to_csv('data.csv', index=False)
            
            # read the CSV file back into a DataFrame
            new_df = pd.read_csv('data.csv')
            
            print(new_df)
            ```
            
            Iwe create a sample DataFrame and use the **`to_csv`** method to write it to a CSV file. We set the **`index`** parameter to **`False`** to exclude the index column from the output file.
            
            We then read the CSV file back into a new DataFrame using the **`pd.read_csv`** function.
            
        5. Converting a DataFrame to an Excel file:
            
            ```python
            
            import pandas as pd
            
            # create a sample DataFrame
            df = pd.DataFrame({
                'name': ['Alice', 'Bob', 'Charlie'],
                'age': [25, 30, 35]
            })
            
            # convert the DataFrame to an Excel file
            df.to_excel('data.xlsx', index=False)
            
            # read the Excel file back into a DataFrame
            new_df = pd.read_excel('data.xlsx')
            
            print(new_df)
            
            ```
            
            In the above example, we create a sample DataFrame and use the **`to_excel`** method to write it to an Excel file. We set the **`index`** parameter to **`False`** to exclude the index column from the output file.
            
            We then read the Excel file back into a new DataFrame using the **`pd.read_excel`** function.
            
        6. Converting a DataFrame to a JSON file:
            
            ```python
            
            import pandas as pd
            
            # create a sample DataFrame
            df = pd.DataFrame({
                'name': ['Alice', 'Bob', 'Charlie'],
                'age': [25, 30, 35]
            })
            
            # convert the DataFrame to a JSON file
            df.to_json('data.json', orient='records')
            
            # read the JSON file back into a DataFrame
            new_df = pd.read_json('data.json', orient='records')
            
            print(new_df)
            
            ```
            
    - Pandas usecases
        
        Pandas is a powerful data manipulation tool that can be used for a wide range of data analysis and manipulation tasks.
        
        1. Data cleaning and preparation: Pandas can be used to clean and preprocess data before performing analysis, including handling missing data, transforming data types, and removing duplicate data.
        2. Data analysis and exploration: Once the data is clean, Pandas can be used to perform a wide range of data analysis tasks, including calculating descriptive statistics, identifying patterns and trends, and creating visualizations.
        3. Time series analysis: Pandas includes many powerful tools for working with time series data, including time-based indexing and resampling, as well as a number of statistical functions for time series analysis.
        4. Data visualization: Pandas can be used in conjunction with popular data visualization libraries like Matplotlib and Seaborn to create a wide range of charts, plots, and graphs.
        5. Machine learning: Pandas can be used to prepare and preprocess data for machine learning tasks, as well as for creating and training machine learning models.
        6. Financial analysis: Pandas can be used for financial data analysis, including calculating financial indicators like moving averages, and performing simulations and risk analysis.
        7. Web scraping and data ingestion: Pandas can be used to scrape data from web pages, and can also be used to read and ingest data from a wide range of sources, including CSV files, Excel spreadsheets, JSON files, and databases.
    - Pandas and Matplotlib
- Numpy module
    - Introduction to Numpy
        
        NumPy (short for Numerical Python) is a Python library that provides support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. NumPy is a fundamental library for scientific computing in Python, and is widely used for tasks such as image and signal processing, machine learning, and data analysis.
        
        NumPy is built around a powerful array processing system, which allows for efficient computation of large arrays of data. NumPy arrays are homogeneous, meaning that all elements in the array must be of the same data type. This allows for fast computation using optimized, compiled code, and makes NumPy arrays more memory-efficient than Python's built-in data structures.
        
        NumPy also provides a large collection of mathematical functions for working with arrays, including functions for linear algebra, Fourier transforms, random number generation, and more. In addition, NumPy integrates with other scientific computing libraries in Python, such as SciPy and Matplotlib, to provide a comprehensive environment for data analysis and scientific computing.
        
        NumPy is an open-source library, and is available under a permissive BSD license. It is actively maintained by a large community of developers, and new features and bug fixes are regularly added to the library.
        
    - Numpy Arrays
        
        NumPy arrays, also known as ndarrays, are the primary data structure used by the NumPy library. NumPy arrays are homogeneous and multidimensional, meaning that all elements in the array must be of the same data type, and the array can have one or more dimensions.
        
        ```python
        import numpy as np
        
        # create a 1D NumPy array
        arr1 = np.array([1, 2, 3, 4, 5])
        print(arr1)
        
        # create a 2D NumPy array
        arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(arr2)
        
        '''
        [1 2 3 4 5]
        [[1 2 3]
         [4 5 6]
         [7 8 9]]
        '''
        
        # create a 3D NumPy array
        arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        print(arr[0, 1, 1])  # prints 4
        print(arr[1, :, :])  # prints [[5 6] [7 8]]
        
        # create a 4D NumPy array
        arr = np.random.rand(2, 3, 4, 5)
        print(arr[0, 1, 2, 3])  # prints a single value
        print(arr[:, :, :, 0])  # prints a 3D slice of the array
        ```
        
        NumPy arrays have a number of useful attributes, including the shape, which gives the dimensions of the array, and the dtype, which gives the data type of the elements in the array:
        
        ```python
        print(arr1.shape)  # prints (5,)
        print(arr1.dtype)  # prints int64
        
        print(arr2.shape)  # prints (3, 3)
        print(arr2.dtype)  # prints int64
        ```
        
        NumPy also provides a number of functions for creating arrays of a specific shape or with specific values, such as **`numpy.zeros()`**, **`numpy.ones()`**, and **`numpy.arange()`**:
        
        ```python
        zeros = np.zeros((3, 4))
        print(zeros)
        
        ones = np.ones((2, 3))
        print(ones)
        
        sequence = np.arange(0, 10, 2)
        print(sequence)
        
        '''
        [[0. 0. 0. 0.]
         [0. 0. 0. 0.]
         [0. 0. 0. 0.]]
        
        [[1. 1. 1.]
         [1. 1. 1.]]
        
        [0 2 4 6 8]
        '''
        ```
        
        NumPy arrays support a wide range of mathematical operations, and can be indexed and sliced in the same way as standard Python lists. NumPy also provides a number of specialized indexing and slicing operations, such as boolean indexing and fancy indexing, which allow for more advanced data manipulation.
        
    - Numpy Array Indexing
        
        NumPy arrays can be indexed and sliced in a similar way to Python lists, but with additional options and functionality. Indexing and slicing in NumPy is done using square brackets
        
        ```python
        import numpy as np
        
        arr = np.array([1, 2, 3, 4, 5])
        print(arr[0])  # prints 1
        print(arr[3])  # prints 4
        
        arr = np.array([1, 2, 3, 4, 5])
        print(arr[1:4])  # prints [2 3 4]
        
        arr = np.array([1, 2, 3, 4, 5])
        print(arr[-1])  # prints 5
        print(arr[-3:-1])  # prints [3 4]
        
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(arr[0, 0])  # prints 1
        print(arr[1, 2])  # prints 6
        print(arr[:, 1])  # prints [2 5 8]
        
        arr = np.array([1, 2, 3, 4, 5])
        mask = np.array([True, False, True, False, True])
        print(arr[mask])  # prints [1 3 5]
        
        arr = np.array([1, 2, 3, 4, 5])
        indices = np.array([1, 3])
        print(arr[indices])  # prints [2 4]
        ```
        
    - Numpy Mathematical operations
        
        NumPy provides a wide range of mathematical functions that can be applied to arrays. Here are some of the basic mathematical operations that can be performed using NumPy:
        
        ### **Arithmetic Operations**
        
        NumPy arrays can be used for element-wise arithmetic operations such as addition, subtraction, multiplication, and division. These operations can be performed using the corresponding mathematical operators such as +, -, *, /, and // for floor division.
        
        ```python
        import numpy as np
        
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        
        print(a + b)  # [5 7 9]
        print(a - b)  # [-3 -3 -3]
        print(a * b)  # [4 10 18]
        print(a / b)  # [0.25 0.4  0.5]
        print(a // b)  # [0 0 0]
        ```
        
        ### **Trigonometric Functions**
        
        NumPy provides a range of trigonometric functions such as sine, cosine, tangent, etc. that can be applied to arrays.
        
        ```python
        
        import numpy as np
        
        a = np.array([0, np.pi/2, np.pi])
        
        print(np.sin(a))  # [0.         1.         0.        ]
        print(np.cos(a))  # [ 1.000000e+00  6.123234e-17 -1.000000e+00]
        print(np.tan(a))  # [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16]
        ```
        
        ### **Exponential and Logarithmic Functions**
        
        NumPy also provides exponential and logarithmic functions that can be applied to arrays.
        
        ```python
        
        import numpy as np
        
        a = np.array([1, 2, 3])
        
        print(np.exp(a))  # [ 2.71828183  7.3890561  20.08553692]
        print(np.log(a))  # [0.         0.69314718 1.09861229]
        print(np.log10(a))  # [0.         0.30103    0.47712125]
        ```
        
        ### **Aggregation Functions**
        
        NumPy also provides a range of aggregation functions such as sum, mean, median, minimum, maximum, etc. that can be applied to arrays.
        
        ```python
        
        import numpy as np
        
        a = np.array([[1, 2, 3], [4, 5, 6]])
        
        print(np.sum(a))  # 21
        print(np.mean(a))  # 3.5
        print(np.median(a))  # 3.5
        print(np.min(a))  # 1
        print(np.max(a))  # 6
        ```
        
        These are just a few examples of the mathematical operations that can be performed using NumPy. NumPy provides a wide range of mathematical functions that can be applied to arrays.
        
    - Numpy Flattening and reshaping
        
        ### **Flattening Arrays**
        
        Flattening an array means converting a multi-dimensional array into a one-dimensional array. This can be done using the **`ravel()`** or **`flatten()`** method.
        
        ```python
        
        import numpy as np
        
        a = np.array([[1, 2, 3], [4, 5, 6]])
        
        print(a.ravel())  # [1 2 3 4 5 6]
        print(a.flatten())  # [1 2 3 4 5 6]
        ```
        
        The difference between **`ravel()`** and **`flatten()`** is that **`ravel()`** returns a view of the original array, whereas **`flatten()`** returns a new copy of the array.
        
        ### **Reshaping Arrays**
        
        Reshaping an array means changing the shape of the array without changing the data. This can be done using the **`reshape()`** method.
        
        ```python
        
        import numpy as np
        
        a = np.array([1, 2, 3, 4, 5, 6])
        
        print(a.reshape((2, 3)))  # [[1 2 3]
                                  #  [4 5 6]]
        
        b = np.array([[1, 2], [3, 4], [5, 6]])
        
        print(b.reshape((2, 3)))  # [[1 2 3]
                                  #  [4 5 6]]
        ```
        
        In the first example, we reshape a one-dimensional array into a two-dimensional array with shape (2, 3). In the second example, we reshape a two-dimensional array with shape (3, 2) into a two-dimensional array with shape (2, 3).
        
        It is important to note that the size of the reshaped array must match the size of the original array. Otherwise, a **`ValueError`** will be raised.
        
    - Numpy Horizontal and Vertical Stack
        
        NumPy provides two functions for stacking arrays horizontally and vertically: **`np.hstack()`** and **`np.vstack()`**, respectively.
        
        ### **Horizontal Stack**
        
        The **`np.hstack()`** function stacks arrays in sequence horizontally (column-wise). The arrays to be stacked can have different shapes, but they must have the same number of rows.
        
        ```python
        
        import numpy as np
        
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        c = np.hstack((a, b))
        
        print(c)  # [1 2 3 4 5 6]
        
        ```
        
        In this example, we create two one-dimensional arrays **`a`** and **`b`**, and then use **`np.hstack()`** to stack them horizontally into a single one-dimensional array **`c`**.
        
        ### **Vertical Stack**
        
        The **`np.vstack()`** function stacks arrays in sequence vertically (row-wise). The arrays to be stacked can have different shapes, but they must have the same number of columns.
        
        ```python
        
        import numpy as np
        
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])
        c = np.vstack((a, b))
        
        print(c)  # [[1 2]
                  #  [3 4]
                  #  [5 6]
                  #  [7 8]]
        
        ```
        
        In this example, we create two two-dimensional arrays **`a`** and **`b`**, and then use **`np.vstack()`** to stack them vertically into a single two-dimensional array **`c`**.
        
    - Numpy linespace and arrange
        
        NumPy provides two functions for creating arrays of evenly spaced values: **`np.linspace()`** and **`np.arange()`**.
        
        ### **`np.linspace()`**
        
        The **`np.linspace()`** function returns an array of **`num`** evenly spaced numbers over a specified interval **`[start, stop]`**. By default, **`num=50`**.
        
        ```python
        
        import numpy as np
        
        a = np.linspace(0, 1, num=5)
        
        print(a)  # [0.   0.25 0.5  0.75 1.  ]
        
        ```
        
        In this example, we create an array **`a`** of 5 evenly spaced values between 0 and 1.
        
        ### **`np.arange()`**
        
        The **`np.arange()`** function returns an array of values with a given interval and step size. The interval is specified as **`[start, stop)`**, where **`start`** is inclusive and **`stop`** is exclusive.
        
        ```python
        
        import numpy as np
        
        a = np.arange(0, 10, step=2)
        
        print(a)  # [0 2 4 6 8]
        
        ```
        
        In this example, we create an array **`a`** of values between 0 and 10, with a step size of 2. The values in the array are [0, 2, 4, 6, 8], since the endpoint is exclusive.
        
    - Numpy asarray and Random numbers
        
        NumPy provides two useful functions for creating arrays: **`np.asarray()`** and **`np.random.rand()`**.
        
        ### **`np.asarray()`**
        
        The **`np.asarray()`** function converts an input to an array. If the input is already an array, it will be returned unchanged. Otherwise, a new array will be created and returned.
        
        ```python
        
        import numpy as np
        
        a = [1, 2, 3]
        b = np.asarray(a)
        
        print(b)  # [1 2 3]
        ```
        
        In this example, we create a list **`a`** and then use **`np.asarray()`** to convert it to a NumPy array **`b`**.
        
        ### **`np.random.rand()`**
        
        The **`np.random.rand()`** function returns an array of random numbers with a given shape. The values in the array are generated from a uniform distribution between 0 and 1.
        
        ```python
        
        import numpy as np
        
        a = np.random.rand(2, 3)
        
        print(a)  # [[0.24831598 0.11366617 0.88248605]
                  #  [0.11150572 0.19860987 0.48155631]]
        ```
        
        In this example, we create a 2x3 array **`a`** of random numbers using **`np.random.rand()`**. The values in the array are generated from a uniform distribution between 0 and 1.
        
    - Numpy iterations and Transpose
    - Numpy Array Manipulation
    - Numpy and matplotlib
    - Numpy Linear Algebra
    - Numpy String Functions
    - Numpy operations and usecases
    - Numpy Working Examples
- Matplotlib module
    - Introduction to matplotlib
    - Installing matplotlib
    - Generating graphs
    - Normal plottings
    - Generating Bargraphs
    - Histograms
    - Scatter plots
    - Stack plots
    - Pie plots
    - Matplotlib working examples
- Working Examples
