'''

def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]
    print("sum_array({})".format(array[1:]))
    return array[0] + sum_array(array[1:])


arr = [1, 2, 3, 4]
print(sum_array(arr))

def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]

    return array[index] + sum_array_index(array, index + 1)

arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))



2nd implementation eliminates the need to do slicing. With the two different functions implemented, let's compare
the running times.

we see, the function sum_array is a polynomial and sum_array_index is linear as we would have predicted.

'''


def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]

    return array[0] + sum_array(array[1:])


def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]

    return array[index] + sum_array_index(array, index + 1)


import matplotlib.pyplot as plt
import statistics
import time

n_steps = 10
step_size = 100
array_sizes = list(range(step_size, n_steps * step_size, step_size))
big_array = list(range(n_steps * step_size))
sum_array_times = []
sum_array_index_times = []

for array_size in array_sizes:
    subset_array = big_array[:array_size]

    start_time = time.time()
    sum_array(subset_array)
    sum_array_times.append(time.time() - start_time)

    start_time = time.time()
    sum_array_index(subset_array, 0)
    sum_array_index_times.append(time.time() - start_time)

plt.scatter(x=array_sizes, y=sum_array_times, label='sum_array')
plt.scatter(x=array_sizes, y=sum_array_index_times, label='sum_array_index')
plt.ylim(
    top=max(sum_array_times + sum_array_index_times),
    bottom=min(sum_array_times + sum_array_index_times))
plt.legend()
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.plot()
plt.show()
