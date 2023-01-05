
def main():
	file = open("./input")
	lines = file.read().splitlines()

	map = [[0]*400 for i in range(800)]

	pos_t = [0, 0]
	pos_h = [0, 0]
	for line in lines:
		command = line.split(" ")
		direction = command[0]
		steps = command[1]
		point = 1 if direction == "R" or direction == "U" else -1
		ax = 0 if direction == "L" or direction == "R" else 1
		for step in range(int(steps)):
			print(direction)
			pos_h[ax] = pos_h[ax] + point
			diff = (abs(pos_h[0]-pos_t[0]) > 1 or abs(pos_h[1]-pos_t[1]) > 1)
			if pos_t[ax] + point != pos_h[ax] and pos_t != pos_h and diff:
				pos_t[ax] = pos_t[ax] + point

			if pos_t[0] != pos_h[0] and pos_t[1] != pos_h[1] and diff:
				if direction == "D" or direction == "U":
					pos_t[0] = pos_h[0]
				else:
					pos_t[1] = pos_h[1]
			print(pos_t, pos_h)
			map[pos_t[0]][pos_t[1]] = map[pos_t[0]][pos_t[1]] + 1

	total = 0
	for submap in map:
		total = total + sum([1 for i in submap if i != 0])
	print(total)


if __name__ == "__main__":
	main()
	# 6522
