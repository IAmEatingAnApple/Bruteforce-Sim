import random
import time
global spid1

num = 0

def fast():
	a = 0
	b = 0
	c = 0
	d = 0
	while c != num:
		b = random.randint(-1000000, 1000000)
		d = random.randint(-1000000, 1000000)
		c = a + b + d
		print(f'{a} + {b} + {d} = {c}')
		a = b
	print(f'ебать ахуеть взломано ебать число {c}')
	
def slower():
	a = 0
	b = 0
	c = 0
	d = 0
	global spid1
	while c != num:
		b = random.randint(-1000000, 1000000)
		d = random.randint(-1000000, 1000000)
		c = a + b + d
		print(f'{a} + {b} + {d} = {c}')
		a = b
		time.sleep(spid1)
	print(f'ебать ахуеть взломано ебать число {c}')

num = random.randint(-1000000, 1000000)
print(f'Рандомное число сгенерировано. Введите скорость подбора (1/2/3/4/5/6)')
spid = int(input(""))
if spid == 1:
	spid1 = 0.5
elif spid == 2:
	spid1 = 0.3
elif spid == 3:
	spid1 = 0.1
elif spid == 4:
	spid1 = 0.05
elif spid == 5:
	spid1 = 0.01
elif spid == 6:
	pass
else:
	exit()
print('Начинаем...')
time.sleep(2)
if spid == 6:
	fast()
else:
	slower()