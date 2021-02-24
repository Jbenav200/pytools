# Content originally learned at GeeksForGeeks
# A python method for an optimized Bubble Sort Algorithm

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from - to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped by inner loop, then break
        if swapped == False:
            break
    return arr


# Testing the sort
""" arr = [62, 22, 25, 11, 21, 11, 85]

bubble_sort(arr)

print("Sorted array:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
 """
