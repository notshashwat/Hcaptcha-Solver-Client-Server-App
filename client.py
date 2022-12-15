import socket
import cv2
import os
import numpy as np
import pickle

def chunked(size, source):
    for i in range(0, len(source), size):
        yield source[i:i+size]


HOST = "127.0.0.1"
PORT = 8889


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect((HOST,PORT))

## Reading the image :


def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

DIR_PATH = './imgs'

#get the newest image in the folder imgs
img_path = newest(DIR_PATH)


image = cv2.imread(img_path)
image = cv2.resize(image,(32,32))

test = []
test.append(image)
test = np.array(test)
test = test/255
#print(test)
pkl = pickle.dumps(test)
chunked_data = list(chunked(1024, pkl))
print("Number of 1024 bytes packets to be transfered: ",len(chunked_data))
client.send(str(len(chunked_data)).encode())
for i in chunked_data:
    client.send(i)
print("The image is of : ", client.recv(1024).decode())

client.close()
