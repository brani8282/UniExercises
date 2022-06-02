#Напишете програма, в която е дефиниран клас със следните характеристики:

#Класът има конструктор, на който се предават две стойности.Тези стойности се присвояват на полетата на обекта от дадения клас. В класа трябва да бъде описан метод, при извикването на който се показват стойностите на полетата на класа. Проверете функционалността на класа , като създадете на негова основа няколко обекта.


# class Class_1:
#     def __init__(self,stoinost1,stoinost2):
#         self.stoinost1=stoinost1
#         self.stoinost2=stoinost2
        
#     def print_info(self):
#         print('Purvata stoinost e:',self.stoinost1,'Vtorata stoinost e:',self.stoinost2)

# stoinosti=Class_1('1','2')
# stoinosti.print_info()


#Напишете програма, в която е описан клас. Обектите на класа трябва да имат поле, представляващо числов списък. Този списък се формира на основата на списък, предаден като аргумент на конструктора. При това от списъка аргумент в списъка поле се включват само числовите елементи(  елементите от други типове се игнорират). Също така трябва да се дефинират два метода :

#Първият метод показва съдържанието на полето списък, а вторият метод изчислява средната стойност на елементите на полето списък

class List:
    def __init__(self,list1):
        self.list1=[]
        for i in list1:
            if type(i)==int:
                self.list1.append(i)

    def print_info(self):
        print("Show what the list contains:",self.list1)

    def average(self):
        suma=sum(self.list1)
        length=len(self.list1)
        print(suma/length)


list2=[1,2,3,4,5,"yes","no"]
object1=List(list2)
object1.print_info()
object1.average()











