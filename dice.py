import random
import sys

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

def main():
	num = 1
	dice = 20
	if len(sys.argv) == 2:
		num = int(sys.argv[1].split("d")[0])
		dice = int(sys.argv[1].split("d")[1])
	print(d(num, dice))
	return 0

if __name__ == '__main__':
	sys.exit(main())