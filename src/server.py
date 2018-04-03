import socket
import datetime

def server_setup:

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP)

    address = ('127.0.0.1', 3000)
    sock.listen(1)


try:
    sock.bind(address)
except socket.error as e:
    print(str(e))

import pdb; pdb.set_trace()

buffer_length = 8
conn, addr = sock.accept()

# print('Connected to: '+addr[0]+':'+str(addr[1]))
# print(conn)
message_complete = False
while not message_complete:
    part = conn.recv(buffer_length)
    message += part
    if len(part) < buffer_length:
        break
# import pdb; pdb.set_trace()

start_message = '--- Starting server on port 3000 at {} ---'.format(datetime.datetime.now().strftime('%c'))

conn.send(message.encode('utf8'))

conn.close()
sock.close()
print('--- Stop server on port 3000 at {} ---'.format(datetime.datetime.now().strftime('%c')))