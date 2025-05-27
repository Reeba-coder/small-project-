def factorial(n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))

def fibonacci(n):
    fib=[0,1]
    while len(fib)<n:
        fib.append(fib[-1]+fib[-2])
    return fib
num=10
print(fibonacci(num))

word1="abcde"
word2="pqr"
merg=" "
i,j=0,0
while i< len(word1) and j<len(word2):
    merg+=word1[i]+word2[j]
    i+=1
    j+=1
while i<len(word1):
    merg+=word1[i]
    i+=1
while j<len(word2):
    merg+=word2[j]
    j+=1
print(merg)

s="abcd"
t="abcde"
i=0
while i<len(s):
    if s[i] != t[i]:
        print(t[i])
        break
    i+=1
if i == len(s):
    print(t[i])
#     {class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         result = 0
#         for char in s:
#             result ^= ord(char)
#         for char in t:
#             result ^= ord(char)
#         return chr(result)

# }