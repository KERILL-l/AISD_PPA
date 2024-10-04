def encode_string(s):
    n = len(s)
    dp = [["" for _ in range(n)] for _ in range(n)]

    for l in range(n):
        for i in range(n - l):
            j = i + l
            substr = s[i:j + 1]
            dp[i][j] = substr

            if j - i < 4:
                continue

            for k in range(i, j):
                if len(dp[i][j]) > len(dp[i][k] + '+' + dp[k + 1][j]):
                    dp[i][j] = dp[i][k] + '+' + dp[k + 1][j]

            for k in range(1, len(substr)):
                repeat_str = substr[:k]
                if repeat_str and len(substr) % len(repeat_str) == 0 and substr == repeat_str * (len(substr) // len(repeat_str)):
                    encoded = f"{dp[i][i + k - 1]}*{len(substr) // len(repeat_str)}"
                    if len(encoded) < len(dp[i][j]):
                        dp[i][j] = encoded

    return dp[0][n - 1]

def main():
    with open('input.txt', 'r') as file:
        s = file.readline().strip()

    result = encode_string(s)

    with open('output.txt', 'w') as file:
        file.write(result + '\n')

if __name__ == "__main__":
    import time
    import tracemalloc

    start_time = time.time()
    tracemalloc.start()

    main()

    current, peak = tracemalloc.get_traced_memory()
    print(f"Время выполнения: {time.time() - start_time:.10f} секунд")
    print(f"Использование памяти: {current / 10**6:.6f} MB; Пиковое использование памяти: {peak / 10**6:.6f} MB")

    tracemalloc.stop()
