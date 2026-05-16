# This is the 4th question from the NeetCode 150 sheet.

# https://leetcode.com/problems/group-anagrams/description/

# Today’s learning and understanding:

# In this problem, we have to group all strings that are anagrams of each other.

# Anagrams are words that contain the same characters with the same frequency,

# only the arrangement of characters is different.

# Example:

# eat, tea, ate → all are anagrams

# There can be multiple approaches for solving this problem:

# 1️ Brute Force Approach

# Compare every string with every other string and check whether they are anagrams or not.

# But this approach is slow because it uses nested loops.

# 2️ Sorting Approach

# Sort every string and use the sorted string as a key.

# Since all sorted strings become same,

# we can store them in the same group.

# Time Complexity: O(n * k log k)

# 3️ Optimal Approach — HashMap / Dictionary

# Use a dictionary where:

# key   → sorted string

# value → list of anagrams

# If multiple words have the same sorted form,

# they belong to the same group.

# The main concepts revised today:

# • Hashmaps / Dictionaries

# • String sorting

# • List handling

# • Traversing arrays

# • Grouping logic

# One thing I’m understanding during this journey is that

# solving the problem and explaining the logic clearly are both important skills.

# While solving this problem,

# I understood the idea quickly,

# but while implementing it,

# I had to carefully think about dictionary creation,

# key handling, and storing values correctly.

class Solution:
    def groupAnagrams(self, s):
        d = {}

        for i in s:
            k = "".join(sorted(i))

            if k not in d:
                d[k] = []

            d[k].append(i)

        return list(d.values())
