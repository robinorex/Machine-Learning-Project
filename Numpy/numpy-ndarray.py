import numpy as np
#1)element wise
# data1=np.array([1,2,3,4])
# data2=np.array([4,7,8,3])
# print(data1+data2)
# print(data1*data2)
# print(data1/data2)
# print(data1>data2)
# print(data1==data2)
#2)matrix
data1=np.array([
    [1,2]
])  #1x2
data2=np.array([
    [2,3,8],
    [3,6,12]
])  #2x3
# result=data1.dot(data2)   #內積
# result=data1@data2
# print("內積",result)   #1x3矩陣
# result2=np.outer(data1,data2)
# print("外積",result2)   #2x6矩陣
#Statistics
# data=np.array([
#     [2,3,1],
#     [6,4,5],
#     [3,6,9]
# ])
# result=data.sum(axis=0)   #直向加總
# result=data.sum(axis=1)   #row sum橫向加總
# result=data.mean(axis=1)
# result=data.cumsum() #逐值累加
# result=data.cumsum(axis=0)
# print(result)
# print(data.T)  #轉置
# print(data.ravel())  #ravel()打平成一維陣列[2 3 1 6 4 5 3 6 9]
# data=np.array([
#     [[2,3,1],[4,6,7]],
#     [[3,6,9],[5,8,4]]
# ])  #2x2x3
# print(data.shape)
# print(data.ravel())
# print(data.T)
# print(data.reshape(3,4))   #(列,行)
# print(np.zeros(18).reshape(2,3,3))  #重塑資料 總數量必須一樣
# data=np.ones(10)
# print(data)
# newData=data.ravel()   #扁平化資料
# print(newData)   
# print(data.reshape(1,2,6))
# data=np.arange(8).reshape(2,4)
# print(data)
# print(data.T)
#slicing資料的切片
# data=np.array([3,5,6,2,4,3])
# print(data[:4])    #[3 5 6 2] 向左包頭不包尾
# print(data[3:])
# print(data[3:5])
# data=np.array([
#     [[2,3,1],[4,6,7]],
#     [[3,6,9],[5,8,4]]
# ])  
# print(data[0:2,1:2])
# data=np.array([
#     [2,3,1],[4,7,8],
#     [3,5,6],[2,3,2]
# ])
# print(data.shape)
# print(data[0:3,2])
# print(data[...,0:2])
# print(data[1,...])

# data=np.array([
#     [3,4,5],[1,2,3],
#     [2,2,2],[1,2,1]
# ])   #4x3
# print(data[0:2,1])  #[4 2]
# print(data[1:3,0:2])  #[[1,2],[2,2]]
data=np.array([
    [
        [8,1,3],
        [5,5,2]
    ],
    [
        [6,4,2],
        [5,1,5]
    ]
])
print(data.shape)  #(2,2,3)
print(data[0,...])  #[[8 1 3] [5 5 2]]
print(data[...,1:3]) #[[[1 3],[5 2]],[[4 2],[1 5]]] 前面兩層全都要 最後一層1:3
data2=np.arange(8)
print(data2)