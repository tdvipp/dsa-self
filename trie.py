'''
https://wiki.vnoi.info/algo/string/trie

Trie - cây tiền tố - quản lý tập hợp các xâu.

Vấn đề:
* kiểm tra tiền tố
* kiểm tra xâu
* thêm xâu vào tập hợp
* xoá xâu khỏi tập hợp

Thiết kế:
* class Node - lưu lại số lượng tiền tố và số lượng xâu, sử dụng mảng 26 phân tử tương ứng bảng chữ cái để lookup nhanh
* add_string - lặp qua từng ký tự trong string và thêm nó vào cây
* find_string - lặp qua từng ký tự trong string và kiểm tra sự tồn tại của nó
* delete_string_recursive - đệ quy để xoá xâu và các ký tự không còn xuất hiện
'''
# pointer version
from __future__ import annotations

class Trie:
    class Node:
        def __init__(self):
            self.child = [None for _ in range(26)]
            self.exist = 0
            self.cnt = 0

    def __init__(self):
        self.root = self.Node()

    def add_string(self, s: str):
        p = self.root 
        for f in s:
            c = ord(f) - ord('a')
            if p.child[c] == None:
                p.child[c] = self.Node()

            p = p.child[c]
            p.cnt += 1 # how many string have this prefix
        p.exist += 1 # how many string end with this

    def find_string(self, s: str) -> bool:
        p = self.root
        for f in s: 
            c = ord(f) - ord('a')
            if p.child[c] == None :
                return False
            p = p.child[c] 
        
        return p.exist != 0

    def delete_string(self, s: str):
        if self.find_string(s) == False:
            return 
        
        self.delete_string_recursive(self.root, s, 0)

    def delete_string_recursive(self, p: Trie.Node, s: str, i) -> bool:
        if i != len(s):
            c = ord(s[i]) - ord('a')
            is_child_deleted = self.delete_string_recursive(p.child[c], s, i + 1)
            if is_child_deleted:
                p.child[c] = None
        else:
            p.exist -= 1
        
        if p != self.root:
            p.cnt -= 1
            if p.cnt == 0:
                del p
                return True 
        return False 

    def print(self):
        # CLAUDE WRITE THIS FOR ME
        def dfs(node, prefix, is_last, indent):
            connector = "└── " if is_last else "├── "
            label = f"{prefix[-1]}  (cnt={node.cnt}, exist={node.exist})" if prefix else "(root)"
            print(indent + connector + label if prefix else "(root)")
            children = [(chr(ord('a') + i), node.child[i]) for i in range(26) if node.child[i]]
            child_indent = indent + ("    " if is_last else "│   ")
            for j, (ch, child) in enumerate(children):
                dfs(child, prefix + ch, j == len(children) - 1, child_indent)

        print("(root)")
        children = [(chr(ord('a') + i), self.root.child[i]) for i in range(26) if self.root.child[i]]
        for j, (ch, child) in enumerate(children):
            dfs(child, ch, j == len(children) - 1, "")

t = Trie()
t.add_string('apple')
t.add_string('app')
t.add_string('apply')
t.add_string('bat')
t.print()
t.delete_string('apply')
t.print()