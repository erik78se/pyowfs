import sys
import rrdtool
import ow
import time


def createrrd(fname):
    data_sources = [ 'DS:sensor1-temp:GAUGE:120:-50:50'] 
    rrdtool.create( fname,
                '--start', 'N', '--step', '60',
                data_sources,
                'RRA:AVERAGE:0.5:1:1440',
                'RRA:MIN:0.5:5:1400', 
                'RRA:MAX:0.5:5:1440',  
                ) 

if __name__== "__main__":
    print "Creating db: {}".format(sys.argv[1])
