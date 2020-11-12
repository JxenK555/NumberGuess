import random
first = input('Insert Your First Number: ')
last = input('Insert Your Last Number: ')
first = int(first)
last = int(last)
r = random.randint(first, last)
turn = 0 
while True:
	turn += 1
	num = input('Try A Number: ')
	num = int(num)
	if num == r:
		print('Congratz, You Are Right!')
		print('Total' turn, 'try')
		break
	elif num > r:
		print('Sorry, Try A Smaller Number Please.')
	elif num < r:
		print('Sorry, Try A Bigger Number Please')