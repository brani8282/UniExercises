
#Да се състави програма при която потребителя въвежда n числа от клавиатурата в интервала от 1 до 1000
#програмата изчислява средноаритметичната стойност на всички нечетни числа и произведението на всички четни числа,чиято стойност е по-голяма от 10 


#Seminarno upr

n=int(input('Broi chisla:'))
average=0
proizvedenie=1
if n>=1 or n<=1000:

    for i in range(0,n):
        num=int(input('Enter a number from 1 to 1000:'))

        if num%2!=0:
            average+=num/n


        elif num>=10 and num%2==0:
            proizvedenie*=num


        elif num<10 and num%2==0:
            print("Incorrect number!!!")

        else:
            print("Wrong!!!")

print("The average is:",average)
print("Proizvedenieto e:",proizvedenie)


#Laboratorno upr.

# def f1(*n):
#     s=0
#     for a in range(len(n)):
#         s+=n[a]
#     return s
# print(f1(1,2,66))
# print(f1(22,33,44,1,3,5))
# print(f1())


# def f1(text):
#     return text.upper()
# def f2(text):
#     return text.lower()

# def f3(func):
#     res=func('Hello World!!!')
#     print(res)


# f3(f2)
# f3(f1)


#Напишете програма, в която се създава  функция. 
#Функцията получава като аргумент числов списък и връща като резултат друг списък, в който са включени само нечетните числа от списъка аргумент.

l1=[]
l2=[]
def f1(l1):
    for i in range(len(l1)):
        if l1[i]%2!=0:
            l2.append(l1[i])
    print(l2)
l1=[1,2,3,4,5,6]
f1(l1)

#Напишете програма,в която е описана функция,връщаща като резултат второто по големина число в списъка, предаден като аргумент на функцията

#list=[1,2,3,5,4,10,9]
#list.sort(reverse=True)
#maximum=max(list)
#def f1(list):
#    return maximum
#print(maximum)
#f1(list)




        







    
        


        
    
    




