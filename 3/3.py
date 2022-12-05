import string


def main():
	file = open("./input")

	rows = file.read().splitlines()

	score = 0
	for i in range((len(rows)//3)):
		group = []
		for x in range(3):
			group.append(rows.pop(0))

		for c in group[0]:
			if c in group[1] and c in group[2]:
				group[1] = group[1].replace(c, "")
				group[2] = group[2].replace(c, "")
				if c in string.ascii_lowercase:
					score = score + string.ascii_lowercase.index(c) + 1
				else:
					score = score + string.ascii_uppercase.index(c) + 27

	print(score)





if __name__ == "__main__":
	main()