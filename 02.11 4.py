import random
s=[random.randint(10,20)for i in range(16)]
for i in range(0,22,3):
    s.insert(i+2,s[i]+s[i+1])
print(s)