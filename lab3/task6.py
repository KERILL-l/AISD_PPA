import time
import timeit
import psutil
from collections import deque

def solve_task():
    # Чтение входных данных
    with open('input.txt', 'r') as file:
        n, m = map(int, file.readline().split())
        u, v = map(int, file.readline().split())
        
        # Создание графа
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, file.readline().split())
            graph[a].append(b)
            graph[b].append(a)
    
    # Поиск кратчайшего пути с помощью BFS
    def bfs(start, end):
        visited = [False] * (n + 1)
        queue = deque([(start, 0)])
        visited[start] = True
        
        while queue:
            current, depth = queue.popleft()
            if current == end:
                return depth
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, depth + 1))
        return -1
    
    # Нахождение кратчайшего пути
    result = bfs(u, v)
    
    # Запись результата в выходной файл
    with open('output.txt', 'w') as file:
        file.write(str(result) + '\n')

if __name__ == "__main__":
    # Начало отсчета времени
    start_time = timeit.default_timer()
    
    # Выполнение задачи
    solve_task()
    
    # Конец отсчета времени
    end_time = timeit.default_timer()
    
    # Подсчет использованного времени
    elapsed_time = end_time - start_time
    
    # Получение информации о текущем процессе
    process = psutil.Process()
    
    # Подсчет использованной памяти в байтах
    memory_usage = process.memory_info().rss
    
    print(f"Время выполнения: {elapsed_time:.6f} секунд")
    print(f"Использованная память: {memory_usage / (1024 * 1024):.2f} МБ")
