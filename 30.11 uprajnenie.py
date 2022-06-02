




#Да се състави програма с използването на клас за обръщането на низ дума по дума


class Convert:
    def __init__(self,text):
        self.text=text
        

    def converter(self):
        
        print("The output text:"+''.join(reversed(self.text)))


object1=Convert(input("Enter text:"))
object1.converter()




















# class Roma:
#     def calc(number_input):
#         decimal = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
#         roman = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

#         result = ''

#         for i in range(0, len(decimal)):
#             count = int(number_input / decimal[i])
#             result += str(roman[i] * count)
#             number_input -= decimal[i] * count
#         print(result)


# number_input = int(input("Enter the number: "))
# obj = Roma
# obj.calc(number_input)




# text=input('Enter text:')
# splittext=text.split()
# reversed=' '.join(reversed(splittext))
# print(text)
# print(reversed)