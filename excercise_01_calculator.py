'''
Excersise 01:
Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!
'''  
a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))

sum = a+b
sub = a-b
mul = a*b
div = a/b
mod = a%b


print("Summition of",a,"and",b,"is",sum)
print("Subtraction of",a,"and",b, "is",sub)
print("Multiplication of",a,"and",b,"is",mul)
print("Division of",a,"and",b,"is",div)
print("Modulus of",a,"and",b,"is",mod)