import sys
import dice
import ui

def dwarven_qualified(scores):
	result = True
	if scores[0] < 8:
		print("STRENGTH: {} is too low for a dwarf, a minimum of 8 is required".format(scores[0]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 11:
		print("CONSTITUTION: {} is too low for a dwarf, a minimum of 12 (adjusted) is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	return result

def elven_qualified(scores):
	result = True
	if scores[1] < 8:
		print("INTELLIGENCE: {} is too low for an elf, a minimum of 8 is required".format(scores[1]),
		      file=sys.stderr)
		result = False
	elif scores[3] < 6:
		print("DEXTERITY: {} is too low for an elf, a minimum of 7 (adjusted) is required".format(scores[3]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 7:
		print("CONSTITUTION: {} is too low for an elf, a minimum of 6 (adjusted) is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	elif scores[5] < 8:
		print("CONSTITUTION: {} is too low for an elf, a minimum of 8 is required".format(scores[5]),
		      file=sys.stderr)
		result = False
	return result

def gnome_qualified(scores):
	result = True
	if scores[0] < 6:
		print("STRENGTH: {} is too low for a gnome, a minimum of 6 is required".format(scores[0]),
		      file=sys.stderr)
		result = False
	elif scores[1] < 7:
		print("INTELLIGENCE: {} is too low for a gnome, a minimum of 7 is required".format(scores[1]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 8:
		print("CONSTITUTION: {} is too low for a gnome, a minimum of 8 is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	return result

def half_elven_qualified(scores):
	result = True
	if scores[1] < 4:
		print("INTELLIGENCE: {} is too low for a half-elf, a minimum of 4 is required".format(scores[1]),
		      file=sys.stderr)
		result = False
	elif scores[3] < 6:
		print("DEXTERITY: {} is too low for a half-elf, a minimum of 6 is required".format(scores[3]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 6:
		print("CONSTITUTION: {} is too low for a half-elf, a minimum of 6 is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	return result

def halfling_qualified(scores):
	result = True
	if scores[0] < 7:
		print("STRENGTH: {} is too low for a halfling, a minimum of 6 (adjusted) is required".format(scores[0]),
		      file=sys.stderr)
		result = False
	elif scores[1] < 6:
		print("INTELLIGENCE: {} is too low for a halfling, a minimum of 6 is required".format(scores[1]),
		      file=sys.stderr)
		result = False
	elif scores[3] < 7:
		print("DEXTERITY: {} is too low for a halfling, a minimum of 8 (adjusted) is required".format(scores[3]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 10:
		print("CONSTITUTION: {} is too low for a halfling, a minimum of 10 is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	return result

def half_orc_qualified(scores):
	result = True
	if scores[0] < 5:
		print("STRENGTH: {} is too low for a half-orc, a minimum of 6 (adjusted) is required".format(scores[0]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 12:
		print("CONSTITUTION: {} is too low for a half-orc, a minimum of 13 (adjusted) is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	return result

def get_ancestry(scores):
	while True:
		ancestry = input("Which ancestry do they belong to?\n" \
				 "Dwarven, Elven, Gnome, Half-Elven, Halfling, Half-Orc, or " \
				 "Human\n")
		if not ui.is_ancestry(ancestry):
			print("Invalid ancestry option: {}\n".format(ancestry), file=sys.stderr)
			continue
		is_masc = ui.is_masc(input("What type of build do they have?\n" \
					   "Masculine or Feminine\n"))
		if ui.is_dwarven(ancestry) and dwarven_qualified(scores):
			if scores[0] > 17 and not is_masc:
				print("STRENGTH: {} is too high for a feminine dwarf, reducing to 17".format(scores[0]),
				      file=sys.stderr)
				scores[0] = 17
			if scores[3] > 17:
				print("DEXTERITY: {} is too high for a dwarf, reducing to 17".format(scores[3]),
				      file=sys.stderr)
				scores[3] = 17
			scores[4] = scores[4] + 1
			if int(scores[5]) > 16:
				print("CHARISMA: {} is too high for a dwarf, reducing to 16 for non-dwarves".format(scores[5]),
				      file=sys.stderr)
				scores[5] = "16 ({})".format(scores[5])
			else:
				scores[5] = "{} ({})".format(scores[5] - 1, scores[5])
			break
		elif ui.is_elven(ancestry) and elven_qualified(scores):
			if scores[0] > 16 and not is_masc:
				print("STRENGTH: {} is too high for a feminine elf, reducing to 16".format(scores[0]),
				      file=sys.stderr)
				scores[0] = 16
			scores[3] = scores[3] + 1
			scores[4] = scores[4] - 1
			break
		elif ui.is_gnome(ancestry) and gnome_qualified(scores):
			if scores[0] > 15 and not is_masc:
				print("STRENGTH: {} is too high for a feminine gnome, reducing to 15".format(scores[0]),
				      file=sys.stderr)
				scores[0] = 15
			break
		elif ui.is_half_elven(ancestry) and half_elven_qualified(scores):
			if scores[0] > 17 and not is_masc:
				print("STRENGTH: {} is too high for a feminine half-elf, reducing to 17".format(scores[0]),
				      file=sys.stderr)
				scores[0] = 17
			break
		elif ui.is_halfling(ancestry) and halfling_qualified(scores):
			if scores[0] > 15 and not is_masc:
				print("STRENGTH: {} is too high for a feminine halfling, reducing to 14".format(scores[0]),
				      file=sys.stderr)
				scores[0] = 14
			else:
				scores[0] = scores[0] - 1
			if scores[2] > 17:
				print("WISDOM: {} is too high for a halfling, reducing to 17".format(scores[2]),
				      file=sys.stderr)
				scores[2] = 17
			if scores[3] < 18:
				scores[3] = scores[3] + 1
			break
		elif ui.is_half_orc(ancestry) and half_orc_qualified(scores):
			if scores[0] < 18:
				scores[0] = scores[0] + 1
			if scores[1] > 17:
				print("INTELLIGENCE: {} is too high for a half-orc, reducing to 17".format(scores[1]),
				      file=sys.stderr)
				scores[1] = 17
			if scores[2] > 14:
				print("WISDOM: {} is too high for a half-orc, reducing to 14".format(scores[2]),
				      file=sys.stderr)
				scores[2] = 14
			if scores[3] > 17:
				print("DEXTERITY: {} is too high for a half-orc, reducing to 17".format(scores[3]),
				      file=sys.stderr)
				scores[3] = 17
			scores[4] = scores[4] + 1
			if int(scores[5]) > 12:
				print("CHARISMA: {} is too high for a half-orc, reducing to 12 for non-half-orcs".format(scores[5]),
				      file=sys.stderr)
				scores[5] = "12 ({})".format(scores[5])
			else:
				scores[5] = "{} ({})".format(scores[5] - 2, scores[5])
			break
		elif ui.is_human(ancestry):
			break
		else:
			print("Invalid option for rolled ability scores: {}\n".format(ancestry), file=sys.stderr)

	print("\nAdjusted scores:")
	ui.print_scores(scores)
	return ancestry, scores

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

def select_score(scores_rolled, scores, name):
	while True:
		print(scores_rolled)
		score = int(input("{} = ?\n".format(name)))
		if score in scores_rolled:
			scores_rolled.remove(score)
			scores.append(score)
			break
		else:
			print("Score {} not in remaining rolled scores".format(score), file=sys.stderr)
	return scores_rolled, scores

def arrange_scores(raw_scores, method_scores):
	scores = []
	if not raw_scores[0]:
		method_scores, scores = select_score(method_scores, scores, "STRENGTH")
	else:
		scores.append(raw_scores[0])
	if not raw_scores[1]:
		if len(method_scores) != 1:
			method_scores, scores = select_score(method_scores, scores, "INTELLIGENCE")
		else:
			scores.append(method_scores[0])
			method_scores.remove(method_scores[0])
	else:
		scores.append(raw_scores[1])
	if not raw_scores[2]:
		if len(method_scores) != 1:
			method_scores, scores = select_score(method_scores, scores, "WISDOM")
		else:
			scores.append(method_scores[0])
			method_scores.remove(method_scores[0])
	else:
		scores.append(raw_scores[2])
	if not raw_scores[3]:
		if len(method_scores) != 1:
			method_scores, scores = select_score(method_scores, scores, "DEXTERITY")
		else:
			scores.append(method_scores[0])
			method_scores.remove(method_scores[0])
	else:
		scores.append(raw_scores[3])
	if not raw_scores[4]:
		if len(method_scores) != 1:
			method_scores, scores = select_score(method_scores, scores, "CONSTITUTION")
		else:
			scores.append(method_scores[0])
			method_scores.remove(method_scores[0])
	else:
		scores.append(raw_scores[4])
	if not raw_scores[5]:
		scores.append(method_scores[0])
	else:
		scores.append(raw_scores[5])
	return scores

def generate_scores():
	method = get_method()
	scores = []
	match method:
		case 1:
			print("Arrange these as the player desires:")
			scores_rolled = method_2()
			scores_rolled, scores = select_score(scores_rolled, scores, "STRENGTH")
			scores_rolled, scores = select_score(scores_rolled, scores, "INTELLIGENCE")
			scores_rolled, scores = select_score(scores_rolled, scores, "WISDOM")
			scores_rolled, scores = select_score(scores_rolled, scores, "DEXTERITY")
			scores_rolled, scores = select_score(scores_rolled, scores, "CONSTITUTION")
			scores.append(scores_rolled[0])
		case 2:
			print("Arrange these as the player desires:")
			scores_rolled = method_2()
			scores_rolled, scores = select_score(scores_rolled, scores, "STRENGTH")
			scores_rolled, scores = select_score(scores_rolled, scores, "INTELLIGENCE")
			scores_rolled, scores = select_score(scores_rolled, scores, "WISDOM")
			scores_rolled, scores = select_score(scores_rolled, scores, "DEXTERITY")
			scores_rolled, scores = select_score(scores_rolled, scores, "CONSTITUTION")
			scores.append(scores_rolled[0])
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
			print("## | STRENGTH | INTELLIGENCE | WISDOM | DEXTERITY | CONSTITUTION | CHARISMA")
			for i in range(1, len(score_sets) + 1):
				scores = score_sets[i - 1]
				line = "{} "
				if i < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}       "
				if scores[0] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}           "
				if scores[1] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}     "
				if scores[2] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}        "
				if scores[3] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}           "
				if scores[4] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}"
				print(line.format(i, scores[0], scores[1], scores[2], scores[3], scores[4], scores[5]))
			print("---------------------------------------------------------------------------\n")
			while True:
				selection = int(input("Which numbered set of scores should be used?\n"))
				if selection > 0 and selection < 13:
					scores = score_sets[selection - 1]
					break
				else:
					print("Invalid selection, 1-12 expected", file=sys.stderr)
		case 5:
			scores = method_5()
			print("STRENGTH: {}".format(scores[0]))
			print("INTELLIGENCE: {}".format(scores[1]))
			print("WISDOM: {}".format(scores[2]))
			print("DEXTERITY: {}".format(scores[3]))
			print("CONSTITUTION: {}".format(scores[4]))
			print("CHARISMA: {}".format(scores[5]))
		case 6:
			raw_scores, method1_scores = method_6()
			if raw_scores[0]:
				print("STRENGTH: {}".format(raw_scores[0]))
			if raw_scores[1]:
				print("INTELLIGENCE: {}".format(raw_scores[1]))
			if raw_scores[2]:
				print("WISDOM: {}".format(raw_scores[2]))
			if raw_scores[3]:
				print("DEXTERITY: {}".format(raw_scores[3]))
			if raw_scores[4]:
				print("CONSTITUTION: {}".format(raw_scores[4]))
			if raw_scores[5]:
				print("CHARISMA: {}".format(raw_scores[5]))
			if method1_scores:
				print("Arrange these as desired:")
			scores = arrange_scores(raw_scores, method1_scores)
		case 7:
			raw_scores, method2_scores = method_7()
			if raw_scores[0]:
				print("STRENGTH: {}".format(raw_scores[0]))
			if raw_scores[1]:
				print("INTELLIGENCE: {}".format(raw_scores[1]))
			if raw_scores[2]:
				print("WISDOM: {}".format(raw_scores[2]))
			if raw_scores[3]:
				print("DEXTERITY: {}".format(raw_scores[3]))
			if raw_scores[4]:
				print("CONSTITUTION: {}".format(raw_scores[4]))
			if raw_scores[5]:
				print("CHARISMA: {}".format(raw_scores[5]))
			if method2_scores:
				print("Arrange these as desired:")
			scores = arrange_scores(raw_scores, method2_scores)
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
			print("## | STRENGTH | INTELLIGENCE | WISDOM | DEXTERITY | CONSTITUTION | CHARISMA")
			for i in range(1, len(score_sets) + 1):
				scores = score_sets[i - 1]
				line = "{} "
				if i < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}       "
				if scores[0] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}           "
				if scores[1] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}     "
				if scores[2] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}        "
				if scores[3] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}           "
				if scores[4] < 10:
					line = line + " | "
				else:
					line = line + "| "
				line = line + "{}"
				print(line.format(i, scores[0], scores[1], scores[2], scores[3], scores[4], scores[5]))
			print("---------------------------------------------------------------------------\n")
			while True:
				selection = int(input("Which numbered set of scores should be used?\n"))
				if selection > 0 and selection < 13:
					scores = score_sets[selection - 1]
					break
				else:
					print("Invalid selection, 1-12 expected", file=sys.stderr)
		case 10:
			scores = method_10()
			print("STRENGTH: {}".format(scores[0]))
			print("INTELLIGENCE: {}".format(scores[1]))
			print("WISDOM: {}".format(scores[2]))
			print("DEXTERITY: {}".format(scores[3]))
			print("CONSTITUTION: {}".format(scores[4]))
			print("CHARISMA: {}".format(scores[5]))

	print("\nInitial scores:")
	ui.print_scores(scores)

	return scores, method < 5

def main():
	scores, is_pc = generate_scores()
	ancestry, scores = get_ancestry(scores)
	return 0

if __name__ == '__main__':
	sys.exit(main())