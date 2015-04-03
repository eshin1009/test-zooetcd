#zookeeper client

import os
import datetime
import zkclient
from libZookeeperTest import init, createNodes, deleteNodes, childPath, ZookeeperClient
from libTest import initTest, doLoop

def readTest(clusterNum, leaderIp, writeratio):
    (servers, options) = init() #ESTELLE: servers being ignored
    client = ZookeeperClient(leaderIp + ':2181', options.timeout) # servers not being used
    #client = ZookeeperClient(servers[0] + ':2181', options.timeout) # on port 4001
    #writeratio = int(client.read('/writeratio')[0])

    initTest('read', writeratio, clusterNum)

    # create nodes
    createNodes(client)

    doLoop(client)

    #deleteNodes(client)

# delete notes
def cleanUp(leaderIp): #ESTELLE: is it OK?
    (servers, options) = init()
    client = ZookeeperClient(leaderIp + ':2181', options.timeout) # on port 4001
    deleteNodes(client)
