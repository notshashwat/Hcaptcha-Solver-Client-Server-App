import pickle
import numpy as np
import tensorflow as tf
import socket
def onehotarr_to_labelarr(onehotarr):
  #expects numpy array
  truelabels=[]
  for i in onehotarr:
    truelabels.append(reverselabel(i))
  return truelabels
labels = ['airplane', 'bicycle', 'boat', 'motorbus', 'motorcycle', 'seaplane', 'truck']
def reverselabel(v):
  return labels[np.argmax(v)]


HOST = "127.0.0.1"
PORT = 8889


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print("[LISTENING]")
server.listen()
conn , addr = server.accept()
whole = []
i=1
num = int(conn.recv(1024).decode())
while num:
    num-=1
    data = conn.recv(1024)
    if data == b"":
        break
    print(i,"chunks recieved!")
    i+=1
    whole.append(data)
    
pkl = b"".join(whole)
test = pickle.loads(pkl)


X_t = tf.constant(test)
my_model = tf.keras.models.load_model("model.h5")

final_pred = my_model.predict(X_t)
print(final_pred)
final_label_pred = []
for soft in final_pred:
  final_label_pred.append(labels[np.argmax(soft)])

ans= final_label_pred[0]
print("Sending the answer to client: ",ans)
conn.send(ans.encode())