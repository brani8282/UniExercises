s=[1,2,3,4,5,6]
print(s)
#s[2]=33
print(s[2])
s1=list('hello')
print(s1)
s2=list((1,2,5,8))
s3=[]
s3.append(10)
s4=s+s3
print(s[-1:])
s5=[(11,22,33),[1,2,3],[4,6,8]]
for i in s:
    print(i)

for i in range(len(s)):
    print(s[i])

s.insert(0,99)
s.pop()
s.remove(5)
print(s)
del s[0]
s.sort(reverse=True)
tup1=(2,4,6,8)
print(tup1[0])
print(tup1)
for smotan in tup1:
    print(smotan)

d={'name':'ivan','l_name':'ivanov'}
d1=dict(name='ivan',l_name='ivanov')
d2=dict([('name','ivan'),('l_name','ivanov')])
d3={}
d3['name']='ivan'
d3['l_name']='ivanov'
d3['l_name']='dimitrov'

keys=list(d.keys())
keys.sort()
print(keys)

set1=set([1,22,3,98,67,1])
print(set1)
set2=set('hello')
for i in set1:
    print(i)

x1={1,3,6,8}
x2={2,3,6,9}
x3=x1|x2
print(x3)
x4=s2-s1
x5=x1&x2
x6=x1^x2
x1.add(4)

  



