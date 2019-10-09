# Introsort
#
# directement adapté de l'implémentation en C++ de la STL

# Définitions utilitaires

# Seuil de passage au tri par insertion
threshold = 16


# Logarithme entier en base 2
def int_log2(n):
    k = 0
    while n:
        n >>= 1
        k += 1
    return k - 1


# Tri par tas


def siftDown(l, start, first, end):
    curr = first
    child = 2 * curr + 1
    while child < end:
        next = curr
        if l[start + child] > l[start + next]:
            next = child
        child += 1
        if child < end and l[start + child] > l[start + next]:
            next = child
        if next == curr:
            break
        l[start + curr], l[start + next] = l[start + next], l[start + curr]
        curr = next
        child = 2 * curr + 1


def heapsort(l, first, last):
    size = last - first
    for i in range((size - 1) // 2, -1, -1):
        siftDown(l, first, i, size)
    for i in range(size - 1, 0, -1):
        l[first + 0], l[first + i] = l[first + i], l[first + 0]
        siftDown(l, first, 0, i)


# Tri par insertion


def unguarded_linear_insert(l, last):
    val = l[last]
    prev = last - 1
    while val < l[prev]:
        l[last] = l[prev]
        last = prev
        prev -= 1
    l[last] = val


def insertion_sort(l, first, last):
    if first == last:
        return
    for i in range(first + 1, last):
        if l[i] < l[first]:
            val = l[i]
            for j in range(i, 0, -1):
                l[j] = l[j - 1]
            l[0] = val
        else:
            unguarded_linear_insert(l, i)


def unguarded_insertion_sort(l, first, last):
    for i in range(first + 1, last):
        unguarded_linear_insert(l, i)


def final_insertion_sort(l, first, last):
    if last - first > threshold:
        insertion_sort(l, first, first + threshold)
        unguarded_insertion_sort(l, first + threshold, last)
    else:
        insertion_sort(l, first, last)


# Tri rapide


def move_median_to_first(l, result, a, b, c):
    if l[a] < l[b]:
        if l[b] < l[c]:
            l[result], l[b] = l[b], l[result]
        elif l[a] < l[c]:
            l[result], l[c] = l[c], l[result]
        else:
            l[result], l[a] = l[a], l[result]
    else:  # l[b] <= l[a]
        if l[a] < l[c]:
            l[result], l[a] = l[a], l[result]
        elif l[b] < l[c]:
            l[result], l[c] = l[c], l[result]
        else:
            l[result], l[b] = l[b], l[result]


def unguarded_partition(l, first, last, pivot):
    while True:
        while l[first] < pivot:
            first += 1
        last -= 1
        while pivot < l[last]:
            last -= 1
        if first >= last:
            return first
        l[first], l[last] = l[last], l[first]
        first += 1


def unguarded_partition_pivot(l, first, last):
    mid = first + (last - first) // 2
    move_median_to_first(l, first, first + 1, mid, last - 1)
    return unguarded_partition(l, first + 1, last, l[first])


# Boucle principale d'introsort


def introsort_loop(l, first, last, depth):
    while (last - first > threshold):
        if depth == 0:
            partial_sort(l, first, last, last)
            return
        depth -= 1
        cut = unguarded_partition_pivot(l, first, last)
        introsort_loop(l, cut, last, depth)
        last = cut


# Fonction principale


def sort(l):
    if len(l) <= 1:
        return
    s = len(l)
    introsort_loop(l, 0, s, 2 * int_log2(s))
    final_insertion_sort(l, 0, s)
