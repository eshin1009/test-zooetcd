import etcd
import sys

op_repeat = 10
leaderIp = '172.31.40.149'

client = etcd.Client(host=leaderIp, port=4001, protocol='http') # on port 4001
writeratio = int(client.read('/writeratio').value)

maxidx = writeratio*op_repeat
readratio = 100-writeratio

while True:
    for x in range(writeratio*op_repeat):
        print "Writing [{0}] to /n{1}".format(str(x),str(x))
        client.write('/n' + str(x), str(x))
    for x in range(readratio*op_repeat):
        nodeId = x % maxidx
        print "Reading /n" + str(nodeId)
        client.read('/n' + str(nodeId))
