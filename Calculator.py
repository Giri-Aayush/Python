print("Enter the number 1 :")
num1 = input()
print("Enter the number 2 :")
num2 = input()
print("Operation you want to do (+,-,*,/)")
operation = input()

if operation == "+":
    print("The addition of the numbers is %f" % (float(num1)+float(num2)))

if operation == "-":
    print("The subtraction of the numbers is %f" % (float(num1)-float(num2)))

if operation == "*":
    print("The product of the numbers is %f" % (float(num1)*float(num2)))

if operation == "/":
    print("The division of the numbers is %f" % (float(num1)/float(num2)))