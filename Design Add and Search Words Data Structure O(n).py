class Node:

    def __init__(self):
        self.end = False
        self.next = {}
    
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter not in cur.next:
                cur.next[letter] = Node()
            
            cur = cur.next[letter]

        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                return cur.end

            if word[i] in cur.next:
                return dfs(i + 1, cur.next[word[i]])

            if word[i] != '.':
                return False
            
            for candidate in cur.next:
                if dfs(i + 1, cur.next[candidate]):
                    return True

        return dfs(0, self.root)
