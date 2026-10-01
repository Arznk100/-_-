def tree(N, c):
    for i in range(1,N//2 + N%2+1):
        for j in range(i):
            print(c, end=' ')
        print(end='\n')
    for i in range(N//2):
        for j in range(N//2 - i):
            print(c, end=' ')
        print(end='\n')
N, c  = map(str, input().split())
tree(int(N),c)
