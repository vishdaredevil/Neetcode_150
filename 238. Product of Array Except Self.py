# LeetCode - Product of Array Except Self
# NeetCode 150 - Arrays & Hashing

# Problem Statement:
# We have to return an array where:
# answer[i] = product of all elements except nums[i]

# ---------------- APPROACH ----------------
# We use Prefix Product and Suffix Product.
# Prefix Product:
# Product of all elements before current index.

# Suffix Product:
# Product of all elements after current index.

# Final Answer:
# answer[i] = prefix * suffix
# ---------------- TIME COMPLEXITY ----------------

# Two traversals only.
# TC = O(n)

# ---------------- SPACE COMPLEXITY ----------------

# Output array excluded from extra space.
# Extra variables used:
# p and s
# SC = O(1)

from typing import List
def productExceptSelf(self, nums: List[int]) -> List[int]:
    a = [1] * len(nums)
    p = 1
    for i in range(len(nums)):
        a[i] = p
        p = p * nums[i]
    s = 1
    for i in range(len(nums) - 1, -1, -1):
        a[i] = a[i] * s
        s = s * nums[i]
    return a