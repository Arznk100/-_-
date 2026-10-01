def evklid(x, y):
    if(x%y == 0 or y%x == 0):
        return min(x, y)
    else:
        return evklid(y, x % y)
N,M= map(int, input().split())
print(evklid(N, M))