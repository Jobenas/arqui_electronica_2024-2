import time

def potencia(n: int) -> int:
    pot = 1

    for _ in range(n):
        pot = pot * n

    return pot


if __name__ == '__main__':
    inicio = time.perf_counter()
    res = potencia(200_000)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo de ejecucion sincrono: {t_ejecucion:0.5f} segundos")