#A tuple is an ordered and immutable collection of elements.

'''
Scenario: You are a software developer at a gaming company. Your manager has given you a task related to a leaderboard system. Players earn points after completing various levels, and the scores are stored in a list. Your task is to identify the second-highest score from the list to award the second-place player. The list of scores may contain duplicates, but only unique scores should be considered for determining the second-highest score.
Sample Input and Output with Explanation:
Input : scores = (85, 90, 78, 92, 88, 76, 95)
Output: Average Score: 86.57
Explanation:
In this case, the scores tuple contains the following values: 85, 90, 78, 92, 88, 76, 95. To calculate the average:
 Add all the scores: 85 + 90 + 78 + 92 + 88 + 76 + 95 = 604
 Divide the total by the number of students: 604 / 7 = 86.57 .
Input : scores = (65, 70, 75, 80, 85)
Output : Average Score: 75.0
Explanation:
For this example, the scores are: 65, 70, 75, 80, 85.
 Add all the scores: 65 + 70 + 75 + 80 + 85 = 375
 Divide by the number of students: 375 / 5 = 75.0
Test Cases:
1. Input: (45, 50, 55, 60, 65) Output: Average Score: 55.0
2. Input: (100, 95, 90, 85, 80, 75, 70, 65) Output: Average Score: 82.5
3. Input: (50, 60, 70) Output: Average Score: 60.0
4. Input: (30, 40, 50, 60, 70, 80, 90) Output: Average Score: 60.0
5. Input: (10, 20, 30, 40) Output: Average Score: 25.0
'''

scores = eval(input())

avg = sum(scores) / len(scores)

print("Average Score:", avg)