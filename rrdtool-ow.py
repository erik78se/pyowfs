import sys
import rrdtool
import ow
import time
import os.path
from dbcreate import createrrd
from graph import render
# http://cuddletech.com/articles/rrd/ar01s02.html
ow.init('127.0.0.1:4304')



# Step/store. Update every N sec

def main(rrdfile=None):
    
    i = 0
    while 1: 
        if i%3 == 0 :
            render(rrdfile)
   
        i += 1
    
        s = ow.Sensor('/28.FEDC2F040000')
        temp = s.temperature.strip()
        print "RRD update with {}".format(temp)

        ret = rrdtool.update(rrdfile, "N:%s" % temp)
        if ret:
            print rrdtool.error()
        time.sleep(60)

if __name__ == "__main__":
    if not os.path.isfile(sys.argv[1]):
        createrrd(sys.argv[1])
    main(rrdfile=sys.argv[1])
