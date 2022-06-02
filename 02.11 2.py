tup=()
n=int(input("Stoinost:"))
for i in range(n):
    m=int(input("Stoinost 2:"))
    tup+=(m,)
    asc_tup=sorted(tup)
    desc_tup=sorted(asc_tup,reverse=True)
print(tup)
print(asc_tup)
print(desc_tup)



