import random, math
arr = []
for i in range(0,100):
    arr.append(int(math.floor(random.random()*10000)))


def selectionSort(arr):

    for i in range(0,len(arr)):
        minNum = i #store index of first element

        for j in range(i,len(arr)):
            if arr[j] < arr[minNum]:
                minNum = j
        temp = arr[i]
        arr[i] = arr[minNum]
        arr[minNum] = temp
    return arr

print selectionSort(arr)

