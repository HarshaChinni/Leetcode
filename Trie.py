class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def getIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # First check the first charecter is there in the root node's children or not
        tmpNode = self.root

        # Post that we need to keep repeating in the process in the nodes to come, we either have the char or have to create a new one
        for ch in word:
            chIdx = self.getIndex(ch)

            if not tmpNode.children[chIdx]:
                tmpNode.children[chIdx] = TrieNode()

            # Then change the acting node from the root --> new char node
            tmpNode = tmpNode.children[chIdx]

        tmpNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmpNode = self.root

        for ch in word:
            chIdx = self.getIndex(ch)

            if not tmpNode.children[chIdx]:
                return False

            tmpNode = tmpNode.children[chIdx]

        return tmpNode.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmpNode = self.root

        for ch in prefix:
            chIdx = self.getIndex(ch)

            if not tmpNode.children[chIdx]:
                return False

            tmpNode = tmpNode.children[chIdx]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
