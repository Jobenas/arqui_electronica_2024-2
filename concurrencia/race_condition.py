import time
from concurrent.futures import ThreadPoolExecutor


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name: str):
        print(f"Thread {name} iniciando actualizacion")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print(f"Thread {name} finalizando actualizacion")


if __name__ == '__main__':
    workers = 2
    tasks = workers

    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        for i in range(tasks):
            executor.submit(db.update, i)

    print(f"Valor final de la base de datos: {db.value}")
