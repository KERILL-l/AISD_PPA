import time
import psutil
import os

def read_input(file_name):
    with open(file_name, 'r') as f:
        n = int(f.readline().strip())
        nodes = []
        for _ in range(n):
            nodes.append(list(map(int, f.readline().strip().split())))
    return n, nodes

def is_bst_util(nodes, node_index, min_key, max_key):
    if node_index == -1:
        return True
    key, left, right = nodes[node_index]
    if key < min_key or key > max_key:
        return False
    return (is_bst_util(nodes, left, min_key, key - 1) and
            is_bst_util(nodes, right, key + 1, max_key))

def is_bst(nodes):
    if not nodes:
        return True
    return is_bst_util(nodes, 0, float('-inf'), float('inf'))

def main():
    process = psutil.Process(os.getpid())
    start_time = time.time()
    start_memory = process.memory_info().rss

    n, nodes = read_input('input.txt')
    if n == 0:
        result = "CORRECT"
    else:
        result = "CORRECT" if is_bst(nodes) else "INCORRECT"

    with open('output.txt', 'w') as f:
        f.write(result + '\n')

    end_time = time.time()
    end_memory = process.memory_info().rss

    print(f"Execution time: {end_time - start_time} seconds")
    print(f"Memory usage: {(end_memory - start_memory) / 10**6} MB")

if __name__ == "__main__":
    main()