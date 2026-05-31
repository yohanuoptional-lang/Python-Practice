import hello


print("HELLO WORLD")
print("yohaan")
print("ECE student")
name= input("enter your name: ")
print("welcome", name)
a=10
b=20
c=a+b
print("the sum of a and b is", c)
if a>b:
    print("a is greater than b")
if a==b:
  
   print("a and b are equal")  
print("b is greater than a")
num1= int(input("enter first number"))
num2= int(input("enter second number"))
if num1>num2:
    print(num1, "is greater than", num2)
elif num1==num2:
    print(num1, "and", num2, "are equal")
else:
    print(num2, "is greater than", num1)
user_input = input("enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    print("you entered the number", number)
else:
    print("invalid input, please enter a number")
age = int(input("enter your age: "))
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
num = int(input("enter a number: "))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
num = int(input("enter a number: "))
if num > 0:
    print(num, "is a positive number")
elif num < 0:
    print(num, "is a negative number")
else:
    print(num, "is zero")
num = int(input("enter a number: "))
if num % 5 == 0 and num % 3 == 0:
    print(num, "is divisible by both 5 and 3")
elif num % 5 == 0:
    print(num, "is divisible by 5")
elif num % 3 == 0:
    print(num, "is divisible by 3")
else:
    print(num, "is not divisible by 5 or 3")
num = int(input("enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print(num, "is divisible by both 2 and 3")
elif num % 2 == 0:
    print(num, "is divisible by 2")
elif num % 3 == 0:
    print(num, "is divisible by 3")
else:
    print(num, "is not divisible by 2 or 3")
x = 1+2*3-4/5**6
print(x)
eee = "hello" + "world"
print(eee)