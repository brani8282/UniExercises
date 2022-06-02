#Създайте клас,който представя студентите във вашата група.
#Напишете метод,който по подадено име добавя само студенти,които не са записани в списъка от студенти
#Напишете метод remove за триене на студент със слаб успех
#Напишете метод за намиране на среден успех на групата
#Напишете метод за намиране на максимален успех на групата и минимален
#Създайте метод move,който да премества студенти с начална буква А в нов списък и се създаде метод delete,който трие студентите в началния списък.



class Students:
    def __init__(self,name,lastname,group,grades):
        self.name=name
        self.lastname=lastname
        self.group=group
        self.grades=grades
    def info(self):
        print("My name is",self.name,self.lastname,"I am in",self.group,'group',"and my success is:",self.grades)

    def add(self,list1):
        self.list1=list1
        list1=[]
        
            
        
        
    
        
student1=Students('Ivan','Ivanov','45','5,50')
student2=Students('Kaloyan','Grigorov','45','5,47')
student3=Students('Petar','Petrov',"45","4,20")
student4=Students('Georgi','Georgiev','45','3,35')


student1.info()
student2.info()
student3.info()
student4.info()



