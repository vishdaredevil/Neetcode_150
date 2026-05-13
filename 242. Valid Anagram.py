# This is the 2nd question from the NeetCode 150 sheet.

# [https://leetcode.com/problems/valid-anagram/description/](https://leetcode.com/problems/valid-anagram/description/)
# Today’s learning and understanding:

# In this problem, we have to check whether two strings are anagrams or not.
# That means both strings should contain the same characters with the same frequency.

# There can be multiple approaches for solving this problem:
# 1️⃣ Brute Force Approach
# We can compare characters manually using nested loops and check frequencies one by one,
#  but this approach is not optimal because the time complexity becomes high.

# 2️⃣ Sorting Approach
# We can sort both strings and compare them.
# If both sorted strings are equal, then they are anagrams.
# Time Complexity: O(n log n)

# 3️⃣ Optimal Approach — HashMap / Dictionary
# In this approach, we store the frequency of characters for both strings using dictionaries.

# If both dictionaries become equal, then both strings are anagrams.

# The main concept revised today:
# • Hashmaps / Dictionaries
# • Frequency counting
# • String traversal
# • Edge case handling using length comparison

# One thing I’m realizing during this journey is that understanding logic and
#  implementing it smoothly are two different skills.

# While solving this problem, I understood the approach quickly,
#  but because of inconsistency in practice over the past few months, 
# I got slightly confused with dictionary handling and syntax during implementation.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):
            return False
        cS = {}
        cT = {}
        for i in range(len(s)):
            cS[s[i]] = 1 + cS.get(s[i], 0)
            cT[t[i]] = 1 + cT.get(t[i], 0)
        return cS == cT
