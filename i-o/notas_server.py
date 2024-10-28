import socket

SOCK_BUFFER = 1024


def extrae_data(data_cruda: bytes) -> list[int]:
    datos_str = data_cruda.decode("utf-8")
    datos_lista_str = datos_str.split(",")
    datos_lista = [int(elemento) if elemento.isnumeric() else -1 for elemento in datos_lista_str]

    return datos_lista


def valida_datos(data_procesada: list[int]) -> bool:
    if len(data_procesada) != 15:
        return False
    
    if -1 in data_procesada:
        return False
    
    return True


def calcula_nota(data_procesada: list[int]) -> float:
    notas_lab = data_procesada[1:13]
    e1 = data_procesada[13]
    e2 = data_procesada[14]

    nota_lab = sum(notas_lab) / len(notas_lab)
    nota_final = ((5 * nota_lab) + (2.5 * e1) + (2.5 * e2)) / 10

    return nota_final

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000)

    print(f"Iniciando el servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()

        print(f"Conexion desde {client_address[0]}:{client_address[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER)

                if data:
                    datos = extrae_data(data)
                    if not valida_datos(datos):
                        conn.sendall("Datos enviados no corresponden al formato o longitud requerida".encode("utf-8"))
                    nota_final = calcula_nota(datos)
                    conn.sendall(f"{nota_final}".encode("utf-8"))
                else:
                    print("No hay mas datos")
                    break
        except ConnectionResetError:
            print("El cliente cerro la conexion de manera abrupta")
        finally:
            print("Cerrando la conexion")
            conn.close()

