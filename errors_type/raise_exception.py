# Raise your own exceptions
''' 
Python raises Keyword is used to raise exceptions or errors. The raise keyword raises and error and stops the control flow of the program.
It is used to bring up the current exception in an exception handler so that it can be handled further up the call stack.
'''
a = 9
if a%2 != 0:
    raise Exception("The number shouldn't be an odd integer")
print("Number is even",a)

#Raise with except 
s = "Apple"
try:
    num = int(s)
except ValueError:
    raise ValueError("Text cannot be changed into int for example apple can not change in int")

#Without except class
s = "Apple"
try:
    num = int(s)
except:
    raise


'''
Epost time And Epost date
File handling(Test binding) - csb
'''