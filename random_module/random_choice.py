#Python3 program to demonstrate the use of
#choice() method

#import random
import random

#prints a single random value from the list
list1 = [1,2,3,4,5,6]
print(random.choice(list1))

#prints a random item from the string
string = "geeks"
print(random.choice(string))

#prints more random items from the tuple accordingly
tuple1 = (1,2,3,4,5)
print(random.choices(tuple1,k=3))