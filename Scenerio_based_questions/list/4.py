'''
Given an list of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Constraints:
 2 <= nums.length <= 104
 -109 <= nums[i] <= 109
 -109 <= target <= 109
Sample Input and Output with Explanation:
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Explanation: Because 1 and 2 are 2 and 4, which add up to the target 6.
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Explanation: Because 0 and 1 are 3 and 3, which add up to the target 6.
Test Cases:
1. Input: nums = [1, 2, 3, 4], target = 5 Output: [0, 3]
2. Input: nums = [2, 5, 5, 11], target = 10 Output: [1, 2]
3. Input: nums = [1, 7, 11, 15], target = 8 Output: [0, 1]
4. Input: nums = [6, 3, 4, 8], target = 10 Output: [1, 2]
5. Input: nums = [3, 5, 9, 2], target = 8 Output: [0, 3]
'''

nums = eval(input())
target = int(input())

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print([i,j])
            break