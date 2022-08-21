import threading
import time
import queue



# class Queue():
#     def __init__(self) -> None:
#         self.items = []
#         self.lock = threading.Lock()#prevent the thread from exiting until all the threads are done
#         self.empty_lock=threading.Lock()#prevent the thread from exiting until all the threads are done
#     def push(self,number):
#         self.lock.acquire()#lock the thread until the thread is done
#         self.items.append(number)
#         self.lock.release()#release the lock when the thread is done

#     def b_pop(self):
#         self.lock.acquire()
#         while self.items == []:
#             self.empty_lock.acquire()

            
#         else:
#             self.pop()
#             self.empty_lock.release()
#             self.lock.release()
        

#     def pop(self):
#         self.lock.acquire()#lock the thread until the thread is done
#         if len(self.items) == 0:
#             return self.b_pop()
#         else:
#             x=self.items[0]
#             self.items.pop(0)
#             self.lock.release()
#             return x
  
#     def peek(self):
#         self.lock.acquire()
#         if len(self.items) == 0:
#             return self.lock.release()
#         else:
#             item=self.items[0]
#             self.lock.release()
#             return item
            
#     def __len__(self):
#         return len(self.items)


