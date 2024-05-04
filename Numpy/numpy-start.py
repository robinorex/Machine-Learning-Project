import numpy as np
# ndarr=np.array([1,2,3,4])  #根據列表建立ndarray物件
# print(ndarr)
# print(ndarr.size)
#一維陣列
# data=np.empty(4)  #創造一個一維陣列未指定數字
# print(data)
# data=np.ones(3)
# print(data)
# data=np.arange(5)   #0-4
# print(data)
#二維陣列
# print(np.zeros([3,2]))
# print(np.empty([3,3]))
# data=np.array([
#     [3,5,3],
#     [6,26,6],
#     [4,2,1]
# ])  #3*3得二維陣列
# print(data)
# #三維陣列
# print(np.zeros([2,2,3]))
# print(np.ones([1,2,3]))
#四維
data=np.array([
    [
        [
            [3,4],
            [5,6]
        ]
    ]
])
print(data) #1*1*2*2四維陣列