n = int(input())  # 1palindrome
mytemp = n
p = 0
while (n > 0):
    dig = n % 10
    p = p * 10 + dig
    n = n // 10
if (mytemp == p):
    print("YES")
else:
    print("NO")
