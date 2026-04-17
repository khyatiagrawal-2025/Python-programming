import numpy
a=numpy.arange(9, dtype=numpy.int_).reshape(3,3)
print(a)
b=numpy.array([10,20,30], dtype=int)
print(b)
print("dot=", numpy.dot(a,b))
'''The numpy.dot() method, when applied to a 2D matrix and a 1D array, performs a matrix-vector multiplication. Specifically, it computes the
dot product of each row of the matrix with the vector.

The result is a new vector where each element i is calculated as the sum of the products of the elements in the i-th row of a and the corresponding elements in b.

First element (Row 0 ⋅ Vector b):
(0×10)+(1×20)+(2×30)=0+20+60=80

Second element (Row 1 ⋅ Vector b):
(3×10)+(4×20)+(5×30)=30+80+150=260

Third element (Row 2 ⋅ Vector b):
(6×10)+(7×20)+(8×30)=60+140+240=440
3. Final Result

Combining these results into a single array, the output of numpy.dot(a, b) is:
dot=[80,260,440]'''
d=numpy.array([1,2,3])
print("product=", numpy.prod(d))
