a=float(input("Enter first number:"))
op=input("Enter operations(+ _ * /):")
b=float(input("Enter Second number:"))

if op == '+':
    print("result:",a+b)
elif op == '-':
    print("result:",a-b)
elif op == '*':
    print("result:",a*b)
elif op == '/':
    print("result:",a/b if b !=0 else "Cannot divide by 0.")
else:
    print("Invalid Operation.")