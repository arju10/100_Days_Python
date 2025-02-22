'''
Modules: Modules is used to import other files.
There are two types of modules:
1. Built-in modules: These modules are already installed with python.
2. External modules: These are modules that are installed using pip.
'''
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file