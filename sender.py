import numpy as np
import pyaudio
import zmq
# from PyQt4 import QtCore, QtGui

FS = 11025  # Hz
CHUNKSZ = 256  # samples


class MicrophoneRecorder():

    def __init__(self, sender):
        self.sender = sender
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=FS,
                                  input=True,
                                  frames_per_buffer=CHUNKSZ)

    def read(self):
        data = self.stream.read(CHUNKSZ)
        self.sender.send(data)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


class Sender():

    def __init__(self):
        self.context = zmq.Context()

        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("tcp://127.0.0.1:5557")

    def send(self, buf):
        topic = 0
        ret = self.socket.send("%d %s" % (topic, buf), zmq.NOBLOCK)


if __name__ == '__main__':
    # app = QtGui.QApplication([])
    sender = Sender()

    mic = MicrophoneRecorder(sender)

    while True:
        mic.read()

    app.exec_()
    mic.close()