import sys
import time
import tracemalloc

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.subtree_sum = key

class SplayTree:
    def __init__(self):
        self.root = None

    def _update(self, node):
        if node:
            node.subtree_sum = node.key
            if node.left:
                node.subtree_sum += node.left.subtree_sum
            if node.right:
                node.subtree_sum += node.right.subtree_sum

    def _rotate(self, x):
        p = x.parent
        g = p.parent
        if p.left == x:
            p.left = x.right
            if x.right:
                x.right.parent = p
            x.right = p
        else:
            p.right = x.left
            if x.left:
                x.left.parent = p
            x.left = p
        p.parent = x
        x.parent = g
        if g:
            if g.left == p:
                g.left = x
            else:
                g.right = x
        else:
            self.root = x
        self._update(p)
        self._update(x)

    def _splay(self, x):
        while x.parent:
            p = x.parent
            g = p.parent
            if g:
                if (g.left == p) == (p.left == x):
                    self._rotate(p)
                else:
                    self._rotate(x)
            self._rotate(x)

    def _find(self, key):
        node = self.root
        while node:
            if key == node.key:
                self._splay(node)
                return node
            elif key < node.key:
                if not node.left:
                    self._splay(node)
                    return None
                node = node.left
            else:
                if not node.right:
                    self._splay(node)
                    return None
                node = node.right
        return None

    def add(self, key):
        if not self.root:
            self.root = Node(key)
            return
        node = self.root
        while True:
            if key == node.key:
                self._splay(node)
                return
            elif key < node.key:
                if not node.left:
                    node.left = Node(key)
                    node.left.parent = node
                    self._splay(node.left)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(key)
                    node.right.parent = node
                    self._splay(node.right)
                    return
                node = node.right

    def delete(self, key):
        node = self._find(key)
        if not node:
            return
        self._splay(node)
        if not node.left:
            self._replace(node, node.right)
        elif not node.right:
            self._replace(node, node.left)
        else:
            min_node = self._subtree_min(node.right)
            if min_node.parent != node:
                self._replace(min_node, min_node.right)
                min_node.right = node.right
                min_node.right.parent = min_node
            self._replace(node, min_node)
            min_node.left = node.left
            min_node.left.parent = min_node
        self._update(self.root)

    def _replace(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def _subtree_min(self, node):
        while node.left:
            node = node.left
        return node

    def find(self, key):
        return self._find(key) is not None

    def sum_range(self, l, r):
        if not self.root:
            return 0
        self._find(l)
        if self.root.key < l:
            if not self.root.right:
                return 0
            self.root = self.root.right
            self.root.parent = None
        self._find(r)
        if self.root.key > r:
            if not self.root.left:
                return 0
            self.root = self.root.left
            self.root.parent = None
        return self._subtree_sum(self.root, l, r)

    def _subtree_sum(self, node, l, r):
        if not node:
            return 0
        if node.key < l:
            return self._subtree_sum(node.right, l, r)
        if node.key > r:
            return self._subtree_sum(node.left, l, r)
        return node.key + self._subtree_sum(node.left, l, r) + self._subtree_sum(node.right, l, r)

def read_input(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        operations = [file.readline().strip() for _ in range(n)]
    return operations

def write_output(file_path, results):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(result + "\n")

def main():
    tracemalloc.start()
    start_time = time.time()

    operations = read_input('input.txt')
    tree = SplayTree()
    last_sum = 0

    results = []

    for operation in operations:
        if operation.startswith('+'):
            value = (int(operation[1:]) + last_sum) % 1000000000
            tree.add(value)
        elif operation.startswith('-'):
            value = (int(operation[1:]) + last_sum) % 1000000000
            tree.delete(value)
        elif operation.startswith('?'):
            value = (int(operation[1:]) + last_sum) % 1000000000
            if tree.find(value):
                results.append("Found")
            else:
                results.append("Not found")
        elif operation.startswith('s'):
            l, r = map(int, operation[1:].split())
            l = (l + last_sum) % 1000000000
            r = (r + last_sum) % 1000000000
            last_sum = tree.sum_range(min(l, r), max(l, r))
            results.append(str(last_sum))
            last_sum = (last_sum + 1000000000) % 1000000000 

    write_output('output.txt', results)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Время выполнения: {end_time - start_time} секунд")
    print(f"Использование памяти: текущее = {current / 10**6} MB, пик = {peak / 10**6} MB")

if __name__ == "__main__":
    main()