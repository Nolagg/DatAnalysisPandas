# DatAnalysisPandas
Pandas is Python’s module for working with tabular data (data that has rows and columns). Pandas gives you the functionality of programs like SQL or Excel along with all the power of Python. Data Analysts use Python to ingest, organize, and analyze large data sets

## Lambdas
In Python, a lambda function is a one-line shorthand for function. A simple lambda function might look like this:

add_two = lambda my_input: my_input + 2

1. The function is stored in a variable called add_two
2. lambda declares that this is a lambda function (if you are familiar with normal Python functions, this is similar to how we use def to declare a function)
3. my_input is what we call the input we are passing into add_two
4. We are returning my_input plus 2 (with normal Python functions, we use the keyword return)

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'

1. Declare lambda function with an input called grade (lambda grade:)
2. Return 'Got an A!' if this statement is true:
grade >= 90
3. Otherwise, return 'Did not get an A...' if this statement is not true:
grade >= 90