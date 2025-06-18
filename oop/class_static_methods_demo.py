class Calculator:
   calculation_type = "Arithmetic Operations"

   @staticmethod 

   def add(a,b):
      return a + b
   
   @classmethod 

   def multiply(cls, a, b):
      
    print(f"Calculation type: {cls.calculation_type}")
    return a * b 
   
print("Sum:", Calculator.add(7, 8))             
print("Product:", Calculator.multiply(5, 10))  