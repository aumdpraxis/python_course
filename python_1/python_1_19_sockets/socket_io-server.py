import eventlet
import socketio

##################
#   SERVER
##################

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.on('message')
def my_message(sid, data):
    sio.emit('message', {'response': 'server message'})
    print('\n-----------\nmessage ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)
    for i in range(10):
        my_message("")
    