print("---Simple Calculator---")
print("Enter two numbers: ")
a=int(input("Num1: "))
b=int(input("Num2: "))
print("Enter your choice(1=+, 2=-, 3=*, 4=/)")
choice=int(input("Choice: "))
match choice:
    case 1:
        print("Sum is: ")
        f"Sum is: {(a+b)}"
        print(a+b)
    case 2:
        print("Difference is: ")
        f"Difference is: {(a-b)}"
        print(a-b)
    case 3:
        print("Product is: ")
        f"Product is: {(a*b)}"
        print(a*b)
    case 4:
        if b!=0:
            print("Division is: ")
            f"Division is: {a/b}"
            print(a/b)
        else:
            print("Division by zero is not allowed")
    case _:
        print("Invalid choice")