N = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
print(numbers[N // 2+ N % 2 -1])