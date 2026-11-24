class Solution:
    from collections import defaultdict
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen=defaultdict(int,{0:1})
        running=0
        count=0
        for x in nums:
            running+=x
            count+=seen[running-k]
            seen[running]+=1
        return count