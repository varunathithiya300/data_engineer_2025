l1 = [1, 3, 5, 7, 9]
it_l1 = iter(l1)

# print(it_l1.__next__())
# print(it_l1.__next__())
# print(it_l1.__next__())
# print(it_l1.__next__())
# print(it_l1.__next__())
# print(it_l1.__next__())

def countUpto(n):
    i = 1
    while i <= n:
        yield i
        i = i+1

gen = countUpto(9)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
# print(gen.__next__())


import time

currenttime= time.localtime(time.time())
print ("Current time is", currenttime)