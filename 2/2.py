
def main():
	win = 6
	draw = 3
	score_map = {
		'A': 1,
		'B': 2,
		'C': 3
	}
	file = open("/Users/dmnk/PycharmProjects/adventofcode/2/input")

	win_condition = {
		'A': 'B',
		'B': 'C',
		'C': 'A'
	}
	lose_condition = {
		'A': 'C',
		'B': 'A',
		'C': 'B'
	}
	rounds = file.read().splitlines()
	score = 0
	for round in rounds:
		actions = round.split(" ")
		if actions[1] == 'Y':
			score = score + draw + score_map.get(actions[0])
		elif actions[1] == 'Z':
			score = score + win + score_map.get(win_condition.get(actions[0]))
		else:
			score = score + score_map.get(lose_condition.get(actions[0]))

	print(score)



if __name__ == "__main__":
	main()