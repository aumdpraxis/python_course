from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Pipe
from multiprocessing import Pool
# from multiprocessing import Value, Array, Manager # para memoria compartida, se usan como los valores normales(int, float, list, dict,...)
from random import randint
from random import randrange
from random import random
from random import shuffle
import time


def get_matrix(dims):
    return [ [randint(1,4) for col in range(dims[1]) ] for row in range(dims[0]) ]

def _sum(numbers):
    temp_var = 0
    for num in numbers:
        temp_var+= num
    return temp_var

def print_name(name):
    print(f"--------{name} starting--------")
    time.sleep(randint(0,3)) 
    print(f"mi name is {name}!, good to see ya!\t{time.ctime()}")

def print_name_1(name,_Q:Queue):
    print(f"--------{name} starting--------")
    string=",_a ,_b ,_c ,_d ,_e ,_f"
    temp_strs= string.split(',')
    temp_strs= name.join(temp_strs)
    temp_strs= temp_strs.split(' ')
    for item in temp_strs:
        _Q.put(item)
        time.sleep(random()*2)
        print(f"##-LOG-##\t<{name}>\t reporting: {_Q.get()}")
    time.sleep(randint(0,3)) 
    print(f"mi name is {name}!, good to see ya!\t{time.ctime()}")

def greet_process(_name,_listener,_greeter):
    print(f"--------{_name} starting--------")
    _greeter.send(f"Hello, im {_name}")
    time.sleep(random()*2)
    _message= _listener.recv()
    print(f"<{_name}>\t: someone said me '{_message}'")


def proc():
    mat = get_matrix((4,4))
    for row in mat:
        print(row)
    p = Pool(1)
    print(p.map(_sum, mat ))

def proc_1():
    processes= []
    thread_names= ['alpha','beta','gamma','etha','iota']
    for item in thread_names:
        temp_p = Process( target=print_name, args=(item,) )
        temp_p.start()
        processes.append(temp_p)
    for p in processes:
        p.join()

def proc_2():
    global q
    processes= []
    thread_names= ['alpha','beta','gamma','etha','iota','ro','sigma','pi','theta']
    q= Queue()
    for item in thread_names:
        temp_p = Process( target=print_name_1, args=(item,q) )
        temp_p.start()
        processes.append(temp_p)
    for p in processes:
        p.join()

def proc_3():
    global _listeners
    global _greeters
    _listeners= []
    _greeters= []
    thread_names= ['alpha','beta','gamma','etha','iota','ro','sigma','pi','theta']
    for name in thread_names:
        temp_listener, temp_greeter= Pipe()
        _listeners.append(temp_listener)
        _greeters.append(temp_greeter)
    
    shuffle(_listeners)
    shuffle(_greeters)
    processes= []
    for index,item in enumerate(thread_names):
        temp_p = Process( target=greet_process , args=(item,_listeners[index], _greeters[index] ) )
        temp_p.start()
        processes.append(temp_p)
    for p in processes:
        p.join()

## IMPORTANT ( main )
if __name__ == "__main__":
    proc_3()