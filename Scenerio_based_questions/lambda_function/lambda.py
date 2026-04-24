#LAMBDA
f=lambda x:x*x
print(f(10))
f= lambda x,y:x+y
print(f(10,2))

'''x=int(input())
y=int(input())
f=lambda x:x*x
print(f(x))
f= lambda x,y:x+y
print(f(x,y))'''

#lambda with list ,tuple
'''x=eval(input())
y=eval(input())
f=tuple(map(lambda x:x*x,x))
print(f)
f= tuple(map(lambda x,y:x+y,x,y))
print(f)#(same for list)'''

#lambda with filter
'''x=eval(input())
f=list(filter(lambda x:(x%2!=0),x))
print(f)'''

'''x=eval(input())
f=tuple(filter(lambda x:(x%2==0),x))
print(f)'''

'''x=eval(input())
f=list(filter(lambda x:(x>0),x))
,3print(f)'''

#lambda with two list
'''x=input()
a=eval(x)
y=input()
b=eval(y)
l1=list(map(lambda x:x in a,b))
print(l1)'''

'''x=input()
a=eval(x)
y=input()
b=eval(y)
l1=tuple(map(lambda x,y:x*y ,a,b))
print(l1)'''

#from functools import*

'''from functools import*
a=eval(input())
l=reduce(lambda y,x : x*y,a)
print(l)'''


#mcqs of lambda

#32
'''names=["alice","bob","chalie","devid"]
sorted_names=sorted(names,key = lambda x:x[-1])
print(sorted_names)'''

#31


