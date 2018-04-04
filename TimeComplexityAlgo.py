#Pratik Prabhakar

'''
This gathers time performance data for a quick and insertion sorting algorithms.
'''
#Importing various python classes used for executing the program
import insertion_sort as i_sort
import quick_sort as q_sort
import time
import random

#Making dictionary for storing data and its time for various sorting algo
# in increasing order
quickSort_Inc_time = {}
insertionSort_Inc_time = {}

#Making dictionary for storing data and its time for various sorting algo
#in decreasing order
quickSort_Dec_time = {}
insertionSort_Dec_time = {}

#Making dictionary for storing data and its time for various sorting algo
#using random order
quickSort_Rnd_time = {}
insertionSort_Rnd_time = {}

#List which contains the time duration taken for executing the alogorithm
#for various inputs
duration_qSort = []
duration_iSort = []
quick_Dict = {}

def quick_sort(s):
    # Wrapper for GTG inplace quicksort
    q_sort.inplace_quick_sort(s, 0, len(s)-1)
   
def insert_sort(s): 
    # Wrapper for GTG inplace insertion sort
    i_sort.insertion_sort(s)

'''
Executing the time complexity for both the algorithms and storing it in the list
for data in increasing order 
'''
randomList_Increasing=[]
for i in range(100,1000+1,25):
    randomList_Increasing.append(i)
    q_sort_Start_time = time.clock()
    quick_sort(randomList_Increasing)
    q_sort_End_time = time.clock()
    q_sort_Duration = q_sort_End_time - q_sort_Start_time
    duration_qSort.append(q_sort_Duration)

    i_sort_Start_time = time.clock()
    insert_sort(randomList_Increasing)
    i_sort_End_time = time.clock()
    i_sort_Duration = i_sort_End_time - i_sort_Start_time
    duration_iSort.append(i_sort_Duration)

    for j in duration_qSort:
        quickSort_Inc_time[i] = j
    for k in duration_iSort:
        insertionSort_Inc_time[i] = k
print("Quick Sort in Increasing Order: ",quickSort_Inc_time)
print("Insertion Sort in Increasing Order: ",insertionSort_Inc_time)

'''
Executing the time complexity for both the algorithms and storing it in the list
for data in decreasing order 
'''
randomList_Decreasing=[]
for i in range(1000,100-1,-25):
    randomList_Decreasing.append(i)
    q_sort_Start_time = time.clock()
    quick_sort(randomList_Decreasing)
    q_sort_End_time = time.clock()
    q_sort_Duration = q_sort_End_time - q_sort_Start_time
    duration_qSort.append(q_sort_Duration)

    i_sort_Start_time = time.clock()
    insert_sort(randomList_Decreasing)
    i_sort_End_time = time.clock()
    i_sort_Duration = i_sort_End_time - i_sort_Start_time
    duration_iSort.append(i_sort_Duration)

    for j in duration_qSort:
        quickSort_Dec_time[i] = j
    for k in duration_iSort:
        insertionSort_Dec_time[i] = k
print("Quick Sort in Decreasing Order: ",quickSort_Dec_time)
print("Insertion Sort in Decreasing Order: ",insertionSort_Dec_time)

'''
Executing the time complexity for both the algorithms and storing it in the list
for data in random order 
'''
randomList_Random=[]
for i in range(20):
    randomNo = random.randrange(100,1000,25)
    randomList_Random.append(randomNo)
    q_sort_Start_time = time.clock()
    quick_sort(randomList_Random)
    q_sort_End_time = time.clock()
    q_sort_Duration = q_sort_End_time - q_sort_Start_time
    duration_qSort.append(q_sort_Duration)

    i_sort_Start_time = time.clock()
    insert_sort(randomList_Random)
    i_sort_End_time = time.clock()
    i_sort_Duration = i_sort_End_time - i_sort_Start_time
    duration_iSort.append(i_sort_Duration)

    for j in duration_qSort:
        quickSort_Rnd_time[randomNo] = j
    for k in duration_iSort:
        insertionSort_Rnd_time[randomNo] = k

print("Quick Sort in Random Order: ",quickSort_Rnd_time)
print("Insertion Sort in Random Order: ",insertionSort_Rnd_time)
