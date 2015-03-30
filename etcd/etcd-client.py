import etcd
import socket
import sys

maxidx = 100
leaderIp = '172.31.40.147'

writeratio = client.read('/writeratio')
readratio = 100-writeratio
ip = socket.gethostbyname(socket.gethostname())
clientId = (ip.split('.'))[-1]

idx = 1
client = etcd.Client(host=leaderIp, protocol='https') # on port 4001
while True:
    for x in range(idx*writeratio):
        client.write('/nodes/n' + clientId + '_' + str(x), x)
    max_written_idx = idx*writeratio
    widx = 0
    for x in range(idx*readratio):
        client.read('/nodes/n' + clientId + '_' + str(widx))
        widx = widx + 1
        if widx == max_written_idx:
            widx = 0
    idx = idx + 1
    if idx > maxidx:
        idx = 1

