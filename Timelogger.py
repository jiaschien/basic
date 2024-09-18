
import time
import csv

while True:
    action = input("计时?(,|.|?|>) 注释 -->:").split()
    if action[0] == ',':
        now = time.time()
        tl = time.localtime(now)
        format_time = time.strftime('%Y-%m-%d, %H:%M:%S', tl)
        print(format_time)
    elif action[0] == '.':
        now = time.time()
        tl = time.localtime(now)
        end_time_format = time.strftime('%Y-%m-%d, %H:%M:%S', tl)
	#	elasped_time = 
