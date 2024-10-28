import socket

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 5000)
    print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "hola mundo"
    msg_bytes = msg.encode("utf-8")
    cantidad_esperada = len(msg_bytes)
    cantidad_recibida = 0
    msg_retorno_bytes = b''

    sock.sendall(msg.encode('utf-8'))

    while cantidad_recibida < cantidad_esperada:
        data = sock.recv(SOCK_BUFFER)
        print(f"Recibi: {data}")
        msg_retorno_bytes += data
        cantidad_recibida += len(data)

    sock.close()

    print(f"mensaje completo recibido {msg_retorno_bytes.decode('utf-8')}")
