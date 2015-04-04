import etcd
import sys
from libTest import initTest, doLoop, endTest

def writeTest(clusterNum, leaderIp, writeratio):
    client = etcd.Client(host=leaderIp, port=4001, protocol='http') # on port 4001
    initTest('write', writeratio, clusterNum)
    doLoop(client, True)
    endTest(client, True)

