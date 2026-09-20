N,b,c = map(int,input().split())
k = 0 
i = 0
while N > 0:
    k += N%10 *(b**i)
    N //= 10
    i += 1
s = 0
i = 0
while k > 0:
    s += k%c * 10**i
    k //= c
    i += 1
print(s)