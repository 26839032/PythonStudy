def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1,24,54,63,23,55,3]))

#快速排序算法，通过递归，将问题不断缩小，堆栈要好好的理解一下，还有欧几里得算法
