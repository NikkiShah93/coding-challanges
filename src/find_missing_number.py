## Find the missing number in the array
## You have been provided with the list of positive integers from 1 to n.
## All the numbers from 1 to n are present except x, and you must find x. 
import time

def find_missing(array):
    if len(array) <= 0:
        return None
    for i in range(1, len(array) + 1):
        if i not in array:
            return i
        
## other approach
def find_missing_num(array):
    sum_num = sum(array)
    expected_sum = sum(range(1, len(array) + 1))

    return int(abs(expected_sum - sum_num)/2)
        
test_array = [1, 3, 4, 5, 6,]
first_func_start = time.time()
print(find_missing(test_array))
first_func_end = time.time()

second_func_start = time.time()
print(find_missing_num(test_array))
second_func_end = time.time()

print(f"First function time: {round(first_func_end - first_func_start, 4)}")
print(f"Second function time: {round(second_func_end - second_func_start, 4)}")