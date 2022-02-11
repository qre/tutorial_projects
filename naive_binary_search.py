import random
import math
import time
#naive search:scan entire list and ask if any of the elements are equal to our goal
#if yes -> return index
#no -> return -1
def naive_search(x, goal):
    for i in range(len(x)):
        if x[i] == goal:
            return i
    return -1

#binary search is a divide and conquer type of search
#only works for ordered lists
def binary_search(x, goal, low=None, high=None):
    if low is None:
        low=0
    if high is None:
        high = len(x)-1

    if high < low:
        return -1
    mid = (low + high) // 2

    if x[mid] == goal:
        return mid
    elif goal < x[mid]:
        return binary_search(x, goal, low, mid-1)
    else:
        return binary_search(x, goal, mid+1, high)

if __name__=='__main__':
    #x = [1, 3, 5, 10, 12]
    #goal =10
    #print(naive_search(x, goal))
    #print(binary_search(x, goal))

    length = 10000
    #build sorted list with 10000 length
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-5*length, 5*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for goal in sorted_list:
        naive_search(sorted_list, goal)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for goal in sorted_list:
        binary_search(sorted_list, goal)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")
