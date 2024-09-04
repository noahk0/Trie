class Node:
    def __init__(self):
        self.num = 0
        self.next = {}
        self.end = False
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root, exist = Node(), set()

        for word in words:
            cur = root

            for letter in word:
                if letter not in cur.next:
                    cur.next[letter] = Node()
                
                cur.num += 1
                cur = cur.next[letter]
            
            cur.end = True

        def search(x, y, cur, candidate):
            if cur.end:
                exist.add(candidate)
                cur.end, node = False, root

                for letter in candidate:
                    node.num -= 1

                    if not node.num:
                        break
                    
                    node = node.next[letter]

            if cur.num and 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] in cur.next:
                c, board[x][y] = board[x][y], None

                search(x, y + 1, cur.next[c], candidate + c)
                search(x, y - 1, cur.next[c], candidate + c)
                search(x + 1, y, cur.next[c], candidate + c)
                search(x - 1, y, cur.next[c], candidate + c)

                board[x][y] = c

        for x in range(len(board)):
            for y in range(len(board[0])):
                search(x, y, root, '')

        return exist
