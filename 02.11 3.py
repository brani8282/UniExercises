tup=()
num=int(input("Stoinost:"))
for i in range(1,num+1):
    tup+=(i,)
    desc_tup=sorted(tup,reverse=True)
print(tup)
print(desc_tup)
