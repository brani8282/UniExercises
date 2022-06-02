# import json
# py_data={'name':'petko','age':22,'married':True,'child':None}
# with open('C:\Users\brani\Desktop\python\json33.json','w') as f:
#     json.dump(py_data,f)
# with open('C:\Users\brani\Desktop\python\json33.json','r') as f1:
#     p=json.load(f1)
#     print(p)


# import pickle
# f=open('C:/Users/brani/Desktop/python/newfile.txt','wb+')
# list1=['25','44','66']
# ps=pickle.dumps(list1,f)


class Student():
    def __init__(self, name,id,language):
        self.name=name
        self.id=id
        self.language=language
    def get_id(self):
        print('You id is:',self.id)
    def get_name(self):
        print('Your name is:',self.name)
    def get_language(self):
        print('Your programming language is:',self.language)
    
    def add_student(student):
        open_file=open("C:/Users/brani/Desktop/python/newfile.txt","a")
        open_file.write(student.name+'\t'+student.id+'\t'+student.language+'\n')
        open_file.close()


student1=Student('Petar','45','python')
student1.get_name()
student1.get_id()
student1.get_language()
student1.add_student()














