class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        if len(words) == 1:
            return "".join(list(set(words[0])))

        graph = defaultdict(list)

        indegree = {c: 0 for word in words for c in word}

        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]

            n1 = len(word1)
            n2 = len(word2)

            minLen = min(n1, n2)

            if word1[:minLen] == word2[:minLen] and n1 > n2:
                return ""
            
            for j in range(minLen):
                if word1[j]!=word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]]+=1
                    break
        

        q = deque()
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)
        
        out = []

        while q:
            node = q.popleft()
            out.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return "" if len(out)!= len(indegree) else "".join(out)