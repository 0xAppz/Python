#1. ADD
#2. SUBSTRACT
#3. MULTIPLY
#4. DIVIDE

print("Select an operation to Perform:")
print("1. ADD ")
print("2. SUBTRACT ")
print("3. MULTIPLY ")
print("4. DIVIDE ")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    sum = int(num1) + int(num2) 
    print("The sum is ", sum)
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    sum = int(num1) - int(num2)
    print("The sum is ", sum)
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    sum = int(num1) * int(num2)
    print("The sum is ", sum)
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    sum = int(num1) / int(num2)
    print("The sum is ", sum)
else: 
    print("Invalid Entry")

    print("Done")