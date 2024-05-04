import numpy as np
# arr1=np.array([
#     [1,2,3],
#     [4,5,6]
# ]) #2x3
# arr2=np.array([
#     [7,8,9],
#     [10,11,12]
# ]) #2x3
# arr3=np.array([
#     [2,4],
#     [3,8]
# ]) #2x2
# #合併第一個維度用vstack
# result1=np.vstack((arr1,arr2)) #[[1,2,3],[4,5,6],[7,8,9],[10,11,12]] 4x3
# print(result1)
# #合併第二個維度用hstack
# result2=np.hstack((arr1,arr2)) #[[1 2 3 7 8 9 ],[4 5 6 10 11 12]]  2x6
# print(result2)
# result3=np.hstack((arr1,arr2,arr3)) #[[1 2 3 7 8 9 2 4],[4 5 6 10 11 12 3 8]] 2x8
# print(result3)
#切割splitting
arr=np.array([
    [1,3,5,7,9,11],
    [2,4,6,8,10,12]
]) #2x6
result=np.vsplit(arr,2)   
'''
array([[1 3 4 7 9 11]])   1x6
array([[2 4 6 8 10 12]])  1x6
'''
print(result)
result2=np.hsplit(arr,2)  #[[1 3 5],[2 4 6]] [[7 9 11],[8 10 12]]
print(result2)
result3=np.hsplit(arr,3) #[[1 3],[2 4]] [[5 7][6 8]] [[9 11][10 12]]
print(result3)


