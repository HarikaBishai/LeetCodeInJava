class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        dp = {"": [""]}

        def dfs(digits):
            if digits in dp:
                return dp[digits]
            
            first_digit = mapping[digits[0]]
            remaining = digits[1:]
            remaining_comb = dfs(remaining)
            result = []
            for c in first_digit:
                for comb in remaining_comb:
                    result.append(c + comb)
            dp[digits] = result
            return result
        
        result = dfs(digits)
        return [] if result == [""] else result