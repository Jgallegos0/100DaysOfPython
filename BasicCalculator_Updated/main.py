from art import logo

def addition(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": addition,
  "-": subtract,
  "*": multiply,
  "/": divide
}

print(logo)

def calculator():
  num1 = float(input("Enter the first number: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation = input("Pick a function from above: ")
    num2 = float(input("Enter the second number: "))

    calculation_function = operations[operation]
    answer = round(calculation_function(num1, num2),2)

    print(f"{num1} {operation} {num2} = {answer}")
    if input(f"Do you want to continue with {answer}? 'y' or 'n':\n") == "y":
      num1 = answer
      
    else:
      should_continue = False

calculator()