#random_guess number 
import random

now_down = int(input('請輸入數字範圍最小值'))
now_up = int(input('請輸入數字範圍最大值'))
r = random.randint(now_down,now_up) #隨機產生一個1~100間的整數，範圍包含1、100
n = 0 #猜了幾次

while True:
	guess = int(input('終極密碼1~100，猜猜看：'))
	n += 1
	if guess == r:
		print('砰！爆炸啦！', '這是你猜的第', n, '次')
		break
	elif guess > r:
		print(now_down, '~', guess)
		now_up = guess
	else:
		print(guess, '~', now_up)
		now_down = guess
	print('這是你猜的第', n, '次')