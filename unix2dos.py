# wang
import re
with open('biji.txt','rb') as f:
    aa = f.read()
    bb = re.sub(b'\\n',b'\\r\\n',aa)
    print(bb)
with open('biji_new.txt','wb') as f:
    f.write(bb)