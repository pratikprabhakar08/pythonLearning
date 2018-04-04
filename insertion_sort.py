#
# Implementation of Insertion-Sort
#

def insertion_sort(lst):
    """ Re-arrange the list 'lst' of comparable elements
        into non-decreasing order.
    """
    for i in range(1, len(lst)):
        cur = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > cur:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = cur
