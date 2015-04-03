#zookeeper client

import os
import datetime
import zkclient
from libZookeeperTest import init, createNodes, deleteNodes, childPath, ZookeeperClient
from libTest import initTest, doLoop

def writeTest(clusterNum, leaderIp, writeratio):
    (servers, options) = init()
    client = ZookeeperClient(leaderIp + ':2181', options.timeout) # on port 4001
    # client = ZookeeperClient(servers[0] + ':2181', options.timeout) # on port 4001
    # writeratio = int(client.read('/writeratio')[0])

    initTest('write', writeratio, clusterNum)

    # create nodes
    createNodes(client)

    doLoop(client)
    # delete notes

    #deleteNodes(client)

