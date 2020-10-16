import gevent
from random import randint
import time

def print_name(name):
    print(f"--------{name} starting--------")
    gevent.sleep(randint(0,3)) 
    print(f"mi name is {name}!, good to see ya!\t{time.ctime()}")


def proc():
    thread_names= ['alpha','beta','gamma','etha','iota']
    processes= [ gevent.spawn(print_name,_name) for _name in thread_names ]
    gevent.joinall(processes)

if __name__ == "__main__":
    proc()