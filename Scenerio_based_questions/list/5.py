'''
Counting Words With a Given Prefix
You are given an list of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.
Example 1:
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
Test Cases
1. Input: words = ["cat", "car", "carbon", "dog"], pref = "ca" Output: 3
2. Input: words = ["hero", "hermit", "heritage", "hello"], pref = "her" Output: 3
3. Input: words = ["light", "like", "life", "line"], pref = "li" Output: 4
4. Input: words = ["zoom", "zebra", "zone"], pref = "zo" Output: 2
5. Input: words = ["book", "bookmark", "board"], pref = "boo" Output: 2
'''
words = eval(input())
pref = input()

count = 0

for word in words:
    if word.startswith(pref):
        count += 1

print(count)