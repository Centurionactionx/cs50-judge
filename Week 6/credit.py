a = int(input("Number: "))
s = str(a)[::-1]
val = False
amex = [37, 34]
mas = [51, 52, 53, 54, 55]

total = 0
for i in range(len(s)):
    dig = int(s[i])
    if i % 2 == 1:  
        dig *= 2
        dig = dig // 10 + dig % 10
    total += dig

if total % 10 == 0:
    val = True
if val == False:
    print("INVALID")
else:
    if (int(str(a)[:2]) in amex) and len(str(a)) == 15:
        print("AMEX")
    elif (int(str(a)[:2]) in mas) and len(str(a)) == 16:
        print("MASTERCARD")
    elif (len(str(a)) == 16 or len(str(a)) == 13) and int(str(a)[:1]) == 4:
        print("VISA")
    else:
        print("INVALID")
