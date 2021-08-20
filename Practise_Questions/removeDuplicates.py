def removeDuplicates(nums):
    sorted_set_nums = sorted(set(nums))
    empty_places_count = len(nums) - len(sorted_set_nums)


removeDuplicates([0,0,1,1,1,2,2,3,3,4])