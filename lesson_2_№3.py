s = str(input())
kriteri1 = 1
kriteri2 = 1
for i in range(len(s)//2+len(s)%2):
    if(((s[i] == 'E') and (s[len(s)-1-i] == '3')) or ((s[i] == '3') and (s[len(s)-1-i] == 'E'))):
        kriteri2 = 0
    elif(((s[i] == 'S') and (s[len(s)-1-i] == '2')) or ((s[i] == '2') and (s[len(s)-1-i] == 'S'))):
        kriteri2 = 0
    elif(((s[i] == 'Z') and (s[len(s)-1-i] == '5')) or ((s[i] == '5') and (s[len(s)-1-i] == 'Z'))):
        kriteri2 = 0
    elif(((s[i] == 'J') and (s[len(s)-1-i] == 'L')) or ((s[i] == 'L') and (s[len(s)-1-i] == 'J'))):
        kriteri2 = 0
    elif(s[i] not in ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']):
        kriteri1 = 0
    elif(s[i] != s[len(s)-1-i]):
        kriteri1 = 0
        kriteri2 = 0
if(kriteri1 == 0 and kriteri2 == 0):
    print(s+ " is not a palindrome")
elif(kriteri1 == 0 and kriteri2 == 1):
    print(s+ " is a regular palindrome")
elif(kriteri1 == 1 and kriteri2 == 0):
    print(s+ " is a mirrored string")
elif(kriteri1 == 1 and kriteri2 == 1):
    print(s+ " is a mirrored palindrome")
    
    