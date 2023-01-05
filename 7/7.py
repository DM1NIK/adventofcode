import timeit


def main():
	file = open("./input")

	lines = file.read().splitlines()
	current = None
	for i in range(len(lines)):
		line = lines[i]
		# command
		if line.startswith("$"):
			if line.startswith("$ cd .."):
				current = current.move_up()
			elif line.startswith("$ cd"):
				new_dir = line.replace("$ cd ", "")
				if current is None:
					current = Node(new_dir, None)
					current.root = current
				else:
					current = current.container.get(new_dir)
		else:
			if line.startswith("dir"):
				dir_name = line.replace("dir ", "")
				if not current.container.__contains__(dir_name):
					current.container[dir_name] = Node(dir_name, current, current.root)
			else:
				f = line.split(" ")
				if not current.container.__contains__(f[1]):
					current.files[f[1]] = int(f[0])
	total, limit_total = current.root.get_total_size2(0, 0)
	needed = 30000000
	left = 70000000 - total
	total, limit_total = current.root.get_total_size2(total, abs(needed-left))
	print(limit_total)


class Node:

	def __init__(self, name, parent, root=None):
		self.name = name
		self.parent = parent
		self.container = {}
		self.files = {}
		self.root = root

	def move_up(self):
		if self.parent is None:
			return self
		return self.parent

	def get_total_size2(self, limit_total, limit):
		total = sum(self.files.values())
		print(limit_total)
		if self.container is not None:
			for v in self.container.values():
				temp_total, limit_total = v.get_total_size2(limit_total, limit)
				total += temp_total

		if limit < total < limit_total:
			limit_total = total
		print(f"{self.name}: {total}")
		return total, limit_total

	def get_total_size(self, limit_total, limit=100000):
		total = sum(self.files.values())

		if self.container is not None:
			for v in self.container.values():
				temp_total, limit_total = v.get_total_size(limit_total)
				total += temp_total

		if total < limit:
			limit_total += total
		print(f"{self.name}: {total}")
		return total, limit_total

if __name__ == "__main__":
	print("Dominik1", timeit.timeit("main()", setup="from __main__ import main", number=1000))
