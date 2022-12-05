# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    file = open("input")
    list_cal = file.read().splitlines()
    start_index = 0
    end_index = -1
    max_cal = 0
    all_cal = []
    for i in range(list_cal.count("")):
        # find next empty
        try:
            start_index = list_cal.index("", start_index + 1)
            end_index = list_cal.index("", start_index + 1)
        except ValueError:
            temp = list(map(int, list_cal[start_index+1:]))
            new_sum = sum(temp)
            all_cal.append(new_sum)


        temp = list(map(int, list_cal[start_index+1:end_index]))
        new_sum = sum(temp)
        all_cal.append(new_sum)

    all_cal.sort()

    print(sum(all_cal[-3:]))


if __name__ == '__main__':
    main()

