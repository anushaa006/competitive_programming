class TrieNode:
    def __init__(self):
        self.children:Dict[str,TrieNode]={}
        self.isWord=False
        self.value=0

class MapSum:

    def __init__(self):
        self.root=TrieNode()
        self.ans=0
    def insert(self, key: str, val: int) -> None:
        node:TrieNode=self.root
        for c in key:
            node=node.children.setdefault(c,TrieNode())
        node.isWord=True
        node.value=val
        

    def sum(self, prefix: str) -> int:
        def dfs(node: TrieNode) -> int:
            if not node:
                return 0
            total = node.value
            for child in node.children.values():
                total += dfs(child)
            return total

        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]

        return dfs(node)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)