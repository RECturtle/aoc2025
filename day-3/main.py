import sys


def part1(joltage):
    tens_slice = joltage[:-1]
    tens_max_index = tens_slice.index(max(tens_slice))
    ones_max = max(joltage[tens_max_index + 1 :])

    return int(joltage[tens_max_index] + ones_max)


def part2(joltage):
    num = []
    remaining_skips = len(joltage) - 12
    start_index = 0

    while remaining_skips != 0 and len(num) < 12:
        search_window_size = remaining_skips + 1
        search_slice = joltage[start_index : start_index + search_window_size]
        index_of_max_num_in_slice = search_slice.index(max(search_slice))

        max_num_index = start_index + index_of_max_num_in_slice
        remaining_skips -= max_num_index - start_index
        start_index = max_num_index + 1
        num.append(joltage[max_num_index])

    if len(num) < 12:
        num.extend(joltage[start_index:])

    return int("".join(num))


def main():
    part_1_total = 0
    part_2_total = 0
    with open(sys.argv[1], "r") as f:
        batteries = f.read().splitlines()

    for battery in batteries:
        joltage = list(battery)
        part_1_total += part1(joltage)
        part_2_total += part2(joltage)

    print(f"Part 1 Total: {part_1_total}")
    print(f"Part 2 Total: {part_2_total}")


if __name__ == "__main__":
    main()
