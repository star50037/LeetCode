class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         elif int(nums[i]) + int(nums[j]) == target:
        #             return (i, j)
        
        # dic = {}
        # for i, n in enumerate(nums): 
        #     if n in dic:
        #         return [dic[n], i]
        #     dic[target-n] = i
            
            
       
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[target - nums[i]] = i
            else:
                return dic[nums[i]], i