#random_guess number 
import random
now_down = int(input('請輸入數字範圍最小值：'))
now_up = int(input('請輸入數字範圍最大值：'))
r = random.randint(now_down,now_up) #隨機產生一個的整數，包含輸入值的範圍
n = 0 #猜了幾次

while True:
	guess = int(input(f'終極密碼 {now_down}~{now_up} 猜猜看：')) # f'' 是格式化字串語法
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
