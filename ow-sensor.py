import datetime
import ow
import time
ow.init('127.0.0.1:4304')

dt = datetime.datetime.now().time().isoformat()

list_of_sensors = ow.Sensor("/")

for l in list_of_sensors:
    print l


s = ow.Sensor('/28.FEDC2F040000')
temp = s.temperature.strip()
print dt + " " + temp


