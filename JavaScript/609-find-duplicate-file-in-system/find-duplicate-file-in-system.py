class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for path in paths:
            path = path.split(" ")
            directory = path[0]
            for file in path[1:]:
                fileSplit = file.split('(')
                fileName = fileSplit[0]
                fileContent = fileSplit[1].rstrip(')')
                groups[fileContent].append(f"{directory}/{fileName}")
        
        return [x for x in groups.values() if len(x) > 1]
