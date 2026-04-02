#Calculadora
a = float(input("número 1:"))
b = float(input("número 2:"))
op = input ("operação +, -, *, /")

if op == "+":
 print(a + b)
elif op == "-":
 print(a - b)
elif op == "*":
 print(a * b)
elif op == "/":
 print(a / b)
else:
 print("Operação invalida")