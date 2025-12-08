s1 = int(input("Enter marks of Sub1: "))
s2 = int(input("Enter marks of Sub2: "))
s3 = int(input("Enter marks of Sub3: "))

tm = s1+s2+s3

per = ((tm) / 300) * 100
print(per)

if(per >= 40 and s1>33 and s2>33 and s3>33):
    print("You are pass")
else:
    print("You are fail")