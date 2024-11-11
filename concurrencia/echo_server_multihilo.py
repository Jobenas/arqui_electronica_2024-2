import socket
from threading import Thread

SOCK_BUFFER = 1024


def client_handler(conn, client_address):
    print(f"Conexion desde {client_address[0]}:{client_address[1]}")

    try:
        while True:
            data = conn.recv(SOCK_BUFFER)

            if data:
                print(f"Recibi: {data}")
                conn.sendall(data)
            else:
                print("No hay mas datos")
                break
    except ConnectionResetError:
        print("El cliente cerro la conexion de manera abrupta")
    finally:
        print("Cerrando la conexion")
        conn.close()


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000)

    print(f"Iniciando el servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        c_conn, c_address = sock.accept()

        t = Thread(target=client_handler, args=(c_conn, c_address))
        t.start()
