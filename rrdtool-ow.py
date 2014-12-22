import sys
import rrdtool
import ow
import time
import os.path
from dbcreate import createrrd
# http://cuddletech.com/articles/rrd/ar01s02.html
ow.init('127.0.0.1:4304')



# Step/store. Update every 10 sec

def render_temp_graph(fname):
    print "Rendering new image."
    info = rrdtool.info(fname)
    for i in info:
	print "{} : {}".format(i,info[i])

    DAY = 86400
    DAYS_5 = DAY * 5
    YEAR = 365 * DAY
    rrdtool.graph('image-temp.png',
              '--imgformat', 'PNG',
              '--width', '540',
              '--height', '100',
              '--start', "-%i" % DAY,
              '--end', "-1",
              '--vertical-label', 'Temperature C',
              '--title', 'Temperature over last 24h',
              '--lower-limit', '0',
              'DEF:temp=%s:sensor1-temp:AVERAGE' % fname ,
              'VDEF:tempmax=temp,MAXIMUM' ,
              'VDEF:tempavg=temp,AVERAGE' ,
              'VDEF:tempmin=temp,MINIMUM' ,
              'LINE1:temp#FF0000:Average Temp' ,
              'LINE1:tempmax#FFFF00:Max temp' ,
              'LINE1:tempmin#FFFFFF:Min temp' ,
              r'GPRINT:tempmax:Max\: %6.1lf C' ,
              r'GPRINT:tempavg:Avg\: %6.1lf C' ,
              r'GPRINT:tempmin:Min\: %6.1lf C' ,
              'AREA:temp#990033:Temperature')

# main loop

def main(rrdfile=None):
    
    i = 0
    while 1: 
        if i%3 == 0 :
            render_temp_graph('sensor_1.rrd')
   
        i += 1
    
        s = ow.Sensor('/28.FEDC2F040000')
        temp = s.temperature.strip()
        print "RRD update with {}".format(temp)

        ret = rrdtool.update('sensor_1.rrd', "N:%s" % temp)
        if ret:
            print rrdtool.error()
        time.sleep(60)

if __name__ == "__main__":
    if not os.path.isfile(sys.argv[1]):
        createrrd(sys.argv[1])
    main(rrdfile=sys.argv[1])
