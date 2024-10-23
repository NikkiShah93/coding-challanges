## Find the missing number in the array
## You have been provided with the list of positive integers from 1 to n.
## All the numbers from 1 to n are present except x, and you must find x. 

def find_missing(array):
    if len(array) <= 0:
        return None
    for i in range(1, len(array) + 1):
        if i not in array:
            return i
        
test_array = [1, 3, 4, 5, 6,]
print(find_missing(test_array))