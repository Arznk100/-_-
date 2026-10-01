def prost(x):
    i = 2
    while x > 1:
        if x % i == 0:
            print(i, end=' ')
            x = x // i
        else:
            i += 1
N = int(input())
prost(N)

