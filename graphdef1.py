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
              'LINE1:temp#FF0000:Average Temp' ,
              'LINE1:tempmax#FFFF00:Max temp' ,
              'LINE1:tempmin#FFFFFF:Min temp' ,
              r'GPRINT:tempmax:Max\: %6.1lf C' ,
              r'GPRINT:tempavg:Avg\: %6.1lf C' ,
              r'GPRINT:tempmin:Min\: %6.1lf C' ,
              'LINE:temp#990033:Temperature')
