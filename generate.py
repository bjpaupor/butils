import re
import sys
import dice
import ui

def dwarven_qualified(scores, is_pc):
	result = True
	if scores[0] < 8 and is_pc:
		print("STRENGTH: {} is too low for a dwarf, a minimum of 8 is required".format(scores[0]),
		      file=sys.stderr)
		result = False
	elif scores[0] < 7 and not is_pc:
		print("STRENGTH: {} is too low for a dwarf, a minimum of 8 (adjusted) is required".format(scores[0]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 11 and is_pc:
		print("CONSTITUTION: {} is too low for a dwarf, a minimum of 12 (adjusted) is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 10 and not is_pc:
		print("CONSTITUTION: {} is too low for a dwarf, a minimum of 12 (adjusted) is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	return result

def elven_qualified(ancestry, scores, is_pc):
	result = True
	if is_pc and not ui.is_high_elf(ancestry):
		print("Elven type: {} isn't allowed for player characters".format(ancestry),
		      file=sys.stderr)
		result = False
	elif scores[1] < 8 and is_pc:
		print("INTELLIGENCE: {} is too low for an elf, a minimum of 8 is required".format(scores[1]),
		      file=sys.stderr)
		result = False
	elif scores[1] < 7 and not is_pc:
		print("INTELLIGENCE: {} is too low for an elf, a minimum of 8 (adjusted) is required".format(scores[1]),
		      file=sys.stderr)
		result = False
	elif scores[3] < 6 and is_pc:
		print("DEXTERITY: {} is too low for an elf, a minimum of 7 (adjusted) is required".format(scores[3]),
		      file=sys.stderr)
		result = False
	elif scores[3] < 5 and not is_pc:
		print("DEXTERITY: {} is too low for an elf, a minimum of 7 (adjusted) is required".format(scores[3]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 7:
		print("CONSTITUTION: {} is too low for an elf, a minimum of 6 (adjusted) is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 8:
		print("CONSTITUTION: {} is too low for an elf, a minimum of 8 is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	return result

def gnome_qualified(scores, is_pc):
	result = True
	if scores[0] < 6:
		print("STRENGTH: {} is too low for a gnome, a minimum of 6 is required".format(scores[0]),
		      file=sys.stderr)
		result = False
	elif scores[1] < 7:
		print("INTELLIGENCE: {} is too low for a gnome, a minimum of 7 is required".format(scores[1]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 8 and is_pc:
		print("CONSTITUTION: {} is too low for a gnome, a minimum of 8 is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 7 and not is_pc:
		print("CONSTITUTION: {} is too low for a gnome, a minimum of 8 (adjusted) is required".format(scores[4]),
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

def halfling_qualified(scores, is_pc):
	result = True
	if scores[0] < 7:
		print("STRENGTH: {} is too low for a halfling, a minimum of 6 (adjusted) is required".format(scores[0]),
		      file=sys.stderr)
		result = False
	elif scores[1] < 6:
		print("INTELLIGENCE: {} is too low for a halfling, a minimum of 6 is required".format(scores[1]),
		      file=sys.stderr)
		result = False
	elif scores[3] < 7 and is_pc:
		print("DEXTERITY: {} is too low for a halfling, a minimum of 8 (adjusted) is required".format(scores[3]),
		      file=sys.stderr)
		result = False
	elif scores[3] < 6 and not is_pc:
		print("DEXTERITY: {} is too low for a halfling, a minimum of 8 (adjusted) is required".format(scores[3]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 10 and is_pc:
		print("CONSTITUTION: {} is too low for a halfling, a minimum of 10 is required".format(scores[4]),
		      file=sys.stderr)
		result = False
	elif scores[4] < 9 and not is_pc:
		print("CONSTITUTION: {} is too low for a halfling, a minimum of 10 (adjusted) is required".format(scores[4]),
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

def get_ancestry(scores, is_pc):
	is_masc = False
	options = ""
	if is_pc:
		options = "([none], Mountain) Dwarven, Elven, Gnome, Half-Elven, Halfling, Half-Orc, or Human"
	else:
		options = "([none], Mountain) Dwarven, (Aquatic, Drow, Gray, High, Wood) Elven, " \
			  "Gnome, Half-Elven, Halfling, Half-Orc, or Human"
	while True:

		ancestry = input("Which ancestry do they belong to?\n{}\n".format(options))
		if not ui.is_ancestry(ancestry):
			print("Invalid ancestry option: {}\n".format(ancestry), file=sys.stderr)
			continue
		is_masc = ui.is_masc(input("What type of build do they have?\n" \
					   "Masculine or Feminine\n"))
		if ui.is_dwarven(ancestry) and dwarven_qualified(scores, is_pc):
			if not is_pc and (scores[0] < 17 or (scores[0] < 18 and is_masc)):
				scores[0] = scores[0] + 1
			if scores[0] > 17 and not is_masc:
				print("STRENGTH: {} is too high for a feminine dwarf, reducing to 17".format(scores[0]),
				      file=sys.stderr)
				scores[0] = 17
			if scores[3] > 17:
				print("DEXTERITY: {} is too high for a dwarf, reducing to 17".format(scores[3]),
				      file=sys.stderr)
				scores[3] = 17
			scores[4] = scores[4] + 1
			if not is_pc and scores[4] < 19:
				scores[4] = scores[4] + 1
			if not is_pc and int(scores[5]) > 3:
				scores[5] = int(scores[5]) - 1
			if int(scores[5]) > 16:
				print("CHARISMA: {} is too high for a dwarf, reducing to 16 for non-dwarves".format(scores[5]),
				      file=sys.stderr)
				scores[5] = "16 ({})".format(scores[5])
			else:
				scores[5] = "{} ({})".format(scores[5] - 1, scores[5])
			break
		elif ui.is_elven(ancestry) and elven_qualified(ancestry, scores, is_pc):
			if scores[0] > 16 and not is_masc:
				print("STRENGTH: {} is too high for a feminine elf, reducing to 16".format(scores[0]),
				      file=sys.stderr)
				scores[0] = 16
			if not is_pc and scores[1] < 18:
				scores[1] = scores[1] + 1
			scores[3] = scores[3] + 1
			if not is_pc and scores[3] < 19:
				scores[3] = scores[3] + 1
			scores[4] = scores[4] - 1
			break
		elif ui.is_gnome(ancestry) and gnome_qualified(scores, is_pc):
			if scores[0] > 15 and not is_masc:
				print("STRENGTH: {} is too high for a feminine gnome, reducing to 15".format(scores[0]),
				      file=sys.stderr)
				scores[0] = 15
			if not is_pc and scores[2] < 18:
				scores[2] = scores[2] + 1
			if not is_pc and scores[4] < 18:
				scores[4] = scores[4] + 1
			if not is_pc and scores[5] > 3:
				scores[5] = scores[5] - 1
			break
		elif ui.is_half_elven(ancestry) and half_elven_qualified(scores):
			if scores[0] > 17 and not is_masc:
				print("STRENGTH: {} is too high for a feminine half-elf, reducing to 17".format(scores[0]),
				      file=sys.stderr)
				scores[0] = 17
			break
		elif ui.is_halfling(ancestry) and halfling_qualified(scores, is_pc):
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
			if not is_pc and scores[3] < 18:
				scores[3] = scores[3] + 1
			if not is_pc and scores[4] < 19:
				scores[4] = scores[4] + 1
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
			print("Invalid option for rolled ability scores or character type: {}\n".format(ancestry), file=sys.stderr)

	print("\nAdjusted scores:")
	ui.print_scores(scores)
	return ancestry, scores, is_masc

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
			ability = 0
			try:
				ability = int(input("Which ability is germane to their profession (1-7)?\n" \
						    "1. STRENGTH\n" \
						    "2. INTELLIGENCE\n" \
						    "3. WISDOM\n" \
						    "4. DEXTERITY\n" \
						    "5. CONSTITUTION\n" \
						    "6. CHARISMA\n" \
						    "7. No more abilities are germane\n"))
			except ValueError as e:
				if ui.is_strength(str(e)):
					ability = 1
				if ui.is_intelligence(str(e)):
					ability = 2
				if ui.is_wisdom(str(e)):
					ability = 3
				if ui.is_dexterity(str(e)):
					ability = 4
				if ui.is_constitution(str(e)):
					ability = 5
				if ui.is_charisma(str(e)):
					ability = 6
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

	print("\nInitial scores:")
	ui.print_scores(scores)

	return scores, method < 5

def mod_avg_height(height):
	avg_height_mod = dice.d100()
	if height < 60:
		if avg_height_mod < 31:
			height = height - dice.d3() * .5
		elif avg_height_mod > 70:
			height = height + dice.d3() * .5
	else:
		if avg_height_mod < 31:
			height = height - dice.d4() * .5
		elif avg_height_mod > 70:
			height = height + dice.d4() * .5
	return height

def mod_avg_weight(weight):
	avg_weight_mod = dice.d100()
	if weight <= 100:
		if avg_weight_mod < 31:
			weight = weight - dice.d4()
		elif avg_weight_mod > 70:
			weight = weight + dice.d4()
	else:
		if avg_weight_mod < 31:
			weight = weight - dice.d8()
		elif avg_weight_mod > 70:
			weight = weight + dice.d8()
	return weight

def get_dwarf_height_and_weight(is_masc, height_roll, weight_roll):
	height = 46
	weight = 120
	if is_masc:
		height = 48
		weight = 150

	if height_roll < 16:
		height = height - dice.d4()
	elif height_roll > 80:
		if is_masc:
			height = height + dice.d6()
		else:
			height = height + dice.d4()
	else:
		height = mod_avg_height(height)

	if weight_roll < 21:
		weight = weight - dice.d(2, 8)
	elif weight_roll > 65:
		if is_masc:
			weight = weight + dice.d(2, 12)
		else:
			weight = weight + dice.d(2, 10)
	else:
		weight = mod_avg_weight(weight)

	return height, weight

def get_elf_height_and_weight(is_masc, height_roll, weight_roll):
	height = 54
	weight = 80
	if is_masc:
		height = 60
		weight = 100

	if height_roll < 11:
		height = height - dice.d4()
	elif height_roll > 80:
		height = height + dice.d6()
	else:
		height = mod_avg_height(height)

	if weight_roll < 16:
		weight = weight - dice.d10()
	elif weight_roll > 90:
		if is_masc:
			weight = weight + dice.d20()
		else:
			weight = weight + dice.d(2, 6)
	else:
		weight = mod_avg_weight(weight)

	return height, weight

def get_gnome_height_and_weight(is_masc, height_roll, weight_roll):
	height = 39
	weight = 75
	if is_masc:
		height = 42
		weight = 80

	if height_roll < 21:
		height = height - dice.d3()
	elif height_roll > 85:
		height = height + dice.d3()
	else:
		height = mod_avg_height(height)

	if weight_roll < 21:
		if is_masc:
			weight = weight - dice.d(2, 4)
		else:
			weight = weight - dice.d8()
	elif weight_roll > 75:
		if is_masc:
			weight = weight + dice.d(2, 6)
		else:
			weight = weight + dice.d8()
	else:
		weight = mod_avg_weight(weight)

	return height, weight

def get_half_elf_height_and_weight(is_masc, height_roll, weight_roll):
	height = 62
	weight = 100
	if is_masc:
		height = 66
		weight = 130

	if height_roll < 36:
		height = height - dice.d6()
	elif height_roll > 90:
		height = height + dice.d6()
	else:
		height = mod_avg_height(height)

	if weight_roll < 21:
		if is_masc:
			weight = weight - dice.d20()
		else:
			weight = weight - dice.d12()
	elif weight_roll > 85:
		if is_masc:
			weight = weight + dice.d20()
		else:
			weight = weight + dice.d(2, 8)
	else:
		weight = mod_avg_weight(weight)

	return height, weight

def get_halfling_height_and_weight(is_masc, height_roll, weight_roll):
	height = 33
	weight = 50
	if is_masc:
		height = 36
		weight = 60

	if height_roll < 11:
		height = height - dice.d3()
	elif height_roll > 90:
		if is_masc:
			height = height + dice.d6()
		else:
			height = height + dice.d3()
	else:
		height = mod_avg_height(height)

	if weight_roll < 11:
		weight = weight - dice.d(2, 4)
	elif weight_roll > 50:
		if is_masc:
			weight = weight + dice.d(2, 6)
		else:
			weight = weight + dice.d(2, 4)
	else:
		weight = mod_avg_weight(weight)

	return height, weight

def get_half_orc_height_and_weight(is_masc, height_roll, weight_roll):
	height = 62
	weight = 120
	if is_masc:
		height = 66
		weight = 150

	if height_roll < 46:
		if is_masc:
			height = height - dice.d4()
		else:
			height = height - dice.d3()
	elif height_roll > 75:
		if is_masc:
			height = height + dice.d4()
		else:
			height = height + dice.d3()
	else:
		height = mod_avg_height(height)

	if weight_roll < 31:
		if is_masc:
			weight = weight - dice.d(2, 8)
		else:
			weight = weight - dice.d(3, 6)
	elif weight_roll > 55:
		if is_masc:
			weight = weight + dice.d(4, 10)
		else:
			weight = weight + dice.d(4, 8)
	else:
		weight = mod_avg_weight(weight)

	return height, weight

def get_human_height_and_weight(is_pc, is_masc, height_roll, weight_roll):
	height = 66
	weight = 130
	if is_masc:
		height = 72
		weight = 175

	using_upper_limits = True
	if is_pc:
		if ui.is_negative(input("Is this PC possibly at the upper limits of human height/weight?\n")):
			using_upper_limits = False

	if height_roll < 21:
		if is_masc:
			height = height - dice.d12()
		else:
			height = height - dice.d6()
	elif height_roll > 80:
		if is_masc and using_upper_limits:
			height = height + dice.d(2, 10)
		elif is_masc:
			height = height + dice.d12()
		elif using_upper_limits:
			height = height + dice.d(2, 6)
		else:
			height = height + dice.d8()
	else:
		height = mod_avg_height(height)

	if weight_roll < 26:
		if is_masc:
			weight = weight - dice.d(3, 12)
		else:
			weight = weight - dice.d(3, 10)
	elif weight_roll > 75:
		if is_masc and using_upper_limits:
			weight = weight + dice.d(10, 20)
		elif is_masc:
			weight = weight + dice.d(5, 12)
		elif using_upper_limits:
			weight = weight + dice.d(10, 12)
		else:
			weight = weight + dice.d(4, 12)
	else:
		weight = mod_avg_weight(weight)

	return height, weight

def generate_height_and_weight(ancestry, is_pc, is_masc):
	height = 0
	weight = 0
	height_roll = dice.d100()
	weight_roll = dice.d100()
	if ui.is_dwarven(ancestry):
		height, weight = get_dwarf_height_and_weight(is_masc, height_roll, weight_roll)
	elif ui.is_elven(ancestry):
		height, weight = get_elf_height_and_weight(is_masc, height_roll, weight_roll)
	elif ui.is_gnome(ancestry):
		height, weight = get_gnome_height_and_weight(is_masc, height_roll, weight_roll)
	elif ui.is_half_elven(ancestry):
		height, weight = get_half_elf_height_and_weight(is_masc, height_roll, weight_roll)
	elif ui.is_halfling(ancestry):
		height, weight = get_halfling_height_and_weight(is_masc, height_roll, weight_roll)
	elif ui.is_half_orc(ancestry):
		height, weight = get_half_orc_height_and_weight(is_masc, height_roll, weight_roll)
	elif ui.is_human(ancestry):
		height, weight = get_human_height_and_weight(is_pc, is_masc, height_roll, weight_roll)
	else:
		print("Unknown ancestry: {}, unable to generate height/weight".format(ancestry), \
		      sys.stderr)
	ui.print_height_and_weight(height, weight)
	return height, weight

def get_strength(scores):
	if isinstance(scores[0], str):
		return int(re.search(r'\d+', scores[0]).group())
	return int(scores[0])

def get_charisma(scores):
	if isinstance(scores[5], str):
		return int(re.search(r'\d+', scores[5]).group())
	return int(scores[5])

def get_possible_classes(ancestry, is_pc, scores):
	possible_classes = []
	if ui.is_dwarven(ancestry):
		if not is_pc:
			possible_classes.append("cleric")
		possible_classes.extend(["fighter", "thief", "assassin", "fighter/thief"])
	elif ui.is_elven(ancestry):
		if not is_pc:
			possible_classes.append("cleric")
		possible_classes.extend(["fighter", "magic-user", "thief", "assassin", \
					 "fighter/magic-user", "fighter/thief", \
					 "magic-user/thief", "fighter/magic-user/thief"])
	elif ui.is_gnome(ancestry):
		if not is_pc:
			possible_classes.append("cleric")
		possible_classes.extend(["fighter", "illusionist", "thief", "assassin", \
					 "fighter/illusionist", "fighter/thief", \
					 "figher/assassin", "illusionist/thief", \
					 "illusionist/assassin"])
	elif ui.is_half_elven(ancestry):
		possible_classes.extend(["bard", "cleric", "druid", "fighter", "ranger", \
					 "magic-user", "thief", "assassin", \
					 "cleric/fighter", "cleric/ranger", \
					 "cleric/magic-user", "fighter/magic-user", \
					 "fighter/thief", "magic-user/thief", \
					 "cleric/fighter/magic-user", \
					 "fighter/magic-user/thief"])
	elif ui.is_halfling(ancestry):
		if not is_pc:
			possible_classes.append("druid")
		possible_classes.extend(["fighter", "thief", "fighter/thief"])
	elif ui.is_half_orc(ancestry):
		possible_classes.extend(["cleric", "fighter", "thief", "assassin", \
					 "cleric/fighter", "cleric/thief", \
					 "cleric/assassin", "fighter/thief", \
					 "fighter/assassin"])
	elif ui.is_human(ancestry):
		possible_classes.extend(["bard", "cleric", "druid", "fighter", "paladin", "ranger", \
					 "magic-user", "illusionist", "thief", "assassin", \
					 "monk"])
	else:
		print("Invalid ancestry: {}\n".format(ancestry), file=sys.stderr)

	if not is_pc:
		possible_classes.extend(["laborer", "mercenary", "merchant", "trader"])

	if (scores[0] < 15 or scores[1] < 12 or scores[2] < 15 or \
	    scores[3] < 15 or scores[4] < 10 or scores[5] < 15) and \
	    "bard" in possible_classes:
		possible_classes.remove("bard")
	if is_pc and scores[2] < 9 and "cleric" in possible_classes:
		possible_classes.remove("cleric")
	if is_pc and scores[2] < 13 and ui.is_half_elven(ancestry):
		possible_classes.remove("cleric/fighter")
		possible_classes.remove("cleric/ranger")
		possible_classes.remove("cleric/magic-user")
		possible_classes.remove("cleric/figher/magic-user")
	elif is_pc and scores[2] < 9 and ui.is_half_orc(ancestry):
		possible_classes.remove("cleric/fighter")
		possible_classes.remove("cleric/thief")
		possible_classes.remove("cleric/assassin")
	if ((is_pc and (scores[2] < 12 or get_charisma(scores) < 15)) or \
		   (not is_pc and (scores[2] < 12 or get_charisma(scores) < 14))) and \
		   "druid" in possible_classes:
		possible_classes.remove("druid")
	if is_pc and (scores[0] < 9 or scores[4] < 7) and "fighter" in possible_classes:
		for class_option in possible_classes:
			if "fighter" in class_option:
				possible_classes.remove(class_option)
	if ((is_pc and (scores[0] < 13 or scores[1] < 13 or scores[2] < 14 or scores[4] < 14)) or \
		   (not is_pc and scores[2] < 12)) and "ranger" in possible_classes:
		for class_option in possible_classes:
			if "ranger" in class_option:
				# NPC cleric/ranger could have 10 Wis + 2 from cleric
				if not is_pc and scores[2] >= 10 and "cleric" in class_option:
					continue
				possible_classes.remove(class_option)
	if ((is_pc and (scores[0] < 12 or scores[1] < 9 or scores[2] < 13 or scores[4] < 9 or get_charisma(scores) < 17)) or \
		   (not is_pc and get_charisma(scores) < 17)) and "paladin" in possible_classes:
		possible_classes.remove("paladin")
	if is_pc and (scores[1] < 9 or scores[3] < 6) and "magic-user" in possible_classes:
		for class_option in possible_classes:
			if "magic-user" in class_option:
				possible_classes.remove(class_option)
	if ((is_pc and (scores[1] < 15 or scores[3] < 16)) or \
		   (not is_pc and (scores[1] < 15 or scores[3] < 15))) and \
		   "illusionist" in possible_classes:
		for class_option in possible_classes:
			if "illusionist" in class_option:
				# NPC illusionist/(thief or assassin) could have 14 Int + 1 and/or 13 Dex + 2
				if not is_pc and scores[1] >= 14 and scores[3] >= 13 and \
					     ("thief" in class_option or "assassin" in class_option):
					continue
				possible_classes.remove(class_option)
	if is_pc and scores[3] < 9 and "thief" in possible_classes:
		for class_option in possible_classes:
			if "thief" in class_option:
				possible_classes.remove(class_option)
	if is_pc and (scores[0] < 12 or scores[1] < 11 or scores[3] < 12) and \
		   "assassin" in possible_classes:
		for class_option in possible_classes:
			if "assassin" in class_option:
				possible_classes.remove(class_option)
	if ((is_pc and (scores[0] < 15 or scores[2] < 15 or scores[3] < 15 or scores[4] < 11)) or \
		   (not is_pc and (scores[0] < 12 or scores[2] < 15 or scores[3] < 15))) and \
		   "monk" in possible_classes:
		possible_classes.remove("monk")
	if not is_pc and (scores[1] < 12 or get_charisma(scores) < 12):
		possible_classes.remove("merchant")
		possible_classes.remove("trader")

	return possible_classes

def adjust_strength(ancestry, is_masc, scores, mod):
	scores[0] = scores[0] + mod
	if ui.is_dwarven(ancestry):
		if is_masc:
			scores[0] = max(min(scores[0], 18), 8)
		else:
			scores[0] = max(min(scores[0], 17), 8)
	elif ui.is_elven(ancestry) and not is_masc:
		scores[0] = max(min(scores[0], 16), 3)
	elif ui.is_gnome(ancestry):
		if is_masc:
			scores[0] = max(min(scores[0], 18), 6)
		else:
			scores[0] = max(min(scores[0], 15), 6)
	elif ui.is_half_elven(ancestry) and not is_masc:
		scores[0] = max(min(scores[0], 17), 3)
	elif ui.is_halfling(ancestry):
		if is_masc:
			scores[0] = max(min(scores[0], 17), 6)
		else:
			scores[0] = max(min(scores[0], 14), 6)
	elif ui.is_half_orc(ancestry):
		scores[0] = max(min(scores[0], 18), 6)
	else:
		scores[0] = max(min(scores[0], 18), 3)
	return scores

def adjust_intelligence(ancestry, scores, mod):
	scores[1] = scores[1] + mod
	if ui.is_elven(ancestry):
		scores[1] = max(min(scores[1], 18), 8)
	elif ui.is_gnome(ancestry):
		scores[1] = max(min(scores[1], 18), 7)
	elif ui.is_half_elven(ancestry):
		scores[1] = max(min(scores[1], 18), 4)
	elif ui.is_halfling(ancestry):
		scores[1] = max(min(scores[1], 18), 6)
	elif ui.is_half_orc(ancestry):
		scores[1] = max(min(scores[1], 17), 3)
	else:
		scores[1] = max(min(scores[1], 18), 3)
	return scores

def adjust_wisdom(ancestry, scores, mod):
	scores[2] = scores[2] + mod
	if ui.is_halfling(ancestry):
		scores[2] = max(min(scores[2], 17), 3)
	elif ui.is_half_orc(ancestry):
		scores[2] = max(min(scores[2], 14), 3)
	else:
		scores[2] = max(min(scores[2], 18), 3)
	return scores

def adjust_dexterity(ancestry, scores, mod):
	scores[3] = scores[3] + mod
	if ui.is_dwarven(ancestry):
		scores[3] = max(min(scores[3], 17), 3)
	elif ui.is_elven(ancestry):
		scores[3] = max(min(scores[3], 19), 7)
	elif ui.is_half_elven(ancestry):
		scores[3] = max(min(scores[3], 18), 6)
	elif ui.is_halfling(ancestry):
		scores[3] = max(min(scores[3], 18), 8)
	elif ui.is_half_orc(ancestry):
		scores[3] = max(min(scores[3], 17), 3)
	else:
		scores[3] = max(min(scores[3], 18), 3)
	return scores

def adjust_constitution(ancestry, scores, mod):
	scores[4] = scores[4] + mod
	if ui.is_dwarven(ancestry):
		scores[4] = max(min(scores[4], 19), 12)
	elif ui.is_elven(ancestry):
		scores[4] = max(min(scores[4], 18), 6)
	elif ui.is_gnome(ancestry):
		scores[4] = max(min(scores[4], 18), 8)
	elif ui.is_half_elven(ancestry):
		scores[4] = max(min(scores[4], 18), 6)
	elif ui.is_halfling(ancestry):
		scores[4] = max(min(scores[4], 19), 10)
	elif ui.is_half_orc(ancestry):
		scores[4] = max(min(scores[4], 19), 13)
	else:
		scores[4] = max(min(scores[4], 18), 3)
	return scores

def get_class(ancestry, is_pc, is_masc, scores):
	char_class = "none"
	possible_classes = get_possible_classes(ancestry, is_pc, scores)
	while char_class not in possible_classes:
		char_class = input("Which class do they belong to?\n{}\n".format(possible_classes))
		if char_class not in possible_classes:
			print("Invalid class option: {}\n".format(char_class), file=sys.stderr)

	if not is_pc:
		if "cleric" in char_class:
			scores = adjust_wisdom(ancestry, scores, 2)
		if "fighter" in char_class or "ranger" in char_class or "paladin" in char_class:
			scores = adjust_strength(ancestry, is_masc, scores, 2)
			scores = adjust_constitution(ancestry, scores, 1)
		if "magic-user" in char_class:
			scores = adjust_intelligence(ancestry, scores, 2)
			scores = adjust_dexterity(ancestry, scores, 1)
		if "thief" in char_class or "assassin" in char_class:
			scores = adjust_intelligence(ancestry, scores, 1)
			scores = adjust_dexterity(ancestry, scores, 2)
		if "assassin" in char_class:
			scores = adjust_strength(ancestry, is_masc, scores, 1)
		if "laborer" == char_class:
			bonus = 0
			while bonus < 1 or bonus > 3:
				try:
					bonus = int(input("What STRENGTH bonus (1-3) does this laborer gain?\n"))
				except ValueError as e:
					print("Invalid bonus: {}\n".format(str(e)), file=sys.stderr)
			scores = adjust_strength(ancestry, is_masc, scores, bonus)
		if "mercenary" == char_class:
			scores = adjust_strength(ancestry, is_masc, scores, 1)
			scores = adjust_constitution(ancestry, scores, 3)

	return char_class, scores

def apply_age_mods(ancestry, age, char_class, is_masc, scores, young, mature, middle, old, venerable):
	if age >= young:
		scores = adjust_wisdom(ancestry, scores, -1)
		if scores[4] <= 17:
			scores = adjust_constitution(ancestry, scores, 1)
	if age >= mature:
		if get_strength(scores) <= 17:
			scores = adjust_strength(ancestry, is_masc, scores, 1)
			if get_strength(scores) == 18:
				scores = generate_exceptional_strength(ancestry, char_class, is_masc, scores)
		scores = adjust_wisdom(ancestry, scores, 1)
	if age >= middle:
		if get_strength(scores) == 18:
			exceptional = int(scores[0].split("/")[1]) / 2
			scores[0] = "18/{}".format(exceptional)
		else:
			scores = adjust_strength(ancestry, is_masc, scores, -1)
		scores = adjust_constitution(ancestry, scores, -1)
		if scores[1] <= 17:
			scores = adjust_intelligence(ancestry, scores, 1)
		scores = adjust_wisdom(ancestry, scores, 1)
	if age >= old:
		scores = adjust_strength(ancestry, is_masc, scores, -2)
		scores = adjust_dexterity(ancestry, scores, -2)
		scores = adjust_constitution(ancestry, scores, -1)
		scores = adjust_wisdom(ancestry, scores, 1)
	if age >= venerable:
		scores = adjust_strength(ancestry, is_masc, scores, -1)
		scores = adjust_dexterity(ancestry, scores, -1)
		scores = adjust_constitution(ancestry, scores, -1)
		if scores[1] <= 17:
			scores = adjust_intelligence(ancestry, scores, 1)
		scores = adjust_wisdom(ancestry, scores, 1)
	return scores

def generate_dwarven_age(char_class):
	age = 0
	if "cleric" in char_class:
		age = 250
		if "cleric" == char_class:
			age = age + dice.d(2, 20)
		else:
			age = age + 40
	elif "thief" in char_class or "assassin" in char_class:
		age = 75
		if "thief" == char_class or "assassin" == char_class:
			age = age + dice.d(3, 6)
		else:
			age = age + 18
	elif "fighter" in char_class:
		age = 40 + dice.d(5, 4)

	return age

def generate_elven_age(char_class):
	age = 0
	if "cleric" in char_class:
		age = 500
		if "cleric" == char_class:
			age = age + dice.d(10, 10)
		else:
			age = age + 100
	elif "magic-user" in char_class:
		age = 150
		if "magic-user" == char_class:
			age = age + dice.d(5, 6)
		else:
			age = age + 30
	elif "fighter" in char_class:
		age = 130
		if "fighter" == char_class:
			age = age + dice.d(5, 6)
		else:
			age = age + 30
	elif "thief" in char_class or "assassin" in char_class:
		age = 100 + dice.d(5, 6)

	return age

def generate_gnome_age(char_class):
	age = 0
	if "cleric" in char_class:
		age = 300
		if "cleric" == char_class:
			age = age + dice.d(3, 12)
		else:
			age = age + 36
	elif "illusionist" in char_class:
		age = 100
		if "illusionist" == char_class:
			age = age + dice.d(2, 12)
		else:
			age = age + 24
	elif "thief" in char_class or "assassin" in char_class:
		age = 80
		if "thief" == char_class or "assassin" == char_class:
			age = age + dice.d(5, 4)
		else:
			age = age + 20
	elif "fighter" in char_class:
		age = 60 + dice.d(5, 4)

	return age

def generate_half_elven_age(char_class):
	age = 0
	if "cleric" in char_class or "druid" in char_class:
		age = 40
		if "cleric" == char_class or "druid" == char_class:
			age = age + dice.d(2, 4)
		else:
			age = age + 8
	elif "magic-user" in char_class:
		age = 30
		if "magic-user" == char_class:
			age = age + dice.d(2, 8)
		else:
			age = age + 16
	elif "thief" in char_class or "assassin" in char_class:
		age = 22
		if "thief" == char_class or "assassin" == char_class:
			age = age + dice.d(3, 8)
		else:
			age = age + 24
	elif "bard" in char_class or "fighter" in char_class or "ranger" in char_class:
		age = 22 + dice.d(3, 4)

	return age

def generate_halfling_age(char_class):
	age = 0
	# The rules don't cover this, so I'm deciding that 60+4d4 is appropriate:
	# - Other NPC Cleric options generally give middle-aged results
	# - Elves of various types could be Mature, so that's also allowed here
	if "druid" in char_class:
		age = 60
		if "druid" == char_class:
			age = age + dice.d(4, 4)
		else:
			age = age + 16
	elif "thief" in char_class:
		age = 40
		if "thief" == char_class:
			age = age + dice.d(2, 4)
		else:
			age = age + 8
	elif "fighter" in char_class:
		age = 20 + dice.d(3, 4)

	return age

def generate_half_orc_age(char_class):
	age = 0
	if "thief" in char_class or "assassin" in char_class:
		age = 20
		if "thief" == char_class or "assassin" == char_class:
			age = age + dice.d(2, 4)
		else:
			age = age + 8
	elif "cleric" in char_class:
		age = 20
		if "cleric" == char_class:
			age = age + dice.d(1, 4)
		else:
			age = age + 4
	elif "fighter" in char_class:
		age = 13 + dice.d(1, 4)

	return age

def generate_human_age(char_class):
	age = 0
	if "illusionist" == char_class:
		age = 30 + dice.d(1, 6)
	elif "magic-user" == char_class:
		age = 24 + dice.d(2, 8)
	elif "monk" == char_class:
		age = 21 + dice.d(1, 4)
	elif "assassin" == char_class or "ranger" == char_class:
		age = 20 + dice.d(1, 4)
	elif "cleric" == char_class or "druid" == char_class or "thief" == char_class:
		age = 18 + dice.d(1, 4)
	elif "paladin" == char_class:
		age = 17 + dice.d(1, 4)
	elif "bard" == char_class or "fighter" == char_class:
		age = 15 + dice.d(1, 4)

	return age

def apply_dwarven_age(ancestry, age, char_class, is_masc, scores):
	if ui.is_mountain_dwarf(ancestry):
		scores = apply_age_mods(ancestry, age, char_class, is_masc, scores, \
					40, 61, 176, 276, 401)
	else:
		scores = apply_age_mods(ancestry, age, char_class, is_masc, scores, \
					35, 51, 151, 251, 351)
	return scores

def apply_elven_age(ancestry, age, char_class, is_masc, scores):
	if ui.is_aquatic_elf(ancestry):
		scores = apply_age_mods(ancestry, age, char_class, is_masc, scores, \
					75, 151, 451, 701, 1001)
	elif ui.is_drow_elf(ancestry):
		scores = apply_age_mods(ancestry, age, char_class, is_masc, scores, \
					50, 101, 401, 601, 801)
	elif ui.is_gray_elf(ancestry):
		scores = apply_age_mods(ancestry, age, char_class, is_masc, scores, \
					150, 251, 651, 1001, 1501)
	elif ui.is_high_elf(ancestry):
		scores = apply_age_mods(ancestry, age, char_class, is_masc, scores, \
					100, 176, 551, 876, 1201)
	elif ui.is_wood_elf(ancestry):
		scores = apply_age_mods(ancestry, age, char_class, is_masc, scores, \
					75, 151, 501, 801, 1101)
	return scores

def apply_gnome_age(ancestry, age, char_class, is_masc, scores):
	return apply_age_mods(ancestry, age, char_class, is_masc, scores, \
			      50, 91, 301, 451, 601)

def apply_half_elven_age(ancestry, age, char_class, is_masc, scores):
	return apply_age_mods(ancestry, age, char_class, is_masc, scores, \
			      24, 41, 101, 176, 251)

def apply_halfling_age(ancestry, age, char_class, is_masc, scores):
	return apply_age_mods(ancestry, age, char_class, is_masc, scores, \
			      22, 34, 69, 102, 145)

def apply_half_orc_age(ancestry, age, char_class, is_masc, scores):
	return apply_age_mods(ancestry, age, char_class, is_masc, scores, \
			      12, 16, 31, 46, 61)

def apply_human_age(ancestry, age, char_class, is_masc, scores):
	return apply_age_mods(ancestry, age, char_class, is_masc, scores, \
			      14, 21, 41, 61, 91)

def generate_age(ancestry, is_pc, char_class, is_masc, scores):
	age = 0
	if not is_pc and (char_class == "laborer" or char_class == "mercenary" or char_class == "merchant" \
	   or char_class == "trader" or ui.is_negative(input("Is this NPC a henchman or otherwise using a rolled age?\n"))):
		age = int(input("How many years old is this character?\n"))
	else:
		if ui.is_dwarven(ancestry):
			age = generate_dwarven_age(char_class)
		elif ui.is_elven(ancestry):
			age = generate_elven_age(char_class)
		elif ui.is_gnome(ancestry):
			age = generate_gnome_age(char_class)
		elif ui.is_half_elven(ancestry):
			age = generate_half_elven_age(char_class)
		elif ui.is_halfling(ancestry):
			age = generate_halfling_age(char_class)
		elif ui.is_half_orc(ancestry):
			age = generate_half_orc_age(char_class)
		elif ui.is_human(ancestry):
			age = generate_human_age(char_class)

	if ui.is_dwarven(ancestry):
		scores = apply_dwarven_age(ancestry, age, char_class, is_masc, scores)
	elif ui.is_elven(ancestry):
		scores = apply_elven_age(ancestry, age, char_class, is_masc, scores)
	elif ui.is_gnome(ancestry):
		scores = apply_gnome_age(ancestry, age, char_class, is_masc, scores)
	elif ui.is_half_elven(ancestry):
		scores = apply_half_elven_age(ancestry, age, char_class, is_masc, scores)
	elif ui.is_halfling(ancestry):
		scores = apply_halfling_age(ancestry, age, char_class, is_masc, scores)
	elif ui.is_half_orc(ancestry):
		scores = apply_half_orc_age(ancestry, age, char_class, is_masc, scores)
	elif ui.is_human(ancestry):
		scores = apply_human_age(ancestry, age, char_class, is_masc, scores)

	print("Age: {} years".format(age))
	return age, scores

def generate_exceptional_strength(ancestry, char_class, is_masc, scores):
	if int(scores[0]) == 18 and "fighter" in char_class:
		percent = dice.d100()
		if (not is_masc and ui.is_human(ancestry)) or ui.is_gnome(ancestry):
			percent = min(percent, 50)
		elif (not is_masc and ui.is_half_orc(ancestry)) or ui.is_elven(ancestry):
			percent = min(percent, 75)
		elif ui.is_half_elven(ancestry):
			percent = min(percent, 90)
		elif ui.is_dwarven(ancestry) or ui.is_half_orc(ancestry):
			percent = min(percent, 99)
		percent = percent % 100
		scores[0] = "18/{:02}".format(percent)

	print("\nAdjusted scores:")
	ui.print_scores(scores)
	return scores

def main():
	#scores = [STRENGTH, INTELLIGENCE, WISDOM, DEXTERITY, CONSTITUTION, CHARISMA]
	scores, is_pc = generate_scores()
	ancestry, scores, is_masc = get_ancestry(scores, is_pc)
	height, weight = generate_height_and_weight(ancestry, is_pc, is_masc)
	char_class, scores = get_class(ancestry, is_pc, is_masc, scores)
	age, scores  = generate_age(ancestry, is_pc, char_class, is_masc, scores)
	if not isinstance(scores[0], str):
		scores = generate_exceptional_strength(ancestry, char_class, is_masc, scores)

	ui.display_character(ancestry, scores, is_masc, height, weight, char_class, age)
	return 0

if __name__ == '__main__':
	sys.exit(main())