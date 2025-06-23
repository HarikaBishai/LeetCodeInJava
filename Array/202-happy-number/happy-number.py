class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        
        while n:
            seen.add(n)
            temp = n
            sum = 0
            while temp > 0:
                sum+= pow(temp%10, 2)
                temp = temp//10
            
            if sum == 1:
                return True
            if sum in seen:
                return False
            
            
            n = sum
        return False