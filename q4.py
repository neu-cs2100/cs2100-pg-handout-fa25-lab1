from typing import Optional

"""
Please implement the pattern() function below. 
There are comments to describe what it should do, but you will need to write
the documentation for the function.
"""

# The pattern() function will return one of these pattern types:

# Right Triangle Numbers (1):
#"1
# 1 2
# 1 2 3
# 1 2 3 4"

# Pyramid Numbers (2):
#"   1
#   1 2
#  1 2 3
# 1 2 3 4"

# Multiplication Table (3):
#"1  2  3  4
# 2  4  6  8
# 3  6  9 12
# 4  8 12 16"

# Fibonacci Sequence (4):
#"Row 1: 1
# Row 2: 1
# Row 3: 2
# Row 4: 3
# Row 5: 5"

def pattern(pattern_type: int, num_rows: int) -> str:
    """
    1. Given the pattern type (1-4) and the number of rows,
    2. Return a string containing the chosen pattern.
    3. If the pattern type or number of rows is invalid, raise a ValueError.
    """
    pass

if __name__ == '__main__':
    print(pattern())
