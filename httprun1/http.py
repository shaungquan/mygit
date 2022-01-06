# a = {"msg":"sucess!","code":0,"data":[{"id":15,"name":"test","sex":"F","age":100,"mail":"283340479@qq.com","create_time":"2021-01-25"}]}
# print(type(a))
# print(a["data"])
#
# b= [1,2,4,2,9,10,7]
# for t in range(1,len(b)):
#     for i in range(1,len(b)):
#         if b[i-1]<b[i]:
#             b[i-1],b[i]=b[i],b[i-1]
# print(b)
# print(b[-1])

#
# test = "312211"
# a = ""
# b = []
# for i in test:
#     if len(a) == 0:
#         a = i
#     else:
#         if a[-1] == i:
#             a += i
#         else:
#             b.append(a)
#             a = i
# else:
#     if len(a):
#         b.append(a)
# y=""
# print(b)
# for x in b:
#     if len(x) == 0:
#         continue
#     else:
#         y = y + str(len(x)) + str(x[0])
# print(y)

# class test_item():
#
#     def __init__(self,a):
#         self.k = str(a)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         a = ""
#         b = []
#         for i in self.k:
#             if len(a) == 0:
#                 a = i
#             else:
#                 if a[-1] == i:
#                     a += i
#                 else:
#                     b.append(a)
#                     a = i
#         else:
#             if len(a):
#                 b.append(a)
#         y = ""
#         print(b)
#         for x in b:
#             if len(x):
#                 y = y + str(len(x)) + str(x[0])
#         self.k = y
#         return y
#
# my_test = test_item(1)
# my_test_item = iter(my_test)
# print(next(my_test_item))
# print(next(my_test_item))
# print(next(my_test_item))
# print(next(my_test_item))
# print(next(my_test_item))



# a = "abcdefg"
# print(a[0:len(a)])
# x=3
# m=[]
# if len(a) >= x:
#     for i in range(len(a)):
#         k = a[i:i+x]
#         m.append(k)
#         if k[-1] == a[-1]:
#             break
# print(m)

key = "124"
body = {"qname":"test1","pwd":1234,"koko":"","sign":""}
a=[b for b in body.items()]
new_body = [str(i)+str(b) for i,b in a if i != "sign" and b]
new_body.sort()
print(new_body)
str_body = "".join(new_body)
print(str_body+str(key))
