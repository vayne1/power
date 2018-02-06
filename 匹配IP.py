# wang
import re
with open('ip1.lst','r') as f:
    for i in f:
        a = re.findall(r'\d+.\d+.\d+.\d+',i)
        b=set(a)
        for i in b:
            with open('result.txt','a+') as f:
                f.write(i+'\n')
