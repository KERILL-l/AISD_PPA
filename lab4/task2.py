import timeit
import tracemalloc

def count_palindromic_triplets(message):
    # Удаляем все пробелы из сообщения
    message = message.replace(" ", "")
    n = len(message)
    count = 0
    
    # Перебираем все возможные комбинации трех букв
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if message[i] == message[k]:
                    count += 1
    
    return count

# Чтение входного файла
with open('input.txt', 'r') as file:
    message = file.readline().strip()

# Начало измерения времени и памяти
tracemalloc.start()
start_time = timeit.default_timer()

# Вычисление количества палиндромных триплетов
result = count_palindromic_triplets(message)

# Окончание измерения времени и памяти
end_time = timeit.default_timer()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Вывод результата в консоль
print(f"{result}")
print(f"Время выполнения: {end_time - start_time:.10f} секунд")
print(f"Использование памяти: {current / 10**6:.6f} MB (текущая), {peak / 10**6:.6f} MB (пиковая)")
