import psutil
import time

def tree_height(node, nodes):
    if node == 0:
        return 0
    key, left, right = nodes[node - 1]
    left_height = tree_height(left, nodes)
    right_height = tree_height(right, nodes)
    return max(left_height, right_height) + 1

def main():
    start_time = time.time()
    process = psutil.Process()

    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        if n < 0 or n > 2 * 10**5:
            raise ValueError("Количество узлов должно быть в диапазоне от 0 до 200000.")
        
        if n == 0:
            with open('output.txt', 'w') as f_out:
                f_out.write("0")
            return
        
        nodes = []
        for _ in range(n):
            key, left, right = map(int, f.readline().strip().split())
            if not (-10**9 <= key <= 10**9):
                raise ValueError("Ключи должны быть в диапазоне от -10^9 до 10^9.")
            if not (0 <= left <= n) or not (0 <= right <= n):
                raise ValueError("Индексы детей должны быть в диапазоне от 0 до n.")
            nodes.append((key, left, right))
        
        height = tree_height(1, nodes)
        
        with open('output.txt', 'w') as f_out:
            f_out.write(f"{height}\n")

    end_time = time.time()
    memory_info = process.memory_info()

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Использование памяти: {memory_info.rss / (1024 * 1024):.6f} MB")

if __name__ == "__main__":
    main()

