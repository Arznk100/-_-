numbers = list(map(int, input().split()))
a = 1
for i in range(len(numbers)):
    a = a * numbers[i]
if len(numbers) == 0:
    print("No numbers provided")
else:
    print(a**(1/len(numbers)))    