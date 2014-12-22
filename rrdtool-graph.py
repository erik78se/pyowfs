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

def render_graph(fname):
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
              'VDEF:tempavg=temp,AVERAGE' ,
              'VDEF:tempmax=temp,MAXIMUM' ,
              'VDEF:tempmin=temp,MINIMUM' ,
              'AREA:temp#01DF01:Temperature' ,
              'LINE:tempmax#FF0000:Max' ,
              r'GPRINT:tempmax:Max\: %6.1lf C' ,
              r'GPRINT:tempavg:Avg\: %6.1lf C' ,
              r'GPRINT:tempmin:Min\: %6.1lf C' ,
              )


if __name__== "__main__":
    if sys.argv[1] == "create":
	createrrd()
    else:
        print "Rendering image"
        render_graph(sys.argv[1])
