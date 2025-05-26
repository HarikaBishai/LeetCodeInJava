class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")



        def compare(part1, part2):
            part1.lstrip("0")
            part2.lstrip("0")
        


            if int(part1) > int(part2):
                return 1
            elif int(part2) > int(part1):
                return -1
            else:
                return 0

        i = 0

        
        while i<len(version1) or i<len(version2):
            part1 = version1[i] if i < len(version1) else "0"
            part2 = version2[i] if i < len(version2) else "0"

            val = compare(part1, part2)
            if val!= 0:
                return val
            
            i+=1
        return 0


