# 1.1-1
# Real world example of sorting:
# Having students line up from the shortest to tallest.
# Real world example of convex hull:
# 1. To test collision of a complex polygon, we can first use its simpler convex hull.
# 2. To find the shortest path between point A and B when there is a polygon obstacle between it,
#    we can first find the convex hull of A, B, and all points of the polygon.
#    The path will traverse the convex hull's sides from A to B.

# 1.1-2
# Space is another measure of efficiency. An algorithm might be fast but requires a lot of space,
# for example if you make a lookup table for a trigonometric function.
# For 32-bit floats you have 2^32 (~ 4 billion) possible input, while each output requires 32-bit or 4 bytes
# of space. In total you will need 16 GB of space. (of course we can optimize it by using trigonometric identities
# and first normalizing the input)

# 1.1-3
# Linked list is a pretty common data structure. One advantage compared to an array is that you can easily
# remove elements in the middle of the list. The disadvantage is that getting a specific element requires traversing
# the list from the beginning (complexity O(n)).

# 1.1-4
# Shortest path problem and TSP is similar in that they both seek to find the shortest path.
# However, in TSP the order of the destinations isn't definite (e.g., you can choose A-B-C-D-A or A-D-B-C-A).

# 1.1-5
# Real world problem where only the best solution will do: Integer addition.
# Approximate solution is OK: Finding a path from A to B. (as long as you arrive without massive detour it is OK)

# ---------------

# 1.2-1
# Algorithmic content required at application level: Find and replace in text editor.
# Algorithm involved: string matching

# 1.2-2
# Insertion sort: 8n^2
# Merge sort: 64n lg n
# at n = 44, insertion sort requires 15,488 steps, while merge sort requires 15,374 steps
# insertion sort wins on n < 44

# 1.2-3
# With n = 15, 100n^2 = 22,500 < 2^n = 32,768. So from n = 15 the algorithm with quadratic complexity runs faster.

# 1.1
# see 1.1.png

from math import log2
from math import sqrt

second = 1000000  # in microseconds
minute = second * 60
hour = minute * 60
day = hour * 24
month = day * 30
year = month * 12
century = year * 100
a = [second, minute, hour, day, month, year, century]


# change f(n) as needed
def f(n):
    if n <= 0:
        return 1
    else:
        return 2 * f(n - 1)


def max_n_find(lower_n, upper_n, t):
    if upper_n == lower_n + 1:
        return lower_n
    mid = (lower_n + upper_n) // 2
    real_t = f(mid)
    if real_t == t:
        return mid
    elif real_t < t:
        return max_n_find(mid, upper_n, t)
    else:
        return max_n_find(lower_n, mid, t)


i = 0
prev_n = 0
n = 1
while i < len(a):
    t = a[i]
    max_n = -1
    while max_n == -1:
        real_t = f(n)
        if real_t == t:
            max_n = n
        elif real_t > t:
            max_n = max_n_find(prev_n, n, t)
        else:
            prev_n = n
            n *= 2
    print(max_n, t)
    i += 1
    n = max_n

