import random
def roller():
	b = input('what die do you want to roll\n')
	if b == 'D4' or b == 'd4':
		w = random.randint(1,4)
	elif b == 'D6' or b == 'd6':
		w = random.randint(1,6)
	elif b == 'D8' or b == 'd8':
		w = random.randint(1,8)
	elif b == 'D10' or b == 'd10':
		w = random.randint(1,10)
	elif b == 'D12' or b == 'd12':
		w = random.randint(1,12)
	elif b == 'D20' or b == 'd20':
		w = random.randint(1,20)
	if w == 20:
		print(f"wow nat {w}")
		return True
	else:
		print(f'the result of your die is {w}')
while True:
	roller()
