import threading

def numbers():
    for i in range(1, 100):
        print(i)


for i in range (10000):
    t=threading.Thread(target=numbers).start()
   
    
    
    