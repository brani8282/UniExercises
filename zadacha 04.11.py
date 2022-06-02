#name=input("Enter text:")
#set1=set(name)
#dict={}
#for x in set1:
#    dict[x]=name.count(x)
#print(dict)



number=int(input("Enter num:"))
set=[]
dict={}

for x in range(1,number+1):
    set.append(x)

for x in set:
    dict[x] = set[::1].pop(-x)

print(dict)








    



    



