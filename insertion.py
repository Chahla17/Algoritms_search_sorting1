from random import randint

items = list(range(100))

def insertion(list_nums):
    for i in range(1, len(list_nums)):
        item = list_nums[i]
        i2 = i - 1
        while i2 >= 0 and list_nums[i2] > item:
            list_nums[i2 + 1] = list_nums[i2]
            i2 -= 1
        list_nums[i2 + 1] = item
random_list=[]
for f in range(10000):
    random_list.append(randint(1,100))

insertion(random_list)
print(random_list)
