import socketio
import time

##################
#   CLIENT
##################

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('message', {'response': 'client message'})

@sio.on('message')
def get_message(data):
    print(f"someone said : ",data)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')
# for i in range(1000):
#     print(f"{i}\t: ")
#     my_message("hello")
#     time.sleep(1)
sio.wait()