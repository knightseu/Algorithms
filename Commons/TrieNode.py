class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.hasWord = False
        self.str = None

    @classmethod
    def add_word(cls, root, word):
        node = root
        for letter in word:
            child = node.children[ord(letter) - ord('a')]
            if child is None:
                child = TrieNode()
                node.children[ord(letter) - ord('a')] = child
            node = child
        node.hasWord = True
        node.str = word
