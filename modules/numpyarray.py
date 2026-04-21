#Mathematical Functions
import numpy as np
a = np.array([0,30,45,60,90])
print ('Sine of different angles:' )
# Convert to radians by multiplying with pi/180
print(np.sin(a*np.pi/180))
print ('Cosine values for angles in array:')
print (np.cos(a*np.pi/180) )
print ('Tangent values for given angles:')
print (np.tan(a*np.pi/180))
print('value of pi')
print(np.pi)
#Functions for Rounding
'''numpy.around()
This is a function that returns the value rounded to the desired precision. The function takes the following parameters.
numpy.around(a,decimals)
The number of decimals to round to. Default is 0. If negative, the integer is rounded to position to the left of the decimal point
Example'''
a = np.array([1.0,5.55, 123, 0.567, 25.532])
print ('Original array:' )
print (a)
print ('After rounding:')
print (np.around(a) )
print (np.around(a, decimals = 1) )
'''numpy.floor()
This function returns the largest integer not greater than the input parameter. The floor of the scalar x is the largest integer i, such that i <= x. Note that in Python, flooring always is rounded away from 0.
Example'''
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print( 'The given array:')
print (a)
print ('The modified array:')
print (np.floor(a))
'''The ceil() function returns the ceiling of an input value, i.e. the ceil of the scalar x is the smallest integer i, such that i >= x.
Example'''
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print( 'The given array:' )
print (a)
print( 'The modified array:' )
print( np.ceil(a))
