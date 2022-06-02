# class FirstClass:
#     x=5
    
# first=FirstClass()
# print(first.x)

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def greetings(self):
#         print('Hello,my name is',self.name)

# class Student(Person):
#     def __init__(self, name,lname):
#         Person.__init__(self,name)
#         self.lname=lname
#     def welcome(self):
#         print('Welcome,',self.name,self.lname)
        


# person1=Person('Kaloyan')
# print(person1.name)
# person1.greetings()
# person1.name='Petyr'
# print(person1.name)
# student1=Student('Stela','Ivanova')
# student1.greetings()
# student1.welcome()


class Person:
    def __init__(self,name,family,age,nationality):
        self.name=name
        self.family=family
        self.age=age
        self.nationality=nationality
    def print_info(self):
        print("My name is:"+self.name,self.family,',my nationality is:',self.nationality)

person1=Person('Ivan','Ivanov','19','bulgarian')
person1.print_info()

class Student(Person):
    def __init__(self,name,family,age,nationality,university,yearofstudy):
        Person.__init__(self,name,family,age,nationality)
        self.university=university
        self.yearofstudy=yearofstudy
        
    def print_info2(self):
        print("My name is:"+self.name,self.family,',my nationality is',self.nationality,'I study at',self.university,'for a',self.yearofstudy)


student1=Student('Ivan','Ivanov','19','bulgarian','Technical Univeristy Sofia','first year.')
student1.print_info2()


class Lecturer(Person):
    def __init__(self,name,family,university,experience):
        self.name=name
        self.family=family
        self.university=university
        self.experience=experience
    def print_info3(self):
        print("My name is:"+self.name,self.family,'I am a lecturer at',self.university,'and my experience is',self.experience)


lecturer1=Lecturer('Petyr','Petrov','Technical Univeristy','25 years')
lecturer1.print_info3()



        









