intro = input("Hello! This is caltulator!You can add, substact, multiply and divide!Press Enter to continue")

a = int(input("What number would the first number be? "))

b = int(input("What number would the second number be? "))

oper = input("What operation would you like to use? ")

if oper == "+":
    
	print(a, "+", b, "=", a + b)

elif oper == "-":
    
	print(a, "-", b, "=", a - b)

elif oper == "*":
    
	print(a, "*", b, "=", a * b)

elif oper == "/":
    
	print(a, "/", b, "=", a / b)

else:
   
	print("Error")