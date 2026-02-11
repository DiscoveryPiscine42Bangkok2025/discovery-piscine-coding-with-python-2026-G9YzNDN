input1 = int(input("Enter number less than 25\n"))
if input1 > 25:
        print("Error")
else:
    while input1 <= 25:
        print(f"Inside the loop, my variable is {input1}")
        input1 += 1