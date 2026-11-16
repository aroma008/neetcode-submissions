class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rl=[]
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    rl.append(i)
                    rl.append(j)
        return rl
 

            
        