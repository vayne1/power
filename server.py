import os
import socket
server = socket.socket()
server.bind(('localhost',6969))
server.listen(5)
print('deng')
while True:
    conn,addr = server.accept()
    #print(conn,addr)
    print('{} is already connected'.format(addr))
    conn.send(b'Welcome')
    while True:
        date = conn.recv(1024)
        print(date)
        if not date or date.decode() == 'exit':
            print('client has close...')
            break
        res = os.popen(date.decode()).read()
        conn.send(str(len(res.encode())).encode('utf-8'))
        conn.send(res.encode('utf-8'))
server.close()
