class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        best=float('inf')
        current=0
        for right in range(len(nums)):
            current+=nums[right]
            while current>=target:
                best=min(best,right-left+1)
                current-=nums[left]
                left+=1
       
        if best==float('inf'):
                return 0
        return best
        