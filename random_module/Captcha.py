#random
import random
a = random.randint(4,10)
print(a)

b = random.randint(-10,-2)
print(b)

c = random.randrange(1,10,2)
print(c)

#Random - randrange - generate within the range
for i in range(5):
    d = random.randrange(1,10,2)
    print(d,end="")

# Random - uniform - generate any decimal number
e = random.uniform(4,10)
print(e)

#Shuffle
f = [1,2,3,4,5]
random.shuffle(f)
print(f)