"""
List Comprehensions
"""

odds = [1, 3, 5, 7, 9]

# like map
print([x+1 for x in odds])

# like filter
print([x for x in odds if 25 % x == 0])

# general form
# [<map expression> for <name> in <sequence expression if <filter expression>]

"""
Dictionary Comprehensions
"""
# Re-watch video for these few lines.