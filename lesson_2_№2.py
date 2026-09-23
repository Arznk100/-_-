G, s = input().split()
G = int(G)
answer = ''
for i in range(len(s)//G):
    answer += s[i*G:(i+1)*G][::-1]
print(answer)