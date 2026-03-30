class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        
        graph = defaultdict(list)

        for w1, w2 in similarPairs:
            graph[w1].append(w2)
            graph[w2].append(w1)
        

        path = set()
        def dfs(src, target, visited):
            if src == target:
                return True

            visited.add(src)
            
            
            for nei in graph[src]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            
            return False
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            visited = set()
            if not dfs(sentence1[i], sentence2[i], visited):
                return False
        return True

            

