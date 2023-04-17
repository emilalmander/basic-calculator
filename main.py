def add (a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer)) 

def subtraction(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer)) 

def multiplication(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer)) 

def division(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer)) 


print(" A, addition")
print(" B, subtraction")
print(" C, multiplication")
print(" D, division")
print(" E, exit")

choice = input("input your choice: ")

if choice == "A" or choice == "a":
    print("addition")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    add(a, b)
elif choice == "b" or choice == "B":
    print("subtraction")
    a = int(input("input first number: "))
    b = int(input("please input second number: "))
    subtraction(a, b)
elif choice == "c" or choice == "C":
    a = int(input("input first number: "))
    b = int(input("please input second number: "))
    multiplication(a, b)
elif choice == "d" or choice == "D":
    a = int(input("input first number: "))
    b = int(input("please input second number: "))
    division(a, b)

elif choice == "e" or choice == "E":
    print("program ended")
    quit()





