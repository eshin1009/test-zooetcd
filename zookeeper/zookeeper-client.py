#zookeeper client

import os
from optparse import OptionParser
import zkclient
from zkclient import ZKClient, SequentialCountingWatcher, zookeeper

import socket
import sys

usage = "usage: %prog [options]"
parser = OptionParser(usage=usage)
parser.add_option("", "--servers", dest="servers",
                  default="localhost:2181", help="comma separated list of host:port (default %default)")
parser.add_option("", "--config",
                  dest="configfile", default=None,
                  help="zookeeper configuration file to lookup servers from")
parser.add_option("", "--timeout", dest="timeout", type="int",
                  default=5000, help="session timeout in milliseconds (default %default)")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="verbose output, include more detail")
parser.add_option("-q", "--quiet",
                  action="store_true", dest="quiet", default=False,
                  help="quiet output, basically just success/failure")

(options, args) = parser.parse_args()

zkclient.options = options

zookeeper.set_log_stream(open("log/cli_log_%d.txt" % (os.getpid()),"w"))

leaderIp = 'ec2-54-148-227-205.us-west-2.compute.amazonaws.com'  #'172.31.8.171'

writeratio = 10 # client.read('/writeratio')
readratio = 100-writeratio
ip = socket.gethostbyname(socket.gethostname())
clientId = (ip.split('.'))[-1]

servers = options.servers.split(",")
client = ZKClient(servers[0], options.timeout) # on port 4001

def childPath(i):
    return rootpath + '/n' + clientId + '_' + str(i)

rootpath = '/nodes'
if not client.exists(rootpath):
    client.create(rootpath)

maxidx = 100
for i in range(maxidx):
    if not client.exists(childPath(i)):
        client.create(childPath(i))

while True:
    for x in range(writeratio):
        nodeId = x % maxidx
        client.set(childPath(nodeId), str(x))
    for x in range(readratio):
        nodeId = x % maxidx
        client.get(childPath(nodeId))

for i in range(maxidx):
    client.delete(chlidPath(i))
client.delete(rootpath)

# while True:
#     for x in range(idx*writeratio):
#         client.create(rootpath + '/n' + clientId + '_' + str(x), str(x))
#     max_written_idx = idx*writeratio
#     widx = 0
#     for x in range(idx*readratio):
#         client.get(rootpath + '/n' + clientId + '_' + str(widx))
#         widx = widx + 1
#         if widx == max_written_idx:
#             widx = 0
#     idx = idx + 1
#     if idx > maxidx:
#         idx = 1
