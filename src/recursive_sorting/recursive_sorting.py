# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    a, b, c = 0, 0, 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
            c += 1
        else:
            merged_arr[c] = arrB[b]
            b += 1
            c += 1
    while a < len(arrA):
        merged_arr[c] = arrA[a]
        a += 1
        c += 1
    while b < len(arrB):
        merged_arr[c] = arrB[b]
        b += 1
        c += 1
    return merged_arr

# Checking Merge in console
l1 = [2, 4, 6, 8, 10]
l2 = [1, 5, 9]
print(f"merged list: {merge(l1, l2)}")


#                [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

#                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#                  Split into smaller lists
#                [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

#                [1, 5, 8, 4, 2] [9, 6, 0, 3, 7]

#                [1, 5, 8,] [4, 2] [9, 6, 0] [3, 7]

#                [1] [5] [8] [4] [2] [9] [6] [0] [3] [7]
#
#


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr


    left = merge_sort(arr[0: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])
    arr = merge(left,right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
