import sys
import multiprocessing
from zookeeper_read_client import readTest, cleanUp, startUp
from zookeeper_write_client import writeTest
import time

sleeptime = 1 #in minutes
leaders = {3: '172.31.3.130', 5: '172.31.16.222', 7: '172.31.23.49'} #ESTELLE: Change this?
writeratios = [5, 20, 50]

#normal ops test
for cluster, ip in leaders.items():
    for x in writeratios:
        startUp(cluster)
        #200 clients total
        write_clients = x*2
        read_clients = (100-x)*2
        # write_clients = 2
        # read_clients = 2
        ps = []
        print "For cluster-{0}, with leader: [{1}], writeratio: [{2}]\n".format(cluster, ip, x)
        for wc in range(write_clients):
            p = multiprocessing.Process(target=writeTest, name="WriteTest", args=(cluster, ip, x,))
            p.start()
            ps.append(p)
        for rc in range(read_clients):
            p = multiprocessing.Process(target=readTest, name="ReadTest", args=(cluster, ip, x,))
            p.start()
            ps.append(p)
        time.sleep(sleeptime*60)
        for p in ps:
            p.terminate()
            print "runTest terminated"
            p.join()
#        cleanUp(cluster, ip) #delete nods
