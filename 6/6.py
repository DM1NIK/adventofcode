import timeit


def main():
	file = open("./input")
	line = file.read()
	for i in range(len(line)):
		part_list = line[i:i+14].rsplit()
		if len([x for x in part_list if part_list.count(x) == 1]) == 14:
			return i + 14


if __name__ == "__main__":
	print("Dominik1", timeit.timeit("main()", setup="from __main__ import main", number=1000))
