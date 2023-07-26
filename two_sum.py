class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsmap={}
        n=len(nums)
        for i in range(n):
            numsmap[nums[i]]=i
        for i in range(n):
            complement=target-nums[i]
            if complement in numsmap and numsmap[complement]!=i:
                return [i,numsmap[complement]]
        return []
