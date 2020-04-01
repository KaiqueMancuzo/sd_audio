import numpy as np
import zmq

context = zmq.Context()
sock = context.socket(zmq.SUB)

print ("connect")
sock.setsockopt(zmq.SUBSCRIBE, '7578128')
sock.connect("tcp://127.0.0.1:5557")

while True:
    envelope = sock.recv()
    data = sock.recv()
    y = np.fromstring(data, dtype=np.float32)
    print ("y")