import scipy.signal
import numpy as np
import cv2
from queue import Queue
import threading

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

def thread1(paths,queue):

    i=0
    

    # Reading the image.
    for path in paths:
        img=cv2.imread(path)
        img_gray = rgb2gray(img)
        i+=1
        queue.put(img_gray)


def thread2(queue):
    i=1
    while queue.empty()==False:
        i+=1
        kernel_size = 10
        kernel = ((1 / (kernel_size ** 2)) * np.ones(kernel_size ** 2))
        kernel = kernel.reshape(kernel_size, kernel_size)
        img = queue.get()
        

        output = scipy.signal.convolve2d(img, kernel)
        cv2.imwrite(f'output_{i}.png', output)
        


        






q1 = Queue()

# q1.put(output)
thread1(['domestic-dog_thumb_4x3.jpeg'] ,q1)
thread2(q1)

t1=threading.Thread(target=thread1,args=['domestic-dog_thumb_4x3.jpeg',q1])
t1.start()
t2=threading.Thread(target=thread2,args=[q1])
t2.start()











