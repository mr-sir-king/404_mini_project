from Sort import *
import random as rnd
import time

arr1 = [20, 80, 10, 50, 90, 30, 0, 70]
arr2 = []



for x in range(10): arr2.append(rnd.randint(0, 100))

sort = Sort(arr2, "array")



def array_to_string(array):
    temp_array = f"{sort.get_name()}"
    for x in array:
        temp_array = temp_array + "[" + str(x) + "]"
    return temp_array

print(sort)
start = time.time()
print(sort.quick_sort())
end = time.time()
print()
delta = ((end - start) * 1000) * 1000
print(f"{delta} microseconds\n")

print(sort)
start = time.time()
print(sort.merge_sort())
end = time.time()
print()
delta = ((end - start) * 1000) * 1000
print(f"{delta} microseconds\n")
