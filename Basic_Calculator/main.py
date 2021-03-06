import art
def calculate_function(first_number, second_number):
  """Will add, subtract, divide, or multiply 2 numbers"""
  first_number_int = int(first_number)
  second_number_int = int(second_number)
  sign = input("Pick a function:\n + - / *\n")
    # + - / *
  if sign == "+":
    plus = first_number_int + second_number_int
    print(plus)
  elif sign == "-":
    minus = first_number_int - second_number_int
    print(minus)
  elif sign == "/":
    divide = first_number_int / second_number_int
    divide_float = round(float(divide),2)
    print(divide_float)
  else:
    if sign == "*":
      multiply = first_number_int * second_number_int
      print(multiply)
print(art.calculator)
number, number_two = input("Enter two numbers, leave a space in between:\n").split()
calculate_function(number, number_two)


