import time

N = 200_000_000


def cuenta(n: int):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    cuenta(N)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo de ejecucion: {t_ejecucion:0.5f} segundos")
