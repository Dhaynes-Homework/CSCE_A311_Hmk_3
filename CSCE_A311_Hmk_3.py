# Devan Haynes
# CSCE_A311_Hmk_3.py
# Used for CSCE A311 Homework Assignment 3
# NEEDS "word.txt" in same folder to work

# 4 Sorting algorithms:
#   Selection Sort
#   Insertion Sort
#   Merge Sort
#   Quick Sort

# Purpose is to compair sorting times and to built the sorting algorithms

# Sorting algorithms are based off the desciptions provided in the slides and found online (geeks for geeks)

compareNum = 0
swapNum = 0
LENTOSORT = 5000

# Selection Sort
def selectionSort(list):
    global compareNum 
    global swapNum
    compareNum = 0
    swapNum = 0

    for i in range(len(list)-1,0,-1):
        maxNum=0
        for location in range(1,i+1):
            compareNum = compareNum + 1
            if list[location] > list[maxNum]:
                maxNum = location

        temp = list[i]
        list[i] = list[maxNum]
        list[maxNum] = temp
        swapNum = swapNum + 1
       
# Insertion Sort
def insertionSort(list):
    global compareNum 
    global swapNum
    compareNum = 0
    swapNum = 0

    for index in range(1,len(list)):

        current = list[index]
        position = index

        while position>0 and list[position-1] > current:
            compareNum = compareNum + 1

            list[position] = list[position-1]
            swapNum = swapNum + 1
            position = position-1

        compareNum = compareNum + 1 # plus one comparison because it doesn't enter the while loop on the end compairison
        list[position] = current

# Merge sort    
def mergeSort(list):
    global compareNum 
    global swapNum

    if len(list) >= 2:

        mid = len(list)//2 #could also use floor math function but this works that same (it is interger division so it truncates the number)
        leftHalf = list[:mid]
        rightHalf = list[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=0
        j=0
        k=0
        while i < len(leftHalf) and j < len(rightHalf):

            compareNum = compareNum + 1
            swapNum = swapNum + 1 # counting each time it place a number in an array as a swap

            if leftHalf[i] < rightHalf[j]:
                list[k] = leftHalf[i]
                i = i + 1
            else:
                list[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf): #Not counting as a compare
            swapNum = swapNum + 1
            list[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):  #Not counting as a compare
            swapNum = swapNum + 1
            list[k] = rightHalf[j]
            j = j + 1
            k = k + 1

# Quick Sort
def quickSort(list,first,end):


    if first < end:

       split = partition(list,first,end)

       quickSort(list,first,split-1) # left split
       quickSort(list,split+1,end) # right split

# Partion
# Used in quick sort
# Pivots around first element
def partition(list,first,end):
    global compareNum 
    global swapNum

    pivot = list[first]

    right = end
    left = first+1
    loop = False

    while not loop:

        while left <= right and list[left] <= pivot:
            compareNum = compareNum + 1
            left = left + 1

        compareNum = compareNum + 1 # plus one comparison because it doesn't enter the while loop on the end compairison

        while list[right] >= pivot and right >= left:
            compareNum = compareNum + 1
            right = right - 1

        compareNum = compareNum + 1 # plus one comparison because it doesn't enter the while loop on the end compairison

        if right < left:
            compareNum = compareNum + 1
            loop = True

        else:
            compareNum = compareNum + 1  # plus one comparison because it compared on the if statment
            swapNum = swapNum + 1
            temp = list[left]
            list[left] = list[right]
            list[right] = temp

    swapNum = swapNum + 1
    temp = list[first]
    list[first] = list[right]
    list[right] = temp


    return right

def printArray(list):
    print (*list, sep = "\n")



# Reading in from words .txt and placing it in an array

object = open("words.txt", "r")
stringList = []
for word in object.read().split():
    stringList.append(word)

stringList = stringList[:LENTOSORT]

# Printing out stats on sorts

copyList = stringList [:LENTOSORT]
insertionSort(copyList)
print("Insertion Sort")
print("The number of swaps is: ", swapNum)
print("The number of comparisons is: ", compareNum)
compareNum = 0
swapNum = 0


copyList = stringList [:LENTOSORT]
selectionSort(copyList)
print("Selection Sort")
print("The number of swaps is: ", swapNum)
print("The number of comparisons is: ", compareNum)
compareNum = 0
swapNum = 0


copyList = stringList [:LENTOSORT]
mergeSort(copyList)
print("Merge Sort")
print("The number of swaps is: ", swapNum)
print("The number of comparisons is: ", compareNum)
compareNum = 0
swapNum = 0

copyList = stringList [:LENTOSORT]
quickSort(copyList, 0, len(copyList) - 1)
print("Quick Sort")
print("The number of swaps is: ", swapNum)
print("The number of comparisons is: ", compareNum)

answer = input("Do you want to print the sorted array? (yes to print): ")
ans = "yes"
if answer == ans:
    printArray(copyList)

