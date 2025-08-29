echo "# simple-calculator" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/eesha-s430/simple-calculator.git
git push -u origin main

#Name: Eesha Sivakumar
#Project: Simple Calculator
#Date: August 28, 2025
#Description: simple calculator that uses basic arithmetic operations to solve equations

#define functions
def add (x, y):
  "this function adds two numbers"
  return x + y

def subtract (x, y):
  "this function subtracts two numbers"
  return x - y

def multiply (x, y):
  "this function multiplies numbers"
  return x * y

def divide (x, y):
  "this function divides two numbers"
  return x / y

#get input from user
print ("choose an operation.")
print ("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input("enter choice (1/2/3/4):")

float1 = int(input("enter the first number: "))
float2 = int(input("enter the second number: "))

if choice == "1":
  print(num1, "+",num2, "=" , add(num1,num2))
elif choice == "2":
    print(num1, "-",num2, "=" , subtract(num1,num2))
elif choice == "3":
    print(num1, "*",num2, "=" , multiply(num1,num2))
elif choice == "4":
    print(num1, "/",num2, "=" , divide(num1,num2))

else: 
  print("invalid input")
  






