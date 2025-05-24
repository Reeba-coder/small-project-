n=10
sum=0
for i in range(1,n+1):
    sum=sum+i
    print ("Sum of first 10 numbers is",sum)
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is Even")
# Print pyramid
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

