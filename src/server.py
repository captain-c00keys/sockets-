import socket
from datetime import datetime

PORT = 3000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

address = ('127.0.0.1', PORT)
# sock.listen(1)
sock.bind(address)

try:
    sock.listen(1)
    # sock.bind(address)
    print('--- Starting server on port 3000 at {} ---'.format(datetime.datetime.now().strftime('%c')))

    conn, addr = sock.accept()
    buffer_length = 8

    message_complete = False

    message = b''

    while not message_complete:
        part = conn.recv(buffer_length)
        message += part

        if len(part) < buffer_length:
            break

    message = message.decode('utf8')
    print('{} Echoed: {}'.format(datetime.now().strftime('%H:%M:%S %d-%m-%y'), message))

    conn.send(message.encode('utf8'))


except socket.error as e:
    print(str(e))

# import pdb; pdb.set_trace()


# print('Connected to: '+addr[0]+':'+str(addr[1]))
# print(conn)

# import pdb; pdb.set_trace()

# start_message = '--- Starting server on port 3000 at {} ---'.format(datetime.datetime.now().strftime('%c'))


conn.close()
sock.close()
print('--- Stop server on port 3000 at {} ---'.format(datetime.datetime.now().strftime('%c')))