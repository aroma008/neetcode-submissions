class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ns = [1] * len(nums)

        p = 1
        for i in range(len(nums)):
            ns[i] = p
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            ns[i] *= p
            p *= nums[i]

        return ns

        
            

        