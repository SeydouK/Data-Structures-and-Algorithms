def contains_duplicate_naive(nums: list) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == nums[i]:
                return True
    return False

print(contains_duplicate_naive([12,3,12,5,6,0]))

def contains_duplicate(nums:list[int]) -> bool:
    seen = set()
    for i in nums: 
        if i in seen:
            return True 
        seen.add(i)
    return False

print(contains_duplicate([12,3,12,5,6,0]))
