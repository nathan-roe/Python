import math
# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(list):
    for i in range(0, len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
# print(biggie_size([1,2,3,4,5.-1,0,-4,3,2]))
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positives(list):
    count = 0
    for i in range(0, len(list)):
        if list[i] > 0:
            count += 1
    list[len(list)-1] = count
    return list
# print(count_positives([1,2,-3,-4,-5,6,7,8,9]))
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
def sum_total(list):
    count = 0
    for x in list:
        count += x
    return count
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
# Average - Create a function that takes a list and returns the average of all the values.x
def average(list):
    count = 0
    for x in list:
        count += x
    return count / len(list)
# print(average([1,2,3,4,5,6,7,8,9]))
# Example: average([1,2,3,4]) should return 2.5
# Length - Create a function that takes a list and returns the length of the list.
def length(list):
    return len(list)
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(list):
    min = list[0]
    for x in list:
        if x < min:
            min = x
    return min
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
def maximum(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(list):
    sum_total = 0
    min = list[0]
    max = list[0]
    my_dict = {"sum": 0, "average": 0, "min": 0, "max": 0}
    for x in list:
        if x < min:
            min = x
        if x > max:
            max = x
        sum_total += x
    my_dict["sum"] = sum_total
    my_dict["average"] = sum_total / len(list)
    my_dict["min"] = min
    my_dict["max"] = max
    return my_dict
# print(ultimate_analysis([1,2,3,4,5,6,7,8,9]))
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse_list(list):
    for i in range(0, math.floor(len(list)/2), 1):
        temp = list[i]
        list[i] = list[len(list) - (1 + i)]
        list[len(list) - (1 + i)] = temp
    return list
print(reverse_list([1,2,3,4,5,6,7,8,9]))
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]