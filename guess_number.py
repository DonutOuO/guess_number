import random

min=input('請決定你的最小範圍:')
max=input('請決定你的最大範圍:')

min=int(min)
max=int(max)
r= random.randint(min,max)

y=0


while True:
	x=input('請輸入數字:')
	y=y+1
	x=int(x)
	if x == r :
		print('終於猜對了')
		print('總共猜了', y ,'次')
		break

	elif x > r :
		print('比答案大')
	
	elif x < r :
		print('比答案小')
	print('這是你猜的第', y ,'次')
