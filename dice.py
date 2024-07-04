import random

def d(num, dice):
	value = 0
	for _ in range(num):
		value = value + random.randrange(dice) + 1
	return value

def d3():
	return random.randrange(3) + 1

def d4():
	return random.randrange(4) + 1

def d6():
	return random.randrange(6) + 1

def d8():
	return random.randrange(8) + 1

def d10():
	return random.randrange(10) + 1

def d12():
	return random.randrange(12) + 1

def d20():
	return random.randrange(20) + 1

def d100():
	return random.randrange(100) + 1