import timeit


def main():
	file = open("./input")

	lines = file.read().splitlines()

	map = [[e for e in lines[x]] for x in range(len(lines))]

	count = len(map[0]) + len(map[-1]) + 2*len(map) - 4
	for y in range(1, len(map) - 1):
		for x in range(1, len(map[y])-1):
			tree = map[y][x]
			alignment_y = [(1 if t < tree else 0) for t in [row[x] for row in map]]
			alignment_x = [(1 if t < tree else 0) for t in map[y]]
			if not (0 in alignment_y[y+1:] and 0 in alignment_y[:y] and 0 in alignment_x[x+1:] and 0 in alignment_x[:x]):
				count += 1

	return count


def main2():
	file = open("./input")

	lines = file.read().splitlines()

	map = [[e for e in lines[x]] for x in range(len(lines))]

	psenic_score = []
	for y in range(1, len(map) - 1):
		for x in range(1, len(map[y])-1):
			tree = map[y][x]
			alignment_y = list(next(iter(())) if t > tree else 1 for t in [row[x] for row in map])
			alignment_x = list(next(iter(())) if t > tree else 1 for t in map[y])

			left = alignment_x[:x]
			right = alignment_x[x+1:]
			up = alignment_y[:y]
			down = alignment_y[y+1:]

			check_left = 0 in left
			check_right = 0 in right
			check_bottom = 0 in down
			check_top = 0 in up

			psenic_score.append(
				(sum(alignment_y[y+1:alignment_y.index(0, y+1)]) + 1 if check_bottom else sum(down))
				*
				(sum(alignment_y[:alignment_y[y::-1].index(0)]) + 1 if check_top else sum(up))
				*
				(sum(alignment_x[x+1:alignment_x.index(0, x+1)]) + 1 if check_right else sum(right))
				*
				(sum(alignment_x[:alignment_x[x::-1].index(0)]) + 1 if check_left else sum(left))
			)


	return max(psenic_score)


def random():
	data = open("./input").read().split("\n")[:-1]

	data = [[int(y) for y in x] for x in data]
	visible = 0
	values = []

	for x in range(len(data[0])):
		for y in range(len(data)):
			height = data[y][x]
			distances = []
			isVisible = False

			if x == 0 or y == 0 or x == len(data[0]) - 1 or y == len(data) - 1:
				isVisible = True

			d = True
			for ix in range(1, x+1):
				if data[y][x-ix] >= height:
					d = False
					distances.append(ix)
					break

			if len(distances) < 1:
				distances.append(x)

			if d:
				isVisible = True

			d = True
			for iy in range(1, y+1):
				if data[y-iy][x] >= height:
					d = False
					distances.append(iy)
					break

			if len(distances) < 2:
				distances.append(y)

			if d:
				isVisible = True

			d = True
			for ix in range(1, len(data[0])-x):
				if data[y][x+ix] >= height:
					d = False
					distances.append(ix)
					break
			if d:
				isVisible = True

			if len(distances) < 3:
				distances.append(len(data[0])-x-1)

			d = True
			for iy in range(1, len(data)-y):
				if data[y+iy][x] >= height:
					d = False
					distances.append(iy)
					break

			if len(distances) < 4:
				distances.append(len(data[0])-y-1)

			if d:
				isVisible = True

			if isVisible:
				visible += 1

			s = 1
			for value in distances:
				s = s*value
			values.append(s)


if __name__ == "__main__":
	main2()
