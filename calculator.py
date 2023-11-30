#simple calculator 

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y

a = float (input("Enter first number: "))
b = float (input("Enter second number: "))
op = input("Enter operation: ")

if op == "+":
    print(add(a,b))
    
elif op == "-":
    print(sub(a,b))
    
elif op == "*":
    print(mult(a,b))
    
elif op == "/":
    print(div(a,b))
    
else:
    print("Invalid operation")
    



