with open('input.txt', 'r', encoding='utf-8') as f:
    s = f.read()
answer = ""
for i in range(len(s)): 
    if((i != 0) and (s[i] in 'уеыаоэяию') and (s[i-1] not in 'уеыаоэяию .,!? \n')):
        answer += s[i]+'с'+s[i]
    else:
        answer += s[i]
print(answer)