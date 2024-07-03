import sys
import dice
import ui

def get_germane_method():
	while True:
		# Only player options are reported
		response = int(input("Which method should be used for germane abilities?\n" \
				     "1. 4d6 - lowest, scores manually ordered\n" \
				     "2. 3d6 12 times, highest 6 manually ordered\n" \
				     "3. 3d6 6 times in order, highest of each\n" \
				     "4. 3d6 12 times in order, manually chosen\n" \
				     "5. 3d6 with +1 to each die < 6\n"))
		if response > 0 and response < 6:
			break
		else:
			print("Invalid option: {}, expected 1-4".format(response), file=sys.stderr)
	return response + 5

def get_pc_method():
	while True:
		# Only player options are reported
		response = int(input("Which method would you like to use?\n" \
				     "1. 4d6 - lowest, scores manually ordered\n" \
				     "2. 3d6 12 times, highest 6 manually ordered\n" \
				     "3. 3d6 6 times in order, highest of each\n" \
				     "4. 3d6 12 times in order, manually chosen\n"))
		if response > 0 and response < 11:
			break
		else:
			print("Invalid option: {}, expected 1-4".format(response), file=sys.stderr)
	return response

def get_method():
	method = 0
	if len(sys.argv) < 2:
		if ui.is_negative(input("Is this character determined as a Player Character?\n")):
			if ui.is_negative(input("Is this NPC special?\n")):
				method = 5
			else:
				method = get_germane_method()
		else:
			method = get_pc_method()
	else:
		method = int(sys.argv[1])
	return method

def get_germane():
	abilities = []
	if len(sys.argv) < 3:
		while True:
			ability = int(input("Which ability is germane to their profession?\n" \
					    "1. STRENGTH\n" \
					    "2. INTELLIGENCE\n" \
					    "3. WISDOM\n" \
					    "4. DEXTERITY\n" \
					    "5. CONSTITUTION\n" \
					    "6. CHARISMA\n" \
					    "7. No more abilities are germane\n"))
			if ability < 1 or ability > 7:
				print("Invalid input: {}, expected 1-6".format(ability), file=sys.stderr)
			elif ability < 7:
				abilities.append(ability)
			else:
				break
	else:
		for arg in sys.argv[2:]:
			ability = int(arg)
			if ability < 1 or ability > 6:
				print("Invalid input: {}, expected 1-6".format(ability), file=sys.stderr)
			abilities.append(ability)
	return abilities

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

# General Characters
def method_5():
	scores = []
	for _ in range(6):
		roll1 = dice.d6()
		if roll1 == 1:
			roll1 = 3
		elif roll1 == 6:
			roll1 = 4
		roll2 = dice.d6()
		if roll2 == 1:
			roll2 = 3
		elif roll2 == 6:
			roll2 = 4
		roll3 = dice.d6()
		if roll3 == 1:
			roll3 = 3
		elif roll3 == 6:
			roll3 = 4
		scores.append(roll1 + roll2 + roll3)
	return scores

# Special NPCs with germane abilities as Method 1
def method_6():
	scores = []
	method1_scores = method_1()
	abilities = get_germane()
	for _ in range(6 - len(abilities)):
		method1_scores.remove(min(method1_scores))
	for i in range(1, 7):
		if i in abilities:
			if len(abilities) == 1:
				scores.append(method1_scores[0])
				method1_scores.remove(method1_scores[0])
			else:
				scores.append(0)
			continue
		roll1 = dice.d6()
		roll2 = dice.d6()
		roll3 = dice.d6()
		scores.append(roll1 + roll2 + roll3)
	return scores, method1_scores

# Special NPCs with germane abilities as Method 2
def method_7():
	scores = []
	method2_scores = method_2()
	abilities = get_germane()
	for _ in range(6 - len(abilities)):
		method2_scores.remove(min(method2_scores))
	for i in range(1, 7):
		if i in abilities:
			if len(abilities) == 1:
				scores.append(method2_scores[0])
				method2_scores.remove(method2_scores[0])
			else:
				scores.append(0)
			continue
		roll1 = dice.d6()
		roll2 = dice.d6()
		roll3 = dice.d6()
		scores.append(roll1 + roll2 + roll3)
	return scores, method2_scores

# Special NPCs with germane abilities as Method 3
def method_8():
	scores = []
	abilities = get_germane()
	for i in range(1, 7):
		if i in abilities:
			score = 0
			for _ in range(6):
				roll1 = dice.d6()
				roll2 = dice.d6()
				roll3 = dice.d6()
				score = max(score, roll1 + roll2 + roll3)
			scores.append(score)
		else:
			roll1 = dice.d6()
			roll2 = dice.d6()
			roll3 = dice.d6()
			scores.append(roll1 + roll2 + roll3)
	return scores

# Special NPCs with germane abilities as Method 4
def method_9():
	score_sets = method_4()
	abilities = get_germane()
	for i in range(1, 7):
		if i in abilities:
			continue
		roll1 = dice.d6()
		roll2 = dice.d6()
		roll3 = dice.d6()
		score = roll1 + roll2 + roll3
		for j in range(len(score_sets)):
			score_sets[j][i - 1] = score
	return score_sets

# Special NPCs not determined as Player Characters
def method_10():
	scores = []
	abilities = get_germane()
	for i in range(1, 7):
		germane = i in abilities
		roll1 = dice.d6()
		if germane and roll1 < 6:
			roll1 = roll1 + 1
		roll2 = dice.d6()
		if germane and roll2 < 6:
			roll2 = roll2 + 1
		roll3 = dice.d6()
		if germane and roll3 < 6:
			roll3 = roll3 + 1
		scores.append(roll1 + roll2 + roll3)
	return scores

def generate_scores():
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
			score_sets = method_4()
			print("Select the most desirable single set of scores:")
			print("STRENGTH | INTELLIGENCE | WISDOM | DEXTERITY | CONSTITUTION | CHARISMA")
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
		case 5:
			scores = method_5()
			print("STRENGTH: {}".format(scores[0]))
			print("INTELLIGENCE: {}".format(scores[1]))
			print("WISDOM: {}".format(scores[2]))
			print("DEXTERITY: {}".format(scores[3]))
			print("CONSTITUTION: {}".format(scores[4]))
			print("CHARISMA: {}".format(scores[5]))
		case 6:
			scores, method1_scores = method_6()
			if scores[0]:
				print("STRENGTH: {}".format(scores[0]))
			if scores[1]:
				print("INTELLIGENCE: {}".format(scores[1]))
			if scores[2]:
				print("WISDOM: {}".format(scores[2]))
			if scores[3]:
				print("DEXTERITY: {}".format(scores[3]))
			if scores[4]:
				print("CONSTITUTION: {}".format(scores[4]))
			if scores[5]:
				print("CHARISMA: {}".format(scores[5]))
			if method1_scores:
				print("Arrange these as desired:")
				print(method1_scores)
		case 7:
			scores, method2_scores = method_7()
			if scores[0]:
				print("STRENGTH: {}".format(scores[0]))
			if scores[1]:
				print("INTELLIGENCE: {}".format(scores[1]))
			if scores[2]:
				print("WISDOM: {}".format(scores[2]))
			if scores[3]:
				print("DEXTERITY: {}".format(scores[3]))
			if scores[4]:
				print("CONSTITUTION: {}".format(scores[4]))
			if scores[5]:
				print("CHARISMA: {}".format(scores[5]))
			if method2_scores:
				print("Arrange these as desired:")
				print(method2_scores)
		case 8:
			scores = method_8()
			print("STRENGTH: {}".format(scores[0]))
			print("INTELLIGENCE: {}".format(scores[1]))
			print("WISDOM: {}".format(scores[2]))
			print("DEXTERITY: {}".format(scores[3]))
			print("CONSTITUTION: {}".format(scores[4]))
			print("CHARISMA: {}".format(scores[5]))
		case 9:
			score_sets = method_9()
			print("Select the most desirable single set of scores:")
			print("STRENGTH | INTELLIGENCE | WISDOM | DEXTERITY | CONSTITUTION | CHARISMA")
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
		case 10:
			scores = method_10()
			print("STRENGTH: {}".format(scores[0]))
			print("INTELLIGENCE: {}".format(scores[1]))
			print("WISDOM: {}".format(scores[2]))
			print("DEXTERITY: {}".format(scores[3]))
			print("CONSTITUTION: {}".format(scores[4]))
			print("CHARISMA: {}".format(scores[5]))

	return scores

def main():
	scores = generate_scores()
	return 0

if __name__ == '__main__':
	sys.exit(main())