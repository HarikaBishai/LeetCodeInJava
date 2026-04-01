class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)

        path = []
        res = []

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return 
            

            for num in counter:
                if counter[num] > 0:
                    counter[num]-=1
                    path.append(num)
                    dfs()
                    path.pop()
                    counter[num]+=1
        
        dfs()
        return res