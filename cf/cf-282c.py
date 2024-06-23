s1 = input()
s2 = input()

zero1 = s1[0] == "0" and len(set(s1)) == 1
zero2 = s2[0] == "0" and len(set(s2)) == 1

if len(s1) != len(s2):
    print("NO")
elif zero1 and zero2:
    print("YES")
elif (zero1 and not zero2) or (zero2 and not zero1):
    print("NO")
else:
    print("YES")
