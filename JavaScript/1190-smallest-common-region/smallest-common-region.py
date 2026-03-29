class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        parentObj = defaultdict(str)

        for region in regions:
            parent = region[0]
            for sub in region[1:]:
                parentObj[sub] = parent
        

        region1_pset = set()

        while region1:
            region1_pset.add(region1)
            region1 = parentObj.get(region1)
        
        while region2 not in region1_pset:
            region2 = parentObj[region2]
        
        return region2
        