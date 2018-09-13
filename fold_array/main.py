import math
def fold_array(array, runs):
    end = array[math.ceil(len(array)/2):]
    array = array[:math.ceil(len(array)/2)]
    end = end[::-1]
    for i in range(0,len(end)):
        array[i] += end[i]
    runs -= 1
    if runs:
        return fold_array(array, runs)
    return array
    