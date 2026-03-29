class TrieNode:
    def __init__(self):
        self.children = {}
        self.deleted = False
        self.serial = ""

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        
        root = TrieNode()
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
            
        serial_count = defaultdict(int)
        def serialize(node):
            if not node.children:
                node.serial = ""
                return ""
            parts = []
            for name in sorted(node.children):
                child = node.children[name]
                child_serialized = serialize(child)
                parts.append(f"({name}{child_serialized})")
            node.serial = "".join(parts)
            serial_count[node.serial]+=1
            return node.serial
        serialize(root)

        def mark_deleted(node):
            for child in node.children.values():
                mark_deleted(child)
            if node.serial and serial_count[node.serial] > 1:
                node.deleted = True
        mark_deleted(root)
        out = []
        def collect(node, path):
            for name, child in node.children.items():
                if child.deleted:
                    continue
                path.append(name)
                out.append(path[:])
                collect(child, path)
                path.pop()
        collect(root,[])

        return out

