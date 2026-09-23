a = list(map(int, input().split()))
max = 0
number = 0
for i in range(len(a)):
    if (a.count(a[i]) > max):
        max = a.count(a[i])
        number = a[i]
print(number)