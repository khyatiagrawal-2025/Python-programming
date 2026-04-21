import numpy as np

# 1D Array
arr_1d = np.array([1, 2, 3, 4])
print("1D Array:\n", arr_1d)            # Output: [1 2 3 4]
print("Sum (Axis 0):", np.sum(arr_1d, axis=0))  # Output: 10 (Sum of all elements)


# 2D Array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("\n2D Array:\n", arr_2d)             # Output: [[1 2 3]
                                          #          [4 5 6]]

print("Sum along rows (Axis 0):", np.sum(arr_2d, axis=0))  # Output: [5 7 9]
print("Sum along columns (Axis 1):", np.sum(arr_2d, axis=1))  # Output: [6 15]
print("Overall Sum:", np.sum(arr_2d))     # Output: 21 (Sum of all elements)


# 3D Array
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])

print("\n3D Array:\n", arr_3d)            # Output: [[[1 2]
                                          #          [3 4]]
                                          #         [[5 6]
                                          #          [7 8]]]
print("Sum along depth (Axis 0):\n", np.sum(arr_3d, axis=0))  
# Output: [[ 6  8]
#          [10 12]]
print("Sum along rows (Axis 1):\n", np.sum(arr_3d, axis=1))  
# Output: [[ 4  6]
#          [12 14]]
print("Sum along columns (Axis 2):\n", np.sum(arr_3d, axis=2))  
# Output: [[ 3  7]
#          [11 15]]
'''Visualizing Axes

In arr_1d, axis 0 is the entire array itself (there's only one direction).
In arr_2d, axis 0 represents rows (moving down), and axis 1 represents columns (moving across).
In arr_3d, axis 0 is the depth (the outer array), axis 1 is rows, and axis 2 is columns.
Key Takeaways
Axes are directions: They define how you move through your array’s dimensions.
Functions use axes: Many NumPy operations (like sum, mean, max) take an axis argument to
determine the direction of the calculus'''
