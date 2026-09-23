with open('input.txt', 'r', encoding='utf-8') as f:
    s = f.read()

o = 0
count = 0

for ch in s:
    if ch in '.!?' and o == 0:
        o = 1
        count += 1
    if o == 1 and ch not in '.!?':
        o = 0

print(count)