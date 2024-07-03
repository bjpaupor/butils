import sys
import dice

def get_method():
	method = 0
	if len(sys.argv) != 2:
		method = int(input("Which method would you like to use?\n" \
				   "1. 4d6 - lowest, scores manually ordered\n" \
				   "2. 3d6 12 times, highest 6 manually ordered\n" \
				   "3. 3d6 6 times in order, highest of each\n" \
				   "4. 3d6 12 times in order, manually chosen\n"))
	else:
		method = int(sys.argv[1])
	return method

def method_1():
	scores = []
	for _ in range(6):
		roll1 = dice.d6()
		roll2 = dice.d6()
		roll3 = dice.d6()
		roll4 = dice.d6()
		scores.append(roll1 + roll2 + roll3 + roll4 - min(roll1, roll2, roll3, roll4))
	return scores

def method_2():
	scores = []
	for _ in range(12):
		roll1 = dice.d6()
		roll2 = dice.d6()
		roll3 = dice.d6()
		scores.append(roll1 + roll2 + roll3)
	for _ in range(6):
		scores.remove(min(scores))
	return scores

def method_3():
	scores = []
	for _ in range(6):
		score = 0
		for _ in range(6):
			roll1 = dice.d6()
			roll2 = dice.d6()
			roll3 = dice.d6()
			score = max(score, roll1 + roll2 + roll3)
		scores.append(score)
	return scores

def method_4():
	score_sets = []
	for _ in range(12):
		scores = []
		for _ in range(6):
			roll1 = dice.d6()
			roll2 = dice.d6()
			roll3 = dice.d6()
			scores.append(roll1 + roll2 + roll3)
		score_sets.append(scores)
	return score_sets

def main():
	match get_method():
		case 1:
			print("Arrange these as the player desires:")
			print(method_1())
		case 2:
			print("Arrange these as the player desires:")
			print(method_2())
		case 3:
			scores = method_3()
			print("STRENGTH: {}".format(scores[0]))
			print("INTELLIGENCE: {}".format(scores[1]))
			print("WISDOM: {}".format(scores[2]))
			print("DEXTERITY: {}".format(scores[3]))
			print("CONSTITUTION: {}".format(scores[4]))
			print("CHARISMA: {}".format(scores[5]))
		case 4:
			print("Select the most desirable single set of scores:")
			print("STRENGTH | INTELLIGENCE | WISDOM | DEXTERITY | CONSTITUTION | CHARISMA")
			score_sets = method_4()
			for scores in score_sets:
				line = "{}         "
				if scores[0] < 10:
					line = line + " "
				line = line + "{}             "
				if scores[1] < 10:
					line = line + " "
				line = line + "{}       "
				if scores[2] < 10:
					line = line + " "
				line = line + "{}          "
				if scores[3] < 10:
					line = line + " "
				line = line + "{}             "
				if scores[4] < 10:
					line = line + " "
				line = line + "{}"
				print(line.format(scores[0], scores[1], scores[2], scores[3], scores[4], scores[5]))
	return 0

if __name__ == '__main__':
	sys.exit(main())