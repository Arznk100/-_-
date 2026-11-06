N = int(input())
INF = 10**9
mass = [INF] * (N + 1)
mass[1] = 0
for i in range(1, N+1):
    if i * 2 < N+1:
        mass[i*2] = min(mass[i*2], mass[i] + 1)
    if i * 3 < N+1:
        mass[i*3] = min(mass[i*3], mass[i] + 1)
    if i + 1 < N+1:
        mass[i+1] = min(mass[i+1], mass[i] + 1)
print(mass[N])