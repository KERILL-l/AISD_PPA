import sys
import timeit
import tracemalloc

def solve():
    tracemalloc.start()

    with open('input.txt', 'r') as f:
        nv, ne = map(int, f.readline().strip().split())
        assert 2 <= nv <= 300
        assert 1 <= ne <= 100000

        INF = 1000 * 1000 * 1000
        d = [[INF] * nv for _ in range(nv)]
        
        for i in range(nv):
            d[i][i] = 0
        
        for _ in range(ne):
            v1, v2 = map(int, f.readline().strip().split())
            v1 -= 1
            v2 -= 1
            d[v1][v2] = 0
            d[v2][v1] = min(d[v2][v1], 1)
        
        # Алгоритм Флойда-Уоршелла
        for k in range(nv):
            for i in range(nv):
                for j in range(nv):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        
        max_k = 0
        for i in range(nv):
            for j in range(nv):
                if i != j:
                    max_k = max(max_k, d[i][j])
        
        with open('output.txt', 'w') as f:
            f.write(str(max_k) + '\n')

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Использование памяти: {current / 10**6:.2f} MB (текущая), {peak / 10**6:.2f} MB (пиковая)")

if __name__ == "__main__":
    execution_time = timeit.timeit("solve()", setup="from __main__ import solve", number=1)
    print(f"Время выполнения: {execution_time:.6f} секунд")