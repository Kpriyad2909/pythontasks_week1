import calculator_base
#user input
a = float(input("Enter the first value:"))
b = float(input("Enter the second value:"))
print("Enter the operator")
operator = input()
#conditions
if operator == '+':
 print(f"Result is {calculator_base.add(a,b):.2f}")
elif operator == '-':
 print(f"Result is {calculator_base.subtract(a,b):.2f}")
elif operator == '*':
 print(f"Result is {calculator_base.multiply(a,b):.2f}")
elif operator == '/':
 print(f"Result is {calculator_base.divide(a,b):.2f}")
else:
  print("Invalid operator")

      

      
    






