# This is the 5th question from the NeetCode 150 sheet.
# https://leetcode.com/problems/top-k-frequent-elements/description/
# Today’s learning and understanding:
# In this problem, we have to return the k most frequent elements from the array.
# That means we need to count how many times each number appears
# and return the elements with highest frequency.
# Example:
# nums = [1,1,1,2,2,3]
# k = 2
# Output:
# [1,2]
# Because:
# 1 appears 3 times
# 2 appears 2 times
# 3 appears 1 time
# There can be multiple approaches for solving this problem:
# 1️ Brute Force Approach
# Count frequency for every element manually using nested loops.
# Then compare frequencies and find top k elements.
# But this approach becomes slow for large inputs.
# 2️ Sorting Approach
# First store frequency of every number in a dictionary.
# Then sort the dictionary based on frequency in descending order.
# Finally return first k elements.
# Time Complexity: O(n log n)
# 3️ Optimal Approach — Bucket Sort / Heap
# We can use Bucket Sort or Heap to reduce time complexity.
# These approaches are more optimized for large datasets.
# The main concepts revised today:
# • Hashmaps / Dictionaries
# • Frequency counting
# • Sorting using keys
# • Array traversal
# • Returning top k elements
# One thing I’m realizing during this journey is that
# understanding the logic is different from implementing it smoothly.
# While solving this question,
# I understood the frequency counting part quickly,
# but while implementing,
# I had to think carefully about sorting dictionaries
# and using keys correctly.
class Solution:
    def topKFrequent(self, n, k):

        d = {}


        for i in n:
            d[i] = 1 + d.get(i, 0)
        s = sorted(d, key=d.get, reverse=True)
        return s[:k]