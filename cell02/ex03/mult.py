input1 = int(input("Enter the first number:"))
input2 = int(input("Enter the second number:"))
mult = input1 * input2
print(f"{input1} x {input2} : {mult}")
if mult > 0:
    print("This number is positive.")
elif mult < 0:
    print("This number is negative.")
else:
    print("This number is both positive and negative.")