
def is_negative(option):
	return "no" in option or "n" in option or "No" in option or "N" in option

def is_ancestry(option):
	return is_dwarven(option) or is_elven(option) or is_gnome(option) or \
	       is_half_elven(option) or is_halfling(option) or is_half_orc(option) or \
	       is_human(option)

def is_strength(option):
	return "S" == option or "s" == option or "Str" in option or "str" in option

def is_intelligence(option):
	return "I" == option or "i" == option or "Int" in option or "int" in option

def is_wisdom(option):
	return "W" == option or "w" == option or "Wis" in option or "wis" in option

def is_dexterity(option):
	return "D" == option or "d" == option or "Dex" in option or "dex" in option

def is_constitution(option):
	return "Con" in option or "con" in option

def is_charisma(option):
	return "Cha" in option or "cha" in option or "Riz" in option or "riz" in option

def is_mountain_dwarf(option):
	return "Mountain" in option or "mountain" in option

def is_dwarven(option):
	return "Dwarven" in option or "dwarven" in option or "Dwarf" in option or "dwarf" in option

def is_aquatic_elf(option):
	return "Aquatic" in option or "aquatic" in option

def is_drow_elf(option):
	return "Drow" in option or "drow" in option

def is_gray_elf(option):
	return "Gray" in option or "gray" in option or "Grey" in option or "grey" in option

def is_high_elf(option):
	return "High" in option or "high" in option or \
	       "Elven" == option or "elven" == option or "Elf" == option or "elf" == option

def is_wood_elf(option):
	return "Wood" in option or "wood" in option

def is_elven(option):
	return ("Elven" in option or "elven" in option or "Elf" in option or "elf" in option) and \
	       (is_aquatic_elf(option) or is_drow_elf(option) or is_gray_elf(option) or \
	        is_high_elf(option) or is_wood_elf(option))

def is_gnome(option):
	return "Gnome" in option or "gnome" in option or "Gnomish" in option or "gnomish" in option

def is_half_elven(option):
	return "Half-Elven" in option or "Half-elven" in option or "half-elven" in option or \
	       "Half-Elf" in option or "Half-elf" in option or "half-elf" in option

def is_halfling(option):
	return "Halfling" in option or "halfling" in option

def is_half_orc(option):
	return "Half-Orc" in option or "Half-orc" in option or "half-orc" in option or \
	       "Half-Orcish" in option or "Half-orcish" in option or "half-orcish" in option

def is_human(option):
	return "Human" in option or "human" in option

def is_masc(option):
	return "Masculine" in option or "masculine" in option or "Masc" in option or \
	       "masc" in option or "M" == option or "m" == option

def print_scores(scores):
	print("STRENGTH | INTELLIGENCE | WISDOM | DEXTERITY | CONSTITUTION | CHARISMA")
	line = "{}    "
	if isinstance(scores[0], str):
		line = line + "| "
	elif scores[0] < 10:
		line = line + "    | "
	else:
		line = line + "   | "
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
	print(line.format(scores[0], scores[1], scores[2], scores[3], scores[4], scores[5]))
	print("----------------------------------------------------------------------\n")

def print_height_and_weight(height, weight):
	feet = int(height / 12)
	inches = height % 12
	print("Height: {}'' ({}' {}''), Weight: {} lbs.".format(height, feet, inches, weight))

def display_character(ancestry, scores, is_masc, height, weight, char_class, age):
	print("\nGenerated Character:")
	if is_masc:
		print("{} {} {}".format("Masculine", ancestry, char_class))
	else:
		print("{} {} {}".format("Feminine", ancestry, char_class))
	print_height_and_weight(height, weight)
	print("Age: {} years".format(age))
	print_scores(scores)