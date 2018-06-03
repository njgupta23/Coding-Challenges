# K-Messed Array Sort

# Given an array of integers arr where each element is at most k places away 
# from its sorted position, code an efficient function sortKMessedArray 
# that sorts arr. 

# For instance, for an input array of size 10 and k = 2, 
# an element belonging to index 6 in the sorted array 
# will be located at either index 4, 5, 6, 7 or 8 in the input array.

# example:

# input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

# output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sort_k_messed_array(arr, k):

    sub_arr = []
    output = []

    for i in range(k+1):
        sub_arr.append(arr[i])

    sub_arr.sort()

    for i in range(len(arr) - k - 1):
        output.append(sub_arr.pop(0))
        sub_arr.append(arr[k+1+i])
        sub_arr.sort()

    return output + sub_arr
