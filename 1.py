import random
import time

def bubble_sort(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
    return list

def test_bubble(arr):
    start_time = time.time()
    for i in range(200):
        bubble_sort(arr)
    end_time = time.time()
    return (end_time - start_time) / 200

def test_sorted(arr):
    start_time = time.time()
    for i in range(200):
        sorted(arr)
    end_time = time.time()
    return (end_time - start_time) / 200


random_list = [random.randint(-1000, 1000) for i in range(1000)]
bubble_sort_time = test_bubble(random_list)
sorted_time = test_sorted(random_list)

print('Время сортировки пузырьком: ', bubble_sort_time)
print('Время сортировки .sort(): ', sorted_time)

if bubble_sort_time < sorted_time:
    print('Пузырек быстрее')
else:
    print('Метод .sort() быстрее')