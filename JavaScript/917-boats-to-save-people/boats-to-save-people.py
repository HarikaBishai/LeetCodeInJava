class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        count = 0

        l = 0
        r = n-1

        while l <= r:
            if people[l] + people[r] <= limit:
                count+=1
                l+=1
                r-=1
            elif people[l] + people[r] > limit:
                r-=1
                count+=1

        return count