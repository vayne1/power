import socket
client = socket.socket()
client.connect(('localhost', 6969))
aa = client.recv(1024)
print(aa.decode())
while True:
        msg = input('>>>:').strip()
        if len(msg) == 0:continue
        if msg == 'exit':exit()
        client.send(msg.encode('utf-8'))
        all_size=client.recv(1024)
        print(all_size)
        date=b''
        date_size = 0
        while date_size < int(all_size):
                d = client.recv(1024)
                date_size += len(d)
                date += d
                print (date_size)
        print(date.decode())
client.close()