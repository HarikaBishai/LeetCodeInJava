class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_a = set(nums1)
        set_b = set(nums2)
        return [list(set_a-set_b), list(set_b-set_a)]