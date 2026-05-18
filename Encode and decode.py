# LeetCode - Encode and Decode Strings
# NeetCode 150 - Arrays & Hashing

# Problem Statement:
# We have to convert a list of strings into a single string (encode)
# and then convert it back into the original list (decode).
# Main Idea:
# We store:
# length_of_word + "#" + actual_word

# Example:
# "Hello" -> "5#Hello"
# "World" -> "5#World"

# Final encoded string:
# "5#Hello5#World"

# Why are we adding length?
# Because strings can contain any character,
# so length helps us know exactly where each word ends.
# ---------------- ENCODE ----------------
# In encode():
# We traverse each word in the list.
# For every word:
# add its length
# then add '#'
# then add the actual word.

# ---------------- DECODE ----------------
# In decode():
# We traverse the encoded string.

# First find '#'
# Characters before '#' represent length.

# Then move pointer forward and repeat.

# Time Complexity:
# Encode -> O(n)
# Decode -> O(n)

# Space Complexity:
# O(n)

def encode(self, strs):
    s = ""
    for w in strs:
        s += str(len(w)) + "#" + w
    return s
def decode(self, s):
    a = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        l = int(s[i:j])
        w = s[j + 1 : j + 1 + l]
        a.append(w)
        i = j + 1 + l
    return a                                            