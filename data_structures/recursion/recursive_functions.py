'''
Recirsive functions

'''
def power_of_2(n):
    if n == 0:
        return 1

    return 2 * power_of_2(n - 1)


# test power_of_2
print(power_of_2(5))
# below line will give error "RecursionError: maximum recursion depth exceeded in comparison"
# print(power_of_2(1000))


def sum_integers(n):
    if n == 1:
        return 1

    return n + sum_integers(n - 1)


# test sum_integers
print(sum_integers(3))


'''
Looking at this, one might think it has a running time of O( 𝑛 ), but that isn't correct due to the slice 
operation array[1:]. This operation will take O( 𝑘 ) time to run where  𝑘  is the number of elements to copy.
So, this function is actually O( 𝑘∗𝑛 ) running time complexity and O( 𝑘∗𝑛 ) space complexity.
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


def sum_array_iter(array):
    result = 0

    for x in array:
        result += x

    return result


arr = [1, 2, 3, 4]
print("sum_array_iter ")
print(sum_array_iter(arr))
