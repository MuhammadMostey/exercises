import calculatorArt
print(calculatorArt.logo)

def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiplication(a,b):
  return (a * b)

def division(a,b):
  return a / b

operations = {
  '+': add, 
  '-': subtract, 
  '*': multiplication, 
  '/': division
}

def calculator():
  remaining = True
  firstNum = float(input("What is the first Number? "))

  while (remaining):
    for symbol in operations:
      print(symbol)
    operator = input("Choose an operator: ")
    secondNum = float(input("What is the second Number? "))
    
    if operator not in operations:
      print("\nPlease Enter a correct operation")
      
    result = operations[operator](firstNum, secondNum)
    print(f"\n{firstNum} + {secondNum} = {result}")
    
    con = input(f"\nType y to continue calculating with {result} or type n to start a new calculation: ").lower()
    if (con == 'y'):
      firstNum = result
    else:
        remaining = False
        remainingAnswer = input("do you want to do a new one? y or n? ").lower()
        if(remainingAnswer == 'y'):
          remaining = False
          calculator()

calculator()