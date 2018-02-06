# wang
import paramiko

transport = paramiko.Transport(('47.93.203.159', 22))
transport.connect(username='root', password='wang520522@')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('server.py','/tmp/server.py')
# 将remove_path 下载到本地 local_path
sftp.get('aws_ip.sh', 'local_path')

transport.close()