def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    result = []

    for i in range(t_len - p_len + 1):
        t_sub_hash = hash(text[i:i + p_len])
        if p_hash == t_sub_hash and text[i:i + p_len] == pattern:
            result.append(i + 1)  # Нумерация с 1

    return result

def main():
    with open('input.txt', 'r') as file:
        pattern = file.readline().strip()
        text = file.readline().strip()

    positions = rabin_karp(pattern, text)
    count = len(positions)

    with open('output.txt', 'w') as file:
        file.write(f"{count}\n")
        file.write(" ".join(map(str, positions)) + "\n")

if __name__ == "__main__":
    import time
    import tracemalloc

    start_time = time.time()
    tracemalloc.start()

    main()

    current, peak = tracemalloc.get_traced_memory()
    print(f"Время выполнения: {time.time() - start_time} секунд")
    print(f"Использование памяти: {current / 10**6} MB; Пиковое использование памяти: {peak / 10**6} MB")

    tracemalloc.stop()
