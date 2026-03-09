def calculator ():
    print("=== Simple calculator ===")
    op =float (input("Enter first number: "))
    num2 = float(input("Enter second number:"))
    if op == '+': result = num1 + num2
    elif op=='-' : result = num1 - num2
    elif op =='*': result = num1 * num2
       if num2 == 0:
        print("error: Division by zero!")
        return
    result = num1 / num2
else:
print("Invalid operator!")
return 
print (f"Result:{num1} {op} {num2} = {result}
       calculator()
       