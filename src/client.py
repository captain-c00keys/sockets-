import socket
import datetime

# import pdb;pdb.set_trace()
socket.getaddrinfo('127.0.0.1', 3000)
get_info = socket.getaddrinfo('127.0.0.1', 3000)

stream_info = [i for i in get_info if i[1] == socket.SOCK_STREAM][0]
client = socket.socket(*stream_info[:3])
client.connect(stream_info[-1])


# start_message = '--- Starting server on port 3000 at {} ---'.format(datetime.datetime.now().strftime(''))
message = 'Welcome to the Client'
client.sendall(message.encode('utf8'))
buffer_length = 8
message_complete = False

while not message_complete:
    part = client.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break

client.close()
