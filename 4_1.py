def binary_search(key, local_array):
    if len(local_array) == 1:
        if key == local_array[0]:
            return local_array[0]
        return 'Элемент не найден'
    else:
        i = len(local_array) // 2
        if local_array[:i][-1] < key:
            local_array = local_array[i:]
        else:
            local_array = local_array[:i]
        return binary_search(key, local_array)


print(binary_search(31, [1, 3, 4, 6, 7, 9, 12, 14, 30]))
