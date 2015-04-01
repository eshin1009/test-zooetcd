import etcd
import sys

maxidx = 100
leaderIp = '172.31.40.149'

client = etcd.Client(host=leaderIp, port=4001, protocol='http') # on port 4001
writeratio = int(client.read('/writeratio').value)

readratio = 100-writeratio
op_repeat = 10

while True:
    for x in range(writeratio*op_repeat):
        nodeId = x % maxidx
        print "Writing [{0}] to /n{1}".format(str(x),str(nodeId))
        client.write('/n' + str(nodeId), str(x))
    for x in range(readratio*op_repeat):
        print "Reading /n" + str(nodeId)
        nodeId = x % maxidx
        client.read('/n' + str(nodeId))
