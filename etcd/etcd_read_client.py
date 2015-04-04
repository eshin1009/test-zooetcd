import etcd
import sys
from libTest import initTest, doLoop

def readTest(clusterNum, leaderIp, writeratio):
    client = etcd.Client(host=leaderIp, port=4001, protocol='http') # on port 4001
    initTest('read', writeratio, clusterNum)
    doLoop(client, True)
    endTest(client, True)
