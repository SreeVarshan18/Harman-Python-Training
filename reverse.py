a = int(input("Enter a number "))
reversenum = 0
while a>0:
    reminder = a % 10
    reversenum = (reversenum * 10) + reminder
    a = a // 10
print(reversenum)