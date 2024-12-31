from datetime import *
time_1= datetime.strptime('2:00:00',"%H:%M:%S")
time_2= datetime.strptime('11:00:00',"%H:%M:%S")
time_interval=time_2 - time_1
print(time_interval)
