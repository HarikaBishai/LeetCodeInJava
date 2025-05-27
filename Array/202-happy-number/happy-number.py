class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n not in seen:
            temp = n
            seen.add(n)
            sum = 0
            while temp > 0:
                sum += pow(temp%10, 2) 
                temp = temp//10
            if sum == 1:
                return True
            n = sum
            
            
        return False
