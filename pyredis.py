# Author: Rahul Mahanot

from redis._compat import xrange
from rediscluster import RedisCluster
import time
from random import random, randint

## connect to the redis cluster
startup_nodes = [{"host": "127.0.0.1", "port": 9100}]
r = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
print("Connected to Redis Cluster")



class Transact():
    def __init__(self):
        print(r.info())
        print('Running...')
        self.random_commands_start()
    
    def random_commands_start(self):
        self.random_key = str(randint(0, 1000000))
        r.set(self.random_key, self.random_key)
        while True:
            try:
                self.number = randint(0, 10)
                self.random_key = str(randint(0, 1000000))
                if self.number % 5 == 0:
                    self.set_key()
                elif (self.number - 1) % 5 == 0:
                    self.get_key()
                elif (self.number - 2) % 5 == 0:
                    self.expire_key()
                # Flush not needed now so commented out
                # elif self.number == 9:
                #     self.flush_keys()
                else:
                    self.do_nothing()
            except:
                pass


    def set_key(self):
        r.set(self.random_key, self.random_key)
        r.incrby(self.random_key, self.number)

    
    def get_key(self):
        r.get(self.random_key)
        # r.randomkey()
    
    def expire_key(self):
        try:
            r.expire(self.random_key, '30')
        except Exception as e:
            print(e)

    def flush_keys(self):
        r.flushall()
    
    def do_nothing(self):
        time.sleep(0.001)


transact = Transact()