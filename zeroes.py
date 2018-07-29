def move_zeroes(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    return arr[:j]

print move_zeroes([0,1,0,0,0,0,0,3,2,6,7,1,0,10,0])

