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


array1 = [5, 4, 3, 2, 0, 1, 6, 3]
array2 = [31, 41, 59, 26, 41, 58]
a = array1


insertion_sort(a)
#rock_sort(array)
#bubble_sort(a)

print(a)
