# 2.1-1
# Illustration of insertion sort on [31, 41, 59, 26, 41, 58]
# [31, <41>, | 59, 26, 41, 58] # 41 already on the correct place
# [31, 41, [59], | 26, 41, 58] # 59 already on the correct place
# [<26>, 31, 41, 59, | 41, 58] # 26 inserted to the correct place
# [26, 31, 41, <41>, 59, | 58]
# [26, 31, 41, 41, <58>, 59]


# 2.1-2
def insertion_sort_nondecreasing(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


# 2.1-3
def linear_search(a, v):
    for i in range(0, len(a)):
        if a[i] == v:
            return i
    return None


# 2.1-3 loop invariant

# 2.1-4
def add_binary(a, b):

    def digit_from_end(binary, index_from_end):
        real_index = len(binary) - 1 - index_from_end
        if real_index < 0:
            return 0
        else:
            return binary[real_index]

    len_a = len(a)
    len_b = len(b)
    len_max = max(len_a, len_b)
    len_c = len_max + 1
    c = [0] * len_c
    carry = 0
    for i in range(0, len_c):
        digit_a = digit_from_end(a, i)
        digit_b = digit_from_end(b, i)
        digit_sum = digit_a + digit_b + carry
        new_digit = digit_sum % 2
        carry = digit_sum // 2
        c[-1 - i] = new_digit
    return c


# 2.2-1
# ç(n^3)

# 2.2-2
# selection sort
# loop invariant:
# the subarray a[0 ... i-1] contains the smallest i elements from a and is sorted
# at beginning, i = 0
#   subarray is [], so the loop invariant holds
# the loop finds the smallest element in a[i ... n -1] and inserts it to a[i]
# so after the loop, the invariant still holds
# after the loop ends, i is n - 1, so the subarray a[0 ... n-2] contains the
# smallest n-1 elements from a and is sorted, which means a itself is sorted
def selection_sort(a):
    for i in range(0, len(a) - 1):
        i_min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[i_min]:
                i_min = j
        a[i], a[i_min] = a[i_min], a[i]

# 2.2-3
# average
#   The algorithm has the same chance of checking for each 1, 2, 3, ... n times before finding
#   the answer. Therefore on average it will require 1/n * (1 + 2 + 3 ... + n)
#   = 1/n * n (n + 1) / 2 = (n + 1) / 2 times before finding an answer.
# worst
#   must check for n times
# both are Θ(n)

# 2.2-4
# check whether the input matches a certain value, and then just return the precalculated answer
# example
def factorial(n):
    if n == 4:
        return 24  # when input is 4, it is best case
    else:
        return None  # for other values, calculate it properly (not implemented)


# insert the i-th item on the correct position
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


# find the (next) smallest item, sink it like a rock
def rock_sort_teleport(a):
    for i in range(0, len(a) - 1):
        min = a[i]
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < min:
                min = a[j]
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]


# the (next) smallest item will sink like a rock
def rock_sort(a):
    for i in range(0, len(a) - 1):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]


# find the (next) largest item, float it like a bubble
def bubble_sort_teleport(a):
    for i in range(0, len(a) - 1):
        max = a[0]
        max_idx = 0
        for j in range(1, len(a) - i):
            if a[j] > max:
                max = a[j]
                max_idx = j
        top_idx = len(a) - 1 - i
        a[top_idx], a[max_idx] = a[max_idx], a[top_idx]


# the (next) largest item will float like a bubble
def bubble_sort(a):
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def print_tab(depth):
    for i in range(0, depth):
        print('  ', end='')


def merge_sort(a):
    merge_sort_real(a, 0, len(a) - 1)


def merge_sort_real(a, i_min, i_max):  #, indent=0):
    #print_tab(indent)
    #print(i_min, i_max)
    count = i_max - i_min + 1
    if count <= 1:
        return
    mid = (i_min + i_max) // 2
    if i_min != mid:
        merge_sort_real(a, i_min, mid)  #, indent + 1)
    if mid + 1 != i_max:
        merge_sort_real(a, mid + 1, i_max)  #, indent + 1)

    # combine
    result = []
    pointer_l = i_min
    pointer_r = mid + 1
    while pointer_l <= mid or pointer_r <= i_max:
        if pointer_l > mid:
            result.append(a[pointer_r])
            pointer_r += 1
        elif pointer_r > i_max:
            result.append(a[pointer_l])
            pointer_l += 1
        elif a[pointer_l] < a[pointer_r]:
            result.append(a[pointer_l])
            pointer_l += 1
        else:
            result.append(a[pointer_r])
            pointer_r += 1
    # write the result back
    pointer_l = i_min
    #print_tab(indent + 1)
    #print(result)
    for n in result:
        a[pointer_l] = n
        pointer_l += 1


array1 = [5, 4, 3, 2, 0, 1, 6, 3]
array2 = [31, 41, 59, 26, 41, 58]
a = array2


#selection_sort(a)
#insertion_sort_nondecreasing(a)
#rock_sort(array)
#bubble_sort(a)
merge_sort(a)

print(a)

#i = linear_search(array1, "adfasdf")
#print(i)

#m = [1, 1]
#n = [1, 1]
#the_sum = add_binary(m, n)
#print(the_sum)
