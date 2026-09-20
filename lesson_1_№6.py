with open('text.txt', 'r') as f:
    lines= f.readlines()
    numbers = list(map(int, lines[0].split()))
    op = lines[1][0]
    s = int(lines[2][0])
    for i in range(len(numbers)):
        n = numbers[i]
        j = 0
        a = 0
        while (n > 0):
            a += (n%10) * (int(s)**j)
            j += 1
            n //= 10
        numbers[i] = a

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
    a = 0 
    i = 0
    result10 = result
    while (result > 0):
        a += result%s * 10**i
        result //= s
        i += 1
    
with open('output.txt','w') as f2:
    f2 = open("output.txt", "w", encoding="utf-8")
    f2.write("В десятичной:"+str(result10)+"\n"+"В "+str(s)+"й системе счисления:"+str(a))