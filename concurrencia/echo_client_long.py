import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 5000)
    print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    for i in range(20):
        msg = f"Mensaje: {i + 1}"
        sock.sendall(msg.encode('utf-8'))
        data = sock.recv(SOCK_BUFFER)
        print(f"Recibi: {data}")

        time.sleep(0.5)

    sock.close()
