# wang
from urllib import request
import gevent,time
from gevent import monkey
monkey.patch_all()
def f(url):
    print('GET:{}'.format(url))
    res = request.urlopen(url)
    date = res.read()
    print(len(date),url)
sync_time = time.time()
f('https://www.python.org/')
#f('https://www.yahoo.com/')
f('https://github.com/')
print(time.time()-sync_time)

rsync_time = time.time()
gevent.joinall([
    gevent.spawn(f,'https://www.python.org/'),
#    gevent.spawn(f,'https://www.yahoo.com/'),
    gevent.spawn(f,'https://github.com/')
])
print(time.time()-rsync_time)