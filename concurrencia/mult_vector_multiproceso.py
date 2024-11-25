from itertools import repeat
from multiprocessing import cpu_count, Pool
import numpy as np
import time

M = 5000
N = 5000

num_proc = cpu_count()


def mult_vector(x: list[np.int32], y: list[np.int32]) -> np.int32:
    suma = 0

    for i in range(len(x)):
        suma += x[i] * y[i]

    return suma


if __name__ == '__main__':
    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N, ))

    args = zip(mat_M, repeat(vector_A))

    inicio = time.perf_counter()
    with Pool(processes=num_proc) as p:
        resultado = p.starmap(mult_vector, args)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    print(f"Tiempo total de procesamiento usando pool de {num_proc}: {t_ejecucion:0.5f} segundos")
