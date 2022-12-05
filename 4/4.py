import string


def main():
	file = open("./input")

	rows = file.read().splitlines()

	counter = 0
	for row in rows:
		elves = row.split(",")
		elve1_range = list(map(int, elves[0].split("-")))
		elve2_range = list(map(int, elves[1].split("-")))
			# 40                20                  50           49
		if elve1_range[0] >= elve2_range[0] and elve1_range[1] >= elve2_range[1]:
			counter = counter + 1
		elif elve2_range[0] >= elve1_range[0] and elve2_range[1] <= elve1_range[1]:
			print(f"{elve2_range[0]} is bigger than {elve1_range[0]}: {elve2_range[0] >= elve1_range[0]}")
			counter = counter + 1

	print(counter)


def main2():
	file = open("./input")

	rows = file.read().splitlines()

	counter = 0
	for row in rows:
		elves = row.split(",")
		elve1_range = list(map(int, elves[0].split("-")))
		elve2_range = list(map(int, elves[1].split("-")))
		if elve2_range[0] <= elve1_range[0] <= elve2_range[1]:
			counter = counter + 1
		elif elve1_range[0] <= elve2_range[0] <= elve1_range[1]:
			counter = counter + 1

	print(counter)




if __name__ == "__main__":
	main2()