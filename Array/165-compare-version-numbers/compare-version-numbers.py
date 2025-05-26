class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        i=0
        while i<len(version1) or i<len(version2):
            part1 = version1[i] if i < len(version1) else "0"
            part2 = version2[i] if i < len(version2) else "0"

            part1.lstrip("0")
            part2.lstrip("0")
            part1 = int(part1)
            part2 = int(part2)


            if int(part1) > int(part2):
                return 1
            elif int(part2) > int(part1):
                return -1
            
            i+=1
        return 0


