# Python Audio Streaming Server

Can be run alongside a video stream to get an Audio+Video version. 
https://github.com/almondboi/python-live-stream-zeromq

## Installation
```
pip install -r requirements.txt
```

## Dependencies

This project depends on the follwing modules:

pyaudio
numpy
zmq

## Usage

To run: 

1. Launch the server to record and publish the audio stream:

```
python3 mic_server.py
```
2. Launch the client to listen to subscribe and listen to the audio stream being published by the server

```
python3 mic_client.py
```

## Notes

Change the Network IP to the one you want to listen to under

```
recv.py
```
