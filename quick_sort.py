from random import randint
def partition(sort_nums, begin, end):
    part = begin
    for i in range(begin+1, end+1):
        if sort_nums[i] <= sort_nums[begin]:
            part += 1
            sort_nums[i], sort_nums[part] = sort_nums[part], sort_nums[i]
    sort_nums[part], sort_nums[begin] = sort_nums[begin], sort_nums[part]
    return part
def quick_sort(sort_nums, begin=0, end=None):
    if end is None:
        end = len(sort_nums) - 1
    def quick(sort_nums, begin, end):
        if begin >= end:
            return
        part = partition(sort_nums, begin, end)
        quick(sort_nums, begin, part-1)
        quick(sort_nums, part+1, end)
    return quick(sort_nums, begin, end)
nums = random_list=[]
for i in range(10):
    random_list.append(randint(1,30))
quick_sort(nums)
print(nums)
