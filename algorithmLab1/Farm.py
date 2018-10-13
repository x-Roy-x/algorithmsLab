import time

farmList = []


class Farm():
    def __init__(self, location, number_of_animals, power_fans):
        self.location = location
        self.number_of_animals = number_of_animals
        self.power_fans = power_fans


with open('Text') as Text:
    for line in Text:
        values = line.split(",")
        farm = Farm(values[0], int(values[1]), int(values[2][0:]))
        farmList.append([farm.location, farm.number_of_animals, farm.power_fans])


def bubble_sort(a, b):
    counter_bubble1 = 0
    counter_bubble2 = 0
    j = 1
    while j < len(a):
        k = 0
        counter_bubble1 += 1
        while k < (len(a) - 1):
            counter_bubble1 += 1
            if a[k][b] < a[k + 1][b]:
                a[k], a[k + 1] = a[k + 1], a[k]
                counter_bubble1 += 1
                counter_bubble2 += 1
            k += 1
        j += 1
    print("Кількість операцій порівняння: ", counter_bubble1)
    print("Кількість операцій обміну: ", counter_bubble2)
    print(a)


def merge_sort(a):
    if len(a) <= 1:
        return a
    list_mid = int(len(a) / 2)
    left = merge_sort(a[:list_mid])
    right = merge_sort(a[list_mid:])
    return merge(left, right)


def merge(left_list, right_list):
    result = []
    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i][1] <= right_list[j][1]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    result += left_list[i:]
    result += right_list[j:]
    return result


print("List")
print(farmList)

animal = farmList.copy()
print("Merge")
start_time = time.clock()
a = merge_sort(animal)
print("Time: " + str(time.clock() - start_time))
print(a)

fans_sort = farmList.copy()
print("Bubble")
start_time = time.clock()
fans_sort = bubble_sort(fans_sort, 2)
print("Time: " + str(time.clock() - start_time))
