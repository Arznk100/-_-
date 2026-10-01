def fib(x, a):
    if x == 0:
        a[0] = 0
        return 0
    elif x == 1:
        a[1] = 1
        return 1
    else:
        result = fib(x - 1, a) + fib(x - 2, a)
        a[x] = result
        return result
a={}
N = int(input())
print(fib(N, a))