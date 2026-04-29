#Explicit exception handling
#clauses 
try:                                   #Without try we can not make exceptions.
    a = [1,2,3,4,5]
    print(a[6])
except IndexError:
    print("List index position is 0.4")
else:                                   #else is opposite of exception - means if there is a error in code then except output will print and if there is no error in code then else will be execute.
    print(a[4])
finally:                                #finally is basically used to close or end the program - it always executes...!
    print(a*3)