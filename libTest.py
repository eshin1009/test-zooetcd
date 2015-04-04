import os
import datetime
import socket
import time

maxidx = 10

outTS = ""
outTS = ""
readratio = 0
writeratio = 0
rootpath = '/nodes'

mode = ""
doesWrite = False

def initTest(rw, wratio, clusterNum):
  global mode, doesWrite, outTS, outDUR, writeratio, readratio
  mode = rw
  doesWrite = rw == 'write'
  pid = os.getpid()
  outTS = open('log/log-ts-{0}-{1}-{2}-{3}.txt'.format(wratio, clusterNum, rw, pid), 'w')
  outDUR = open('log/log-dur-{0}-{1}-{2}-{3}.txt'.format(wratio, clusterNum, rw, pid), 'w')
  # writeratio = wratio
  # readratio = 100-wratio

def getMaxIdx():
  return maxidx

def childPath(i):
  return  rootpath + '/n' + '_' + str(i)

def doLoop(client):
  while True:
    for nodeId in range(maxidx):
      path = childPath(nodeId)
      #print "{0} {1}".format(mode, path)
      startTime = datetime.datetime.now()
      if doesWrite:
        client.write(path, str(nodeId))
      else:
        try:
          client.read(path)
        except:
          time.sleep(1) #read failed meaning writing is taking time
      endTime = datetime.datetime.now()
      deltaTime = endTime - startTime

      # outTS.write('{0} {1} {2} {3} BEGIN {4}\n'.format(startTime.hour,
      outTS.write('{0} {1} {2} {3} {4}\n'.format(startTime.hour,
                                                 startTime.minute, startTime.second, startTime.microsecond / 1000, mode))
      # outTS.write('{0} {1} {2} {3} END {4}\n'.format(endTime.hour,
      #   endTime.minute, endTime.second, endTime.microsecond / 1000, mode))
      outDUR.write('{0} {1} {2}\n'.format(mode, deltaTime.seconds, 
                                          deltaTime.microseconds / 1000))
      outTS.flush()
      outDUR.flush()


def endTest(client, etcd=False):
  outTS.close()
  outDUR.close()
  if etcd == True:
    for nodeId in range(maxidx):
      client.delete('/n' + str(nodeId))
