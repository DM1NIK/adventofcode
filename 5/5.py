
import timeit


def main():
	file, file2 = seperator()

	rows = file.splitlines()

	last = rows[-1]
	del rows[-1]

	all_crates = {}

	rows.reverse()
	for row in rows:
		for i in range(len(row)):
			if row[i] == "[":
				letter = i + 1
				crate_pos = last[letter]
				if all_crates.__contains__(crate_pos):
					all_crates[crate_pos].append(row[letter])
				else:
					all_crates[crate_pos] = [row[letter]]

	rows_move = file2.replace("move ", "").replace("from ", "").replace("to ", "").splitlines()

	for row in rows_move:
		set = row.split(" ")
		crate_count = set[0]
		pos_old = set[1]
		pos_new = set[2]
		old_crate = all_crates.get(pos_old)
		new_crate = all_crates.get(pos_new)
		for i in range(int(crate_count)):
			new_crate.append(old_crate[-1])
			del old_crate[-1]

	final = ""
	for k, v in all_crates.items():
		final += v[-1]
	return final


def main2():
	file, file2 = seperator()
	rows = file.splitlines()

	last = rows[-1]
	del rows[-1]

	all_crates = {}
	rows.reverse()
	for row in rows:
		for i in range(len(row)):
			if row[i] == "[":
				letter = i + 1
				crate_pos = last[letter]
				if all_crates.__contains__(crate_pos):
					all_crates[crate_pos].append(row[letter])
				else:
					all_crates[crate_pos] = [row[letter]]

	rows_move = file2.replace("move ", "").replace("from ", "").replace("to ", "").splitlines()

	for row in rows_move:
		set = row.split(" ")
		crate_count = set[0]
		pos_old = set[1]
		pos_new = set[2]
		old_crate = all_crates.get(pos_old)
		new_crate = all_crates.get(pos_new)
		new_set = []
		for i in range(int(crate_count)):
			new_crate.append(old_crate[-1])
			del old_crate[-1]
		new_set.reverse()

		new_crate.extend(new_set)

	final = ""
	for k, v in all_crates.items():
		final += v[-1]
	return final


def seperator():
	file = open("input")

	rows = file.read().splitlines()
	str1 = ""
	for i in range(len(rows)):
		row = rows[0]
		del rows[0]
		if row == '':
			break
		str1 += row + "\n"

	str2 = ""
	for i in range(len(rows)):
		row = rows[0]
		del rows[0]
		str2 += row + "\n"
	return str1, str2

def noah2():
	with open('input') as f:
		build_stack = True
		stacks = {}

		for line in f:
			line = line.rstrip()
			if len(line) == 0:
				continue

			if build_stack and line.replace(" ", "").isdigit():
				for k in stacks.keys():
					stacks[k] = stacks[k][::-1]

				build_stack = False
				continue

			if build_stack:
				index, i = 1, 1
				while index <= len(line) - 1:
					if i not in stacks.keys():
						stacks[i] = []

					container = line[index].strip()
					if len(container) == 1:
						stacks[i].append(container)

					i += 1
					index = 4 * i - 3

				continue

			command = [int(x) for x in line.split(" ") if x.isdigit()]
			stacks[command[2]].extend([stacks[command[1]].pop() for _ in range(command[0])][::-1])

		return ("".join([s[-1] for s in stacks.values()]))

def noah():
	with open('input') as f:
		build_stack = True
		stacks = {}

		for line in f:
			line = line.rstrip()
			if len(line) == 0:
				continue

			if build_stack and line.replace(" ", "").isdigit():
				for k in stacks.keys():
					stacks[k] = stacks[k][::-1]

				build_stack = False
				continue

			if build_stack:
				index, i = 1, 1
				while index <= len(line) - 1:
					if i not in stacks.keys():
						stacks[i] = []

					container = line[index].strip()
					if len(container) == 1:
						stacks[i].append(container)

					i += 1
					index = 4 * i - 3

				continue

			command = [int(x) for x in line.split(" ") if x.isdigit()]
			for i in range(command[0]):
				stacks[command[2]].append(stacks[command[1]].pop())

		return("".join([s[-1] for s in stacks.values()]))

if __name__ == "__main__":
	# measure the performance of the whole program or all the functions combined
	print("Noah1", timeit.timeit("noah()", setup="from __main__ import noah", number=1000))
	print("Noah2", timeit.timeit("noah2()", setup="from __main__ import noah2", number=1000))
	print("Dominik1", timeit.timeit("main()", setup="from __main__ import main", number=1000))
	print("Dominik2", timeit.timeit("main2()", setup="from __main__ import main2", number=1000))
