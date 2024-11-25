def bubble_sort(array):
    n = len(array)
    swap_count = 0  
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:  
                array[j], array[j + 1] = array[j + 1], array[j]
                swap_count += 1  
    return array, swap_count
#testing

test_list = [5, 66,6 ,12,1]
sorted_list, total_swaps = bubble_sort(test_list)
print("Sorted List:", sorted_list)
print("Total Swaps:", total_swaps)
