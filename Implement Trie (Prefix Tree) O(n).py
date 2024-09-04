class Node:
    def __init__(self):
        self.next = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter not in cur.next:
                cur.next[letter] = Node()

            cur = cur.next[letter]

        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            if letter not in cur.next:
                return False

            cur = cur.next[letter]

        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:
            if letter not in cur.next:
                return False
            
            cur = cur.next[letter]

        return True
