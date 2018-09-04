#Implement a program to get three values from CLA and print the sum of them.

def sum(x,y,z):
    return x+y+z

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))

print("Sum of the given three numbers is: ", sum(a,b,c))