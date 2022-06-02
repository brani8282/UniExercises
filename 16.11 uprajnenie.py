
#Да се състави програма с функция, която получава като аргумент числов списък и връща като резултат друг списък в който са включени само нечетните числа от списъка аргумент.


l1=[]
l2=[]
def f1(l1):
    for i in range(len(l1)):
        if l1[i]%2!=0:
            l2.append(l1[i])
    print(l2)
l1=[1,2,3,4,5,6]
f1(l1)

#Напишете програма с функция с произволен брой числови аргументи, която връща като резултат списък от 3 елемента,средно аритметично,максимална и минимална стойност на аргументите

import random
list1=[]
list2=[]
suma=0
n=random.randint(1,15)
for i in range(1,n+1):
    list1.append(i)
    suma=suma+i
    average=suma/len(list1)
    maximum=max(list1)
    minimum=min(list1)
    

def function(list2):
    list2.append(average)
    list2.append(maximum)
    list2.append(minimum)
    print("List with-average,max,min:", list2)
    

function(list2)




    






    









