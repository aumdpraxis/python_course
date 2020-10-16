from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from game_obj import snake,apple
import uuid
from random import randint, choice
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

CURRENT_TIME= 0
APPLES={}
SCENARIO_DIMS=[0,0]
GRID_SIZE= 0
PLAYERS={}
COLORS=[]

current_milli_time = lambda: int(round(time.time() * 1000))

###
### 
### INIT FUNCTION
def begin():
    global CURRENT_TIME
    global APPLES
    global SCENARIO_DIMS
    global GRID_SIZE
    global PLAYERS
    global APPLES
    global COLORS
    CURRENT_TIME= current_milli_time()
    SCENARIO_DIMS=[800,600]
    GRID_SIZE= 8
    PLAYERS={}
    APPLES={}
    COLORS=[
        '#a35626', # naranja obscuro
        '#f0620a', # naranja claro 
        '#f0c60a', # amarillo claro 
        '#a38c24', # amarillo obscuro
        '#779922', # verde lima obscuro
        '#9de60b', # verde lima claro
        '#0ceb0f', # verde hoja claro
        '#29992b', # verde hoja obscuro
        '#299968', # turquesa obscuro
        '#09eb89', # turquesa claro
        '#09ebe3', # cyan claro
        '#239490', # cyan obscuro
        '#236994', # azul obscuro
        '#0995eb', # azul claro
        '#092beb', # zafiro claro
        '#2b3b94', # zafiro obscuro
        '#422b94', # morado obscuro
        '#6109ed', # morado claro
        '#9609ed', # magenta claro
        '#5f2682', # magenta obscuro
        '#832885', # lila obscuro
        '#e609eb', # lila claro
        '#eb09b3', # rosa claro
        '#8c2974'  # rosa obscuro
    ]
    temp_id_apple= str(uuid.uuid1())
    temp_pos_apple= get_random_pos()
    APPLES={}
    APPLES[temp_id_apple]=apple(temp_id_apple,temp_pos_apple[0],temp_pos_apple[1])

###
### UTILITIES 
###
def get_random_pos():
    return [
        randint(0,int(SCENARIO_DIMS[0]/GRID_SIZE))*GRID_SIZE,
        randint(0,int(SCENARIO_DIMS[1]/GRID_SIZE))*GRID_SIZE
    ]
###
### MAIN PAGE SERVER
###
@app.route('/')
def home():
    return render_template('index.html')

###
### SOCKET FUNCTIONS
###
@socketio.on('get_player')
def get_new_player(data):
    global PLAYERS
    global APPLES
    if(len(APPLES)<1 or int(len(APPLES)/2)<len(PLAYERS)):
        temp_id_apple= str(uuid.uuid1())
        temp_pos_apple= get_random_pos()
        APPLES={}
        APPLES[temp_id_apple]=apple(temp_id_apple,temp_pos_apple[0],temp_pos_apple[1])
    temp_pos = get_random_pos()
    temp_id= str(uuid.uuid1())
    PLAYERS[temp_id]= snake(temp_pos[0],temp_pos[1],GRID_SIZE,SCENARIO_DIMS,choice(COLORS))
    emit('set_player',{'player':temp_id})

@socketio.on('delete_player')
def delete_player(data):
    global PLAYERS
    global APPLES
    PLAYERS.pop(data['sender'])
    if(len(APPLES)>1):
        APPLES.popitem()
    try:
        del PLAYERS[data['sender']]
    except:
        print("item had been deleted")
    socketio.emit('player_left',{'player':data['sender']})

@socketio.on('update_environment')
def update_environment(data):
    global PLAYERS
    global CURRENT_TIME
    temp_time = current_milli_time()
    kill_list=[]

    ### SYNCRONIZED UPDATES ON EVERY CLIENT
    if((temp_time-CURRENT_TIME)>40):
        ### GET CURRENT POSITION OF EVERY SNAKE BODY
        owned_indicator={}
        for _id,player in PLAYERS.items():
            for cell in player.get_current_pos():
                owned_indicator[(cell['x'],cell['y'])]=_id

        ### CHACK IF NEXT STAPE GENERATE COLITION
        final_keys= owned_indicator.keys()
        for _id,player in PLAYERS.items():
            next_state= player.get_next_state()
            if((next_state[0],next_state[1]) in final_keys):
                kill_list.append(_id)
                continue

        ### UPDATE BODY IF A COLITION IS NOT GENERATED, ELSE RESET SNAKE
        for _id,player in PLAYERS.items():
            if(_id not in kill_list):
                next_state= player.get_next_state()
                player.update_pos(next_state)
            else:
                temp_pos = get_random_pos()
                PLAYERS[_id]= snake(temp_pos[0],temp_pos[1],GRID_SIZE,SCENARIO_DIMS,PLAYERS[_id].color)
        CURRENT_TIME=temp_time
    
    ### PREPARE DATA TO SEND TO CLIENT
    temp_state_players = []
    for _id,player in PLAYERS.items():
        temp_state_players.append(player.get_metadata())

    temp_state_apples = []
    for _id,apple in APPLES.items():
        temp_state_apples.append(apple.get_metadata())

    ### SEND
    emit('update',{'players':temp_state_players,'apples':temp_state_apples})

@socketio.on('ate_apple')
def new_apple(data):
    global PLAYERS
    global APPLES
    try:
        ### GET A NEW POSITION FOR THE APPLE
        APPLES.pop(data['apple'])
        temp_id_apple= str(uuid.uuid1())
        temp_pos_apple= get_random_pos()
        APPLES={}
        APPLES[temp_id_apple]=apple(temp_id_apple,temp_pos_apple[0],temp_pos_apple[1])

        ### INCREASE SNAKE SIZE
        PLAYERS[data['sender']].ate_apple()
    except:
        pass

@socketio.on('key_press')
def key_press(data):
    if(data['key']=='l'):
        PLAYERS[data['sender']].on_left_key()
    if(data['key']=='u'):
        PLAYERS[data['sender']].on_up_key()
    if(data['key']=='r'):
        PLAYERS[data['sender']].on_right_key()
    if(data['key']=='d'):
        PLAYERS[data['sender']].on_down_key()

###
### MAIN FUNCTION
### 
if __name__ == '__main__':
    begin()
    socketio.run(app,port=5400)