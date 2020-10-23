import random
num = random.randint(1, 10)
while True:
	print('guess the number from 1 to 10') 
	guess = input()
	i = int(guess)
	if i == num:
		print('yas!')  
		break
	elif i < num:
		print('bigger')
	elif i > num:
		print('smaller')