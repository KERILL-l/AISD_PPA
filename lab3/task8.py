import timeit
import psutil
import heapq

def solve_task():
    # Чтение входных данных
    with open('input.txt', 'r') as file:
        n, m = map(int, file.readline().split())
        
        # Создание графа
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, w = map(int, file.readline().split())
            graph[a].append((b, w))
        
        # Чтение начальной и конечной вершин
        u, v = map(int, file.readline().split())
    
    # Поиск кратчайшего пути с помощью алгоритма Дейкстры
    def dijkstra(start, end):
        distances = [float('inf')] * (n + 1)
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances[end] if distances[end] != float('inf') else -1
    
    # Нахождение кратчайшего пути
    result = dijkstra(u, v)
    
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
