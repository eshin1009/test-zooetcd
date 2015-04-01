from optparse import OptionParser
import zkclient
from zkclient import zookeeper

import os
import socket

rootpath = '/nodes'

ip = socket.gethostbyname(socket.gethostname())
clientId = (ip.split('.'))[-1]

def init():
  servers_file = 'servers.txt'
  usage = "usage: %prog [options]"
  parser = OptionParser(usage=usage)
  parser.add_option("", "--servers", dest="servers_file",
                    default="servers.txt", help="comma separated list of host:port (default %default)")
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
  servers = readServers(servers_file)
  return (servers, options)


def childPath(i):
    return rootpath + '/n' + clientId + '_' + str(i)

def readServers(fname):
    lines = [line.strip() for line in open(fname)]
    return map(lambda x : x.split(' ')[0], lines)


def createNodes(client, maxidx):
  if not client.exists(rootpath):
    client.create(rootpath)
  for i in range(maxidx):
    if not client.exists(childPath(i)):
      client.create(childPath(i))

def deleteNodes(client, maxidx):
  for i in range(maxidx):
    client.delete(childPath(i))
  client.delete(rootpath)

