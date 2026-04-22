'''
Scenario: You are working on a sports tournament management system where players from two different teams have been registered. These players' IDs are stored in two separate tuples. The tournament committee wants to identify which players are part of both teams, as these players might have transferred between teams. Your task is to find and return the common player IDs (i.e., the players who exist in both tuples).
Example Input 1:
team_a = (101, 102, 103, 104)
team_b = (103, 105, 106)
Expected Output 1:
(103)
Explanation:
In this case, the player IDs from both teams are: team_a = (101, 102, 103, 104) team_b = (103, 105, 106).
 The player ID "103" is present in both teams, so it is the common element between the two tuples.
Example Input 2:
team_a = (201, 202, 203)
team_b = (203, 204, 205)
Expected Output 2:
(203)
Explanation:
In this case, the player IDs from both teams are: team_a = (201, 202, 203) team_b = (203, 204, 205).
 The player ID "203" is present in both teams, so it is the common element between the two tuples.
Test Cases:
1. Input: (111, 112, 113, 114), (113, 115, 116) Output: (113)
2. Input: (301, 302, 303, 304), (305, 302, 306) Output: (302)
3. Input: (501, 502, 503), (503, 504, 505) Output: (503)
4. Input: (1001, 1002), (1003, 1004, 1001) Output: (1001)
5. Input: (121, 122, 123), (123, 124, 125) Output: (123)
'''

team_a = eval(input())
team_b = eval(input())

common = []

for item in team_a:
    if item in team_b:
        common.append(item)

result = tuple(common)

print(result)