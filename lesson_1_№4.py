with open('text.txt', 'r') as f:
    lines= f.readlines()
    numbers = list(map(int, lines[0].split()))
    op = lines[1][0]
    if op == "+":
        result = sum(numbers)
    elif op == "-":
        result = numbers[0]
        for i in range(len(numbers[1:])):
            result -= numbers[i+1]
    else:
        result = 1
        for i in range(len(numbers)):
            result *= numbers[i]
    
with open('output.txt','w') as f2:
    f2 = open("output.txt", "w", encoding="utf-8")
    f2.write(str(result))