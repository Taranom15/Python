from datetime import datetime
import random
import time

odds = [1, 3, 5, 7, 8, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
for num in range(5):
	right_this_min = datetime.today().minute
	if right_this_min in odds:
		print('This min seems a bit odd ' + str(right_this_min))
	else:
		print('Not an odd min!' + str(right_this_min))
	wait_time = random.randint(1,60)
	print(wait_time)
	time.sleep(wait_time)
