from functions import *
import time

while True:
	try:
		get_old()
	except:
		print "db empty"
	time.sleep(15)
