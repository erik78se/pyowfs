import sys
import rrdtool
import ow
import time

# http://cuddletech.com/articles/rrd/ar01s02.html
ow.init('127.0.0.1:4304')



# Step/store. Update every 10 sec

def createrrd():
    data_sources = [ 'DS:sensor1-temp:GAUGE:120:-50:50'] 
    rrdtool.create( 'sensor_1.rrd',
                '--start', 'N', '--step', '60',
                data_sources,
		'RRA:AVERAGE:0.5:1:1440',
		'RRA:MIN:0.5:5:1400', 
		'RRA:MAX:0.5:5:1440',  
		) 

# createrrd()


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

def main():
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

main()
