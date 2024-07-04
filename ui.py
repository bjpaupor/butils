
def is_negative(option):
	return "no" in option or "n" in option or "No" in option or "N" in option

def is_ancestry(option):
	return is_dwarven(option) or is_elven(option) or is_gnome(option) or \
	       is_half_elven(option) or is_halfling(option) or is_half_orc(option) or \
	       is_human(option)

def is_dwarven(option):
	return "Dwarven" in option or "dwarven" in option or "Dwarf" in option or "dwarf" in option

# equal to avoid miscompare with Half-Elven characters
def is_elven(option):
	return "Elven" == option or "elven" == option or "Elf" == option or "elf" == option

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
	line = "{}       "
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
	print(line.format(scores[0], scores[1], scores[2], scores[3], scores[4], scores[5]))
	print("----------------------------------------------------------------------\n")