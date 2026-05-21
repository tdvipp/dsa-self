'''
https://wiki.vnoi.info/algo/data-structures/disjoint-set-union

Disjoint Set Union - DSU - quản lý hiệu quả tập hợp của các tập hợp

Vấn đề:
* thêm 1 cạnh giữa x và y
* in ra YES nếu x và y nằm trong cùng 1 thành phần liên thông, NO nếu ngược lại

Thiết kế:
* make_set(v) - tạo 1 tập hợp mới chỉ chứa v
* union_sets(a, b) - gộp 2 set a và b thành một
* find_set(v) - tìm đại diện của set chứa v, sử dụng đại diện để kiểm tra x và y có là thành phần liên thông hay không, 
    x và y là thành phần liên thông nếu đại diện của nó giống nhau
'''
# Demo cài đặt cho int
class Naive_DSU:
    def __init__(self, n: int):
        self.parent = [-1 for _ in range(n)]

    def make_set(self, v):
        self.parent[v] = v
    
    def find_set(self, v) -> int:
        if self.parent[v] == v:
            return v
        return self.find_set(self.parent[v])

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b: 
            self.parent[b] = a

    def print(self):
        print(self.parent)
        # find leaves
        par_set = set(self.parent)
        for i in range(n):
            if i in par_set:
                continue
            v = i
            print(v, end = " ")
            while self.parent[v] != v:
                v = self.parent[v]
                print("->", v, end = " ")
            print()

# n = 10
# dsu = Naive_DSU(n)
# for i in range(n):
#     dsu.make_set(i)
# dsu.union_sets(1, 0)
# dsu.union_sets(2, 1)
# dsu.union_sets(3, 2)
# dsu.union_sets(4, 3)
# dsu.union_sets(5, 4)

# dsu.print()

class Optimal_Union_DSU:
    def __init__(self, n: int):
        self.parent = [-1 for _ in range(n)]
        self.size = [-1 for _ in range(n)]
    
    def make_set(self, v):
        self.parent[v] = v
        self.size[v] = 1
    
    def find_set(self, v) -> int:
        if self.parent[v] == v:
            return v
        return self.find_set(self.parent[v])

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b: 
            if self.size[a] < self.size[b]: 
                tmp = a 
                a = b 
                b = tmp 
            
            self.parent[b] = a 
            self.size[a] += self.size[b]

    def print(self):
        print(self.parent)
        print(self.size)
        # find leaves
        par_set = set(self.parent)
        for i in range(n):
            if i in par_set:
                continue
            v = i
            print(v, end = " ")
            while self.parent[v] != v:
                v = self.parent[v]
                print("->", v, end = " ")
            print()

# n = 10
# dsu = Optimal_Union_DSU(n)
# for i in range(n):
#     dsu.make_set(i)
# dsu.union_sets(1, 0)
# dsu.union_sets(2, 1)
# dsu.union_sets(3, 2)
# dsu.union_sets(4, 3)
# dsu.union_sets(5, 4)

# dsu.print()

class Optimal_Union_Find_DSU:
    def __init__(self, n: int):
        self.parent = [-1 for _ in range(n)]
        self.size = [-1 for _ in range(n)]
    
    def make_set(self, v):
        self.parent[v] = v
        self.size[v] = 1
    
    def find_set(self, v) -> int:
        # time comp decrease from O(log n) to O(1)
        if self.parent[v] == v:
            return v
        p = self.find_set(self.parent[v])
        self.parent[v] = p 
        return p

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b: 
            if self.size[a] < self.size[b]: 
                tmp = a 
                a = b 
                b = tmp 
            
            self.parent[b] = a 
            self.size[a] += self.size[b]

    def print(self):
        print(self.parent)
        print(self.size)
        # find leaves
        par_set = set(self.parent)
        for i in range(n):
            if i in par_set:
                continue
            v = i
            print(v, end = " ")
            while self.parent[v] != v:
                v = self.parent[v]
                print("->", v, end = " ")
            print()

n = 10
dsu = Optimal_Union_Find_DSU(n)
for i in range(n):
    dsu.make_set(i)
dsu.union_sets(0, 1)
dsu.union_sets(2, 3)
dsu.union_sets(4, 5)
dsu.union_sets(6, 7)
dsu.union_sets(8, 9)
dsu.print()

dsu.union_sets(0, 2)
dsu.union_sets(4, 7)
dsu.union_sets(8, 4)
dsu.print()

dsu.union_sets(0, 8)
dsu.print()
dsu.find_set(9)
dsu.print()