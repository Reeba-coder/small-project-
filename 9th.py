# T=int(input())
# for _ in range(T):
#     N=int(input())
#     if N%2==0:
#         k=(N-4)//2
#         num=45*(10**k)
#     else:
#         k=(N-5)//2
#         num=205*(10**k)
#     print(num*num)

T = int(input())
for _ in range(T):
    n = int(input())
    if n < 4:
        print("Invalid input: n must be at least 4")
        continue
    if n % 2 == 0:
        if n < 4:
            print("Invalid input for even n")
        else:
            k = (n - 4) // 2
            num = 45 * (10 ** k)
    else:
        if n < 5:
            print("Invalid input for odd n")
        else:
            k = (n - 5) // 2
            num = 205 * (10 ** k)
    print(num * num)
