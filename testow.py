import ow
import time


ow.init('127.0.0.1:4304')

while True:
    s = ow.Sensor('/28.FEDC2F040000')
    print s.temperature
    time.sleep(2)
