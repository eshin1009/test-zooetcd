#zookeeper client

import os
import datetime
import zkclient
from libZookeeperTest import init, createNodes, deleteNodes, childPath, ZookeeperClient
from libTest import initTest, doLoop
import random

def readTest(clusterNum, leaderIp, writeratio):
    random.seed()  # use system time by default
    (servers, options) = init(clusterNum)
    sid = random.randint(0, clusterNum-1)
    client = ZookeeperClient(servers[sid] + ':2181', options.timeout) # on port 4001

    initTest('read', writeratio, clusterNum)

    # create nodes
    # createNodes(client)

    doLoop(client)

def startUp(clusterNum):
    (servers, options) = init(clusterNum)
    client = ZookeeperClient(servers[0] + ':2181', options.timeout)
    createNodes(client)    

# delete notes
def cleanUp(clusterNum, leaderIp):
    (servers, options) = init(clusterNum)
    client = ZookeeperClient(servers[0] + ':2181', options.timeout) # on port 4001
    deleteNodes(client)
