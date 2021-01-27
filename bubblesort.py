def bubbleSort(alist):
            if alist[1]>alist[2]:
                temp = alist[1]
                alist[1] = alist[2]
                alist[2] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)