#A list is an ordered and mutable collection of elements in Python.

'''
Scenario: You are a software developer at a gaming company. Your manager has given you a task related to a leaderboard system. Players earn points after completing various levels, and the scores are stored in a list. Your task is to identify the second-highest score from the list to award the second-place player. The list of scores may contain duplicates, but only unique scores should be considered for determining the second-highest score.

Constraints:

1. If the list has less than two unique scores, there should be no second-highest score, and the result should be "No second-highest score."
2. The input list will always contain integers.

Sample Input and Output with Explanation:

1. Input: [2, 3, 1, 4, 5] Output: 4
Explanation: The unique scores are [1, 2, 3, 4, 5]. The highest score is 5, and the second-highest score is 4.

2. Input: [5, 5, 5, 5] Output: No second-highest score
Explanation: The list has only one unique score [5]. Since there is no second-highest score, the output is "No second-highest score".

3. Input: [10, 40, 20, 20, 30, 30,40] Output: 30
Explanation: The unique scores are [10, 20, 30, 40]. The highest score is 40, and the second-highest score is 30.

Test Cases:
1. Input: [7, 10, 5, 8, 9] Output: 9
2. Input: [100, 200, 100, 50, 200] Output: 100
3. Input: [1] Output: No second-highest score
4. Input: [4, 1, 2, 4, 3] Output: 3
5. Input: [0, -1, -2, -1, 0] Output: -1
'''
scores = eval(input())

unique_scores = list(set(scores))

if len(unique_scores) < 2:
    print("No second-highest score")
else:
    unique_scores.sort()
    print(unique_scores[-2])