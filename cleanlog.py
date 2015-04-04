import sys
import glob
import os
import errno

def make_clean_dir():
    try:
        os.makedirs("./cleanlog")
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def start_clean():
    make_clean_dir()
    for file in glob.glob("./log/dur*.txt"):
        print "Cleaning: [{0}]".format(file)
        with open(file, "r") as input:
            nm = file.split("/")
            with open("./cleanlog/"+nm[-1], "wb") as output:
                for line in input:
                    a = line.split(" ")
                    if len(a) != 3:
                        continue
                    cmd = a[0]
                    try:
                        sec = int(a[1])
                        ms = int(a[2])
                    except:
                        continue
                    output.write(line)
    for file in glob.glob("./log/ts*.txt"):
        print "Cleaning: [{0}]".format(file)
        with open(file, "r") as input:
            nm = file.split("/")
            with open("./cleanlog/"+nm[-1], "wb") as output:
                for line in input:
                    a = line.split(" ")
                    if len(a) != 5:
                        continue
                    try:
                        hr = int(a[0])
                        min = int(a[1])
                        sec = int(a[2])
                        ms = int(a[3])
                    except:
                        continue
                    mode = a[4]
                    if mode != 'read' and mode != 'write':
                        continue
                    output.write(line)

    print "Output is in ./cleanlog\n"

start_clean()
