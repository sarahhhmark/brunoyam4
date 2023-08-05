def insert_sort(test_array):
    for i in range(1, len(test_array)):
        for j in range(i, 0, -1):
            if test_array[j - 1] > test_array[j]:
                test_array[j - 1], test_array[j] = test_array[j], test_array[j - 1]
            else:
                break
    return test_array


print(insert_sort([10, 5, -1, 9, 8, 20, 7]))
