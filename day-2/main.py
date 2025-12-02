import sys


def invalid_id(str_num, length):
    for pattern_length in range(1, length // 2):
        if length % pattern_length == 0:
            if str_num[:pattern_length] * (length // pattern_length) == str_num:
                return True
    return False


def main():
    part_1_counter = 0
    part_2_counter = 0

    with open(sys.argv[1], "r") as f:
        input = f.read().strip().split(",")

    ranges = [r.split("-") for r in input]

    for r in ranges:
        for num in range(int(r[0]), int(r[1]) + 1):
            str_num = str(num)
            str_length = len(str_num)

            # part 1 check
            if str_length % 2 == 0:
                mid = str_length // 2
                if str_num[:mid] == str_num[mid:]:
                    part_1_counter += num

            # part 2 check
            if invalid_id(str_num, str_length):
                part_2_counter += num

    print(f"Part 1 Total: {part_1_counter}")
    print(f"Part 2 Total: {part_2_counter}")


if __name__ == "__main__":
    main()
