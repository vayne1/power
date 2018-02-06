# wang
import paramiko
transport = paramiko.Transport(('47.93.203.159', 22))
transport.connect(username='root', password='wang520522@')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('ls')
res = stdout.read()
print(res.decode())
transport.close()