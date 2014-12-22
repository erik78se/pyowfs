import ow
ow.init('127.0.0.1:4304')
s = ow.Sensor('/28.FEDC2F040000')
print s.temperature.strip()
