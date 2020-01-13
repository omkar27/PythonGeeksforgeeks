def duplicate(x):
    _size = len(x)
    repeated = []

    for i in range(_size):
        k = i+1
        for j in range(k,_size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    print repeated

x = [1,2,3,4,5,61,2,3,7,8,9,8,0,65,98,90,345,2,23,23]
duplicate(x)



















# def Repeat(x):
#     _size = len(x)
#     repeated = []
#     for i in range(_size):
#         k = i + 1
#         for j in range(k, _size):
#             if x[i] == x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#     return repeated
#
#
# # Driver Code
# list1 = [10, 20, 30, 20, 20, 30, 40,
#          50, -20, 60, 60, -20, -20]
# print (Repeat(list1))
