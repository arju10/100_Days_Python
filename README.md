# Modules
**Modules:** Modules is used to import other files.</br>
There are two types of modules:</br>
**1. Built-in modules:** These modules are already installed with python.</br>
**2. External modules:** These are modules that are installed using pip.

**Example:** 
```bash
pip install pandas
```
It will install pandas library.And It is a built-in module.

Using of Pandas Module
```python
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file
```

# print() Statement
**print():** print() can be used to print something on the console in python.

**Example:**
```python
print("It will print string") # It will print string
print(18 * 2) # It will print 36. Means mulplication of 18 and 2
print("Division: ", 18 / 2) #  9. Means division of 18 and 2
```
**Output:**</br>
It will print string </br>
36 </br>
9.0 </br>
