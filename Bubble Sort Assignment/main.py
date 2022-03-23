# Bubble Sort Assignment by Omar Elshimi

nums = [6, 9, 2, 3, 5]

def bubbleSort(array):
    for numCompare in range(len(array) - 1, 0, -1):
        for i in range(numCompare):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                
print(bubbleSort(nums))

