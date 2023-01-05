class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx1, idx2 = 0, 1
        endIdx = len(nums) - 1

        while((nums[idx1] + nums[idx2]) != target):
            if idx2 == endIdx:
                idx1+=1
                idx2 = idx1 + 1
            else:
                idx2+=1

        return [idx1, idx2]