from random import sample


def binary_search(target, sorted_list):
    left = 0
    right = len(sorted_list) - 1
    iteration_count = 0

    while left <= right:
        middle = (left + right) // 2  # Находим середину списка
        print(f'left = {left}, right = {right}')

        if target == sorted_list[middle]:  # Если число найдено, завершаем поиск
            print(f"Number {target} found at index {middle}")
            break
        else:
            if target > sorted_list[middle]:  # Если искомое число больше, смещаем левую границу
                left = middle + 1
            else:  # Иначе смещаем правую границу
                right = middle - 1
        iteration_count += 1

    print(f"Number of iterations: {iteration_count}")


def bubble_sort(unsorted_list):
    n = len(unsorted_list)

    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list


# Генерируем список уникальных случайных чисел
numbers_list = sample(range(1, 80), 50)

numbers_list = bubble_sort(numbers_list)

print(numbers_list)

target_number = int(input('Input number: '))

binary_search(target_number, numbers_list)
