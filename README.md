# pyowfs
A small set of tools to graph temperature readings. Using OWFS.

This code was initially written to be used with 
1 RasberryPi B+
1 OneWire USB adapter
1 Temperature sensor DS18B20

# Setup
 Install owfsd (it should bring up web-access and all
 > apt-get install owfsd
 
 Configure (/etc/owfsd.conf)
 
 Example config is in the directory.
 
 Try access the web-interface for owfs:
 
 > http://127.0.0.1:2121/
  
# Initialize RRD-database

> python dbcreate.py <filename.rrd>
 
This creates a new rrd-database to be updated every 60 sec.

# Run updater process

> nohup python rrdtool-ow.py 2&>/dev/null

Updates the RRD database and creates an image continously

# Serve the files
 This will serve the current directory - for testing purposes.
 > nohup python -c "import CGIHTTPServer;CGIHTTPServer.test()" &
 
 Access the image with url:
 > http://127.0.0.1/image-temp.png

 
