while True:
    number=int(input("Enter a number (stop to Enter 0):"))
    if number==0:
        print("Exiting the program:")
        break
    elif number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    # Write code for print table of Numbers
    while True:
        num =int(input("Enter a number ( negative to stop):"))
        if num<0:
            print("Exiciting a program:")
            break
        print(f"\n Mutliplication table of {num}:")
        for i in range(1,11):
            print(f"{num} x {i} = {num*i}")