#def f1(name='ivan',city='sofia'):
#    print(f"Hello {name}, you are from {city}")
#    return

#def f2():
#    print('hello world!!!')

#def suma(a,b):
#   return a+b

#f2()
#f1('Kaloyan','Sofia')
#f1(name='Fredi',city='Plovdiv')
#f1(name='maria')
#f1()
#num1=int(input("num1= "))
#num2=int(input("num2= "))
#result=suma(num1,num2)
#print(result)



figure=input('triangle,square or rectangle:')

def lice(strana1):
    return (strana1)**2
    
def lice2(stranatr,visochina):
    return (stranatr*visochina)/2

def lice3(stranarec1,stranarec2):
    return (stranarec1*stranarec2)
    
   
if figure=='square':
    strana1=int(input("Vavedete stoinnost1:"))
    licekvadrat=lice(strana1)
    print('Liceto na kvadrata e:',licekvadrat)
    
elif figure=='triangle':
    stranatr=int(input("Vavedete stoinost:"))
    visochina=int(input("Vavedete visochina"))
    licetr=lice2(stranatr,visochina)
    print('Liceto na triugulnika e:',licetr)
    
elif figure=='rectangle':
    stranarec1=int(input("Vavedete stoinost1:"))
    stranarec2=int(input("Vavedete stoinost2"))
    licerec=lice3(stranarec1,stranarec2)
    print('Liceto na pravougulnika e:',licerec)
else:
    print("WRONG OR NO FIGURE ENTERED!!!")
    





    
        
        


    
    