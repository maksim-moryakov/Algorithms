# Алгоритм бинарного поиска (нахождения среднего числа)

def binary_search(list, item):
    low = 0
    high = list[-1]
    print(f'Последний элемент списка {high}')

    while low <= high:
        mid = (low + high) / 2
        print(f'Среднее значение {mid}')
        guess = list[mid]  # Надо переделать это в python 3
        print(f'Выводим список {guess}')
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
