class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}
        for i, num in enumerate(nums):
            diferencia = target - num
            if diferencia in vistos:
                return[vistos[diferencia], i]
            vistos[num] = i
