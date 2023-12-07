#random_guess number 
import random
r = random.randint(1,100) #隨機產生一個1~100間的整數，範圍包含1、100
guess = int(input('終極密碼1~100，猜猜看：'))
now_down = 0
now_up = 100
while guess != r:
	if guess > r:
		print(now_down, '~', guess)
		now_up = guess
		guess = int(input('終極密碼，猜猜看：'))
	else:
		print(guess, '~', now_up)
		now_down = guess
		guess = int(input('終極密碼，猜猜看：'))
print('砰！爆炸啦！')