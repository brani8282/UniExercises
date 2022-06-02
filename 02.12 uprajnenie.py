# x=10
# try:
#     print(x)
# except NameError:
#     print('x is not defined')
# except:
#     print('Error')
# else:
#     print('ok')
# finally:
#     print('print')



# while True:
#     try:
#         y=int(input('y='))
#         print(y)
#         break
#     except ValueError:
#         print('NOT A VALID NUM!!!TRY AGAIN:')



# def f():
#     x=10/0
#     return x
# try:
#     f()
# except ZeroDivisionError as error:
#     print(error)



# x=-1
# try:
#     if x<0:
#         raise Exception('No numbers below zero')
# except Exception as error:
#     print(error)



#Напишете програмата, в която потребителя въвежда име и възраст . Да се генерира изключение ,ако името съдържа цифри и ако възрастта е по-малка от 0 и по-голяма от 100 .Генерираните изключения да се прихванат и обработят.

name=input("Enter name:")
age=int(input("enter age:"))

try:
    if age<0 or age>100:
        raise ValueError('Not a valid age/name')
    
    elif name==int:
        raise NameError('Not a valid name')
        
    else:
        print(name,age)
        
except:
    print("Error")

    


    


        




