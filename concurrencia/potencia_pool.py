from multiprocessing import Pool
import time

N = 200_000
num_proc = 16
num_tareas = 256


def potencia(exponente: int, base: int = N) -> int:
    pot = 1

    for _ in range(exponente):
        pot = pot * base

    return pot


if __name__ == '__main__':
    args = [N // num_tareas] * num_tareas

    inicio = time.perf_counter()
    p = Pool(processes=num_proc)
    res = p.map(potencia, args)
    p.close()
    p.join()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    print(f"Tiempo de ejecucion en pool de {num_proc} workers para {num_tareas} tareas: {t_ejecucion:0.5f} segundos")
