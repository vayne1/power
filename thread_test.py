# wang
import threading,time
class Mythread(threading.Thread):
    def __init__(self,n):
        super(Mythread,self).__init__()
        self.n = n
    def run(self):
        print('{} test'.format(self.n),threading.current_thread())
        time.sleep(3)
res = []
start_time = time.time()
for i in range(10):
    t = Mythread(i)
#    t.setDaemon(True)
    t.start()
    res.append(t)
#for r in res:
#    r.join()
print('cost:',time.time()-start_time,threading.active_count(),threading.current_thread())
