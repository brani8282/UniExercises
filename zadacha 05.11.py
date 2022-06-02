#напишете програма, в която потребителя запълва списък с числа. после се създава втори списък ,
#който се състои от два елемента: стойността на най- големия елемент в списъка и индекса на този елемент
#в списъка.


num=int(input("enter num"))
l=[]
for x in range(1,num+1):
    n=int(input("second num:"))
    l.append(n)


l2=[max(l), l.index(max(l))]

print(l)
print(l2)


#Напишете програма, в която на основата на текст, въведен от потребителя, се създава кортеж.
#На основата на този кортеж се създава нов кортеж, в него се включват равноотстоящите елементи, започвайки
#от първия(с нулев индекс). Разстоянието между елементите се въвежда от потребителя.
#Пример:
#Enter string: devetstotin
#('d', 'e', 'v', 'e', 't', 's', 't', 'o', 't', 'i', 'n')
#Enter distance: 2
#('d', 'v', 't', 't', 't', 'n')


#text=input("Enter text:")
#tup=tuple(text)
#print(tup)
#num=int(input("Enter distance:"))
#tup2=tup[::num]
#print(tup2)


#Напишете програма, в която се създават два списъка с еднакви размери. На основата на тези списъци
#се формира нов списък, като в него се поставят чрез редуване елементите от първия и елементите от
#втория списък.
#пример : [1,22,67,8]
#         [3,55,89,4]
#изход:   [1,3,22,55,67,89,8,4]


#num=int(input("Enter num1:"))
#set1=[]
#set2=[]
#for i in range(1,num+1):
#    num2=int(input("Nums for set1:"))
#    set1.append(num2)
#print(set1)
#for i in range(1,num+1):
#    num3=int(input("Nums for set2:"))
#    set2.append(num3)
#print(set2)

#Напишете програма, в която на основата на текст въведен от потребителя се създава нов текст, в който в сравнение с изходния думите са разположени в обратен ред.

text2=input("Enter text:")
reversedtext=[]
splittext=text2.split()
for element in splittext[::-1]:
    reversedtext.append(element)

print(reversedtext)




