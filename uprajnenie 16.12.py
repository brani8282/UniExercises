# f=open('primer.txt','a+')
# cars=['audi\n',"toyota\n","nissan\n"]
# f.write('this is a string\n')
# f.write('hello python\n')
# f.writelines(cars)
# f.seek(0)
# print(f.tell())
# print(f.read())
# print(f.tell())
# f.close()



# f=open('primer.txt','wb+')
# text='hello my friend'
# en=text.encode()
# f.write(en)
# f.seek(0)
# b_data=f.read()


# for byte in b_data:
#     print(chr(byte))


# f.close()
#Задача 1:
# f=open("/Users/brani/Desktop/python/primer.txt","r")
# redove=f.readlines()
# for line in redove:
#     print(line)

# f.close()


f1=open("/Users/brani/Desktop/python/duljinaduma.txt","r")
i=f1.readlines()
if i=='a' or 'e' or 'i' or  'o' or 'u':
    print(i)

f1.close()














#r-четене;w-писане;a-добавяне на нова инф във файла;x-създаване на файл(ако не съществува);
#Ако работим в двоичен режим се поставя b след r например;
#'wb+'-отваряне на двоичен файл за запис и четене
#'ab+'-отваряне на двоичен файл за добавяне и четене