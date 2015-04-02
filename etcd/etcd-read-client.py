import etcd
import sys
from libTest import initTest doLoop

op_repeat = 10
leaderIp = '172.31.40.149'

client = etcd.Client(host=leaderIp, port=4001, protocol='http') # on port 4001
writeratio = int(client.read('/writeratio').value)

initTest('read', writeratio)

doLoop(client)
