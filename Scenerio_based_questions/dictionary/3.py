'''
Scenario 3:
Calculate Average Marks You are required to calculate the average marks for a student based on their scores in three subjects: Math, Science, and English. Additionally, you will add a History subject with predefined marks to the student's record. This problem helps you learn how to update a dictionary and perform basic arithmetic operations.
Input Format:
 Three space-separated integers representing marks for Math, Science, and English.
Constraints:
 0 ≤ Marks ≤ 100.
Output Format:
 Two lines:
1. The updated dictionary (with History marks).
2. The average marks rounded to 2 decimal places.
Sample Inputs and Outputs:
Sample Input
Sample Output
80 90 85
Updated Marks: {'Math': 80, 'Science': 90, 'English': 85, 'History': 88} Average Marks: 85.75
70 85 80
Updated Marks: {'Math': 70, 'Science': 85, 'English': 80, 'History': 88} Average Marks: 80.75
95 88 92
Updated Marks: {'Math': 95, 'Science': 88, 'English': 92, 'History': 88} Average Marks: 90.75
60 75 65
Updated Marks: {'Math': 60, 'Science': 75, 'English': 65, 'History': 88} Average Marks: 72.00
50 50 50
Updated Marks: {'Math': 50, 'Science': 50, 'English': 50, 'History': 88} Average Marks: 59.50
'''

maths, science, english = map(int, input().split())

marks = {
    "Math": maths,
    "Science": science,
    "English": english
}

# add History
marks["History"] = 88

# calculate average
avg = sum(marks.values()) / len(marks)

print("Updated Marks:", marks)
print("Average Marks:", format(avg, ".2f"))