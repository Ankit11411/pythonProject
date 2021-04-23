import threading
import time
from module import *


l=threading.Lock()

t1=threading.Thread(target=lambda: [extfile.lock(l)],)
t2=threading.Thread(target=lambda: [extfile.lock(l)],)
t1.start()
t2.start()
t1.join()
t2.join()