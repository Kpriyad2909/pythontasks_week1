from calculator_base import calci
#child class
class child(calci):
 #methods
 def add(self):
      if self.op == '+':
        print(f"Result is {(self.a + self.b):.2f}")
    
 def sub(self):
      if self.op == '-':
        print(f"Result is {(self.a - self.b):.2f}")
 def multiply(self):
      if self.op == '*':
        print(f"Result is {(self.a * self.b):.2f}")
 def divide(self):
      if self.op == '/':
          if self.b == 0:
           print("Invalid number,cannot divide by 0") 
          else:  
            print(f"Result is {(self.a / self.b):.2f}")
        
result = child()
result.add()
result.sub()
result.multiply()
result.divide()