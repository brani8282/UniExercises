n=int(input("Enter num:"))
list1=[]
list2=[]

for i in range(0,n):
    num=int(input("Vuvedete chislo:"))
    if num%3==0 and num%2==1:
        list1.append(num)
    elif num%2==0:
        list2.append(num)
    else:
        print("Error")

print("list1:",list1)
print("list2:",list2)
max_nechetni=max(list1)
print("maximum:",max_nechetni)
min_nechetni=min(list1)
print("Minimum:",min_nechetni)
suma_chetni=sum(list2)
average_chetni=suma_chetni/len(list2)
print("Suma:",suma_chetni)
print("Average:",average_chetni)
