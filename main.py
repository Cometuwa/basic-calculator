while 2 > 1:
  print("1 - addition")
  print("2 - subtraction")
  print("3 - multiplication")
  print("4 - division")
  operation = input("Choose operation: ")
  if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print (float(num1) + float(num2))
  elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print (float(num1) - float(num2))
  elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print (float(num1) * float(num2))
  elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print (float(num1) / float(num2))
  else:
    print("error")