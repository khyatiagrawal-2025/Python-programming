'''
Scenario: Rotate a list by k elements
A conveyor belt system moves items in a circular fashion. To align items for a specific process, you need to rotate the list of item positions to the right by k steps. Your task is to determine the new order of items after the rotation.
Sample Input and Output with Explanation:
1. Input: list = [1, 2, 3, 4, 5], k = 2 Output: [4, 5, 1, 2, 3] Explanation: Rotating the list [1, 2, 3, 4, 5] to the right by 2 positions gives [4, 5, 1, 2, 3].
2. Input: list = [10, 20, 30, 40, 50], k = 3 Output: [30, 40, 50, 10, 20] Explanation: Rotating [10, 20, 30, 40, 50] by 3 positions gives [30, 40, 50, 10, 20].
3. Input: list = [7, 8, 9], k = 1 Output: [9, 7, 8] Explanation: Rotating [7, 8, 9] by 1 position gives [9, 7, 8].
Test Cases:
1. Input: list = [0, 1, 2, 3], k = 6 Output: [2, 3, 0, 1]
2. Input: list = [1, 2, 3, 4, 5], k = 1 Output: [5, 1, 2, 3, 4]
3. Input: list = [1, 2, 3, 4, 5], k = 5 Output: [1, 2, 3, 4, 5]
4. Input: list = [1, 2, 3, 4, 5], k = 0 Output: [1, 2, 3, 4, 5]
5. Input: list = [10, 20, 30], k = 2 Output: [20, 30, 10]
'''

arr = eval(input())
k = int(input())

k = k % len(arr)   # important for large k

result = arr[-k:] + arr[:-k]

print(result)