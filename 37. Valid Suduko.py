# LeetCode - Valid Sudoku
# NeetCode 150 - Arrays & Hashing

# Problem Statement:
# We have to check whether a Sudoku board is valid or not.

# Conditions:
# 1. Every row should contain numbers 1-9 without repetition
# 2. Every column should contain numbers 1-9 without repetition
# 3. Every 3x3 box should contain numbers 1-9 without repetition

# Important:
# We only check filled cells.
# Empty cells are represented by '.'

# ---------------- APPROACH ----------------

# We use sets because:
# Sets automatically store unique values.
# If a value already exists, then Sudoku becomes invalid.

# We maintain:
# r -> stores numbers present in each row
# c -> stores numbers present in each column
# b -> stores numbers present in each 3x3 box

# ---------------- MAIN LOGIC ----------------

# Traverse the complete board using nested loops.

# For every cell:
# 1. Skip if cell contains '.'
# 2. Check whether number already exists in:
#       - current row
#       - current column
#       - current 3x3 box
#
# If yes:
# return False

# Otherwise:
# add number into row, column and box sets.

# ---------------- TIME COMPLEXITY ----------------
# We traverse 9x9 board once.
# TC = O(81) -> O(1)

# ---------------- SPACE COMPLEXITY ----------------
# Extra sets used
# SC = O(1)

class Solution:
    def isValidSudoku(self, board):

        r = {}
        c = {}
        b = {}

        for i in range(9):

            for j in range(9):

                n = board[i][j]

                if n == ".":
                    continue

                if i not in r:
                    r[i] = set()

                if j not in c:
                    c[j] = set()

                k = (i // 3, j // 3)

                if k not in b:
                    b[k] = set()

                if n in r[i] or n in c[j] or n in b[k]:
                    return False

                r[i].add(n)
                c[j].add(n)
                b[k].add(n)

        return True