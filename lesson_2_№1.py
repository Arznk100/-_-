n = int(input())
numbers = list(map(int,input().split()))
numbersFull = [i for i in range(1,n+1)]
print(sum(numbersFull)-sum(numbers))