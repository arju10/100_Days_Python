'''
String Slice
'''
# Lenghth of a string
country = "Dhaka, Bangladesh"
print(len(country))

name = "Ahmed"
print(name[0]) # pinting first character (A) 
print(name[0:]) # print all (Ahmed)
print(name[0:3]) # print 0 to 3 (Ahm)
print(name[:4])  # print 0 to 4 (Ahme)
print(name[0:5:2]) # print 0 to 5 with step 2 (Amd)
print(name[:])  # print all (Ahmed)
print(name[::2]) # print all with step 2 (Amd)
print(name[::-1]) # print all in reverse (dehmaA)
print(name[::-2]) # print all in reverse with step 2 (dehmaA)
print(name[-4:-2]) 

# Convert lower to upper case
name = "Ahmed"
upper = name.upper()
print(upper) # AHMED

# Convert upper to lower case
lower = name.lower()
print(lower) # ahmed

# !!! String is immutable !!!
name  = '!Huzaifa!!!!!!!!!'
print(name.rstrip("!"))  # remove trailing characters

print(name.replace("Huzaifa", "Ahmed")) # replace characters

name = "huzaifa ahmed"
print(name.split(" ")) # split string

print(name.capitalize()) # capitalize first character

print(len(name)) # center string
print(len(name.center(50)))

print(name.count("a"))  # count characters 
print(name.endswith("d")) # check ending
print(name.endswith("a", 0, 6)) # check ending with range

print(name.find("a")) # find characters
print(name.find("t")) # If not found return -1
print(name.index("a")) # find characters
# print(name.index("t")) # If not found return error 
'''
Traceback (most recent call last):
  File "/home/runner/workspace/main.py", line 50, in <module>
    print(name.index("t")) # If not found return error
          ^^^^^^^^^^^^^^^
ValueError: substring not found
'''
print(name.isalnum()) # check alphanumeric\
print(name.isalpha()) # check alphabet
print(name.islower()) # check lower case
print(name.isupper()) # check upper case
print(name.isprintable()) # check printable
print(name.isspace()) # check space
print(name.istitle()) # check title
print(name.swapcase()) # swap case
print(name.title()) # title case