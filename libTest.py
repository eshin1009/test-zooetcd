import os
import datetime
import socket

op_repeat = 10
maxidx = 0

pid = os.getpid()

outTS = ""
outTS = ""
readratio = 0
writeratio = 0
rootpath = '/nodes'

mode = ""
doesWrite = False

def initTest(rw, wratio):
  global mode, doesWrite, outTS, outDUR, writeratio, readratio, maxidx
  mode = rw
  doesWrite = rw == 'write'
  outTS = open('log/log-ts-{0}-{1}-{2}.txt'.format(wratio, rw, pid), 'w')
  outDUR = open('log/log-dur-{0}-{1}-{2}.txt'.format(wratio, rw, pid), 'w')
  writeratio = wratio
  readratio = 100-wratio
  maxidx = wratio * op_repeat

def getMaxIdx():
  return maxidx

def childPath(i):
  return  rootpath + '/n' + '_' + str(i)

def doLoop(client):
  while True:
    for nodeId in range(maxidx):
      path = childPath(nodeId)
      print "{0} {1}".format(mode, path)
      startTime = datetime.datetime.now()
      if doesWrite:
        client.write(path, str(nodeId))
      else:
        client.read(path)
      endTime = datetime.datetime.now()
      deltaTime = endTime - startTime

      outTS.write('{0} {1} {2} {3} BEGIN {4}\n'.format(startTime.hour,
        startTime.minute, startTime.second, startTime.microsecond / 1000, mode))
      outTS.write('{0} {1} {2} {3} END {4}\n'.format(endTime.hour,
        endTime.minute, endTime.second, endTime.microsecond / 1000, mode))
      outDUR.write('{0} {1} {2}\n'.format(mode, deltaTime.seconds, 
        deltaTime.microseconds / 1000))
