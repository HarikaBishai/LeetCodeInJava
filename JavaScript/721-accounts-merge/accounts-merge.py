class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
        

        def union(u, v):
            parentu = find(u)
            parentv = find(v)
            if parentu != parentv:
                parent[parentv] = parentu
            
        
        email_to_name = {}

        for account in accounts:
            name = account[0]
            firstEmail = account[1]
            for email in account[1:]:
                union(firstEmail, email)
                email_to_name[email] = name
        
        groups = defaultdict(list)

        for email in email_to_name:
            root = find(email)
            groups[root].append(email)
        out = []
        for root, emails in groups.items():
            out.append([email_to_name[root]] + sorted(emails))
        return out
