# LeetCode 1 - Two Sum
# https://leetcode.com/problems/two-sum/
# NeetCode 150 - Arrays & Hashing

# Problem Statement:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# Each input has exactly one solution and we cannot use the same element twice.

# Approach Used: HashMap / Dictionary

# Logic:
# We traverse the array once.
# For every element, we calculate the remaining value needed:
# remaining = target - current_element
#
# If remaining already exists in hashmap,
# then we found the pair and return their indices.
#
# Otherwise store current element and its index in hashmap.

# Why HashMap?
# HashMap gives O(1) lookup time,
# making the overall solution optimal.

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums, target):
        
        hp= {}

        for i in range(len(nums)):

            remaining = target - nums[i]

            if remaining in hp:
                return [hp[remaining], i]

            hp[nums[i]] = i