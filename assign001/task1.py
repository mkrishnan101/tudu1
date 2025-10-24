'''
ASSIGNMENT 1:
Module 2: Basic Python Concepts

Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
 Expected Output:
The output should include the result of each operation performed, for example:
'''

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Division: ", round((num1 / num2),2))
