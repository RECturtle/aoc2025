import sys


def read_file(file_path):
    """Read directions from input file."""
    directions = []
    with open(file_path, "r") as f:
        for line in f.read().splitlines():
            directions.append((line[0], int(line[1:])))
    return directions


def index_wrapping(index):
    """Wrap index around a circular array of size 100."""
    if index == -1:
        return 99
    if index == 100:
        return 0
    return index


def move(direction, count, index, counter):
    """Move along circular array and return final index."""
    movement = 1
    if direction == "L":
        movement = -1

    for _ in range(count):
        index += movement
        index = index_wrapping(index)
        if index == 0:
            counter += 1
    return index, counter


def main():
    p1_zero_count = 0
    p2_zero_count = 0
    current_index = 50
    directions = read_file(sys.argv[1])

    for direction, count in directions:
        current_index, p2_zero_count = move(
            direction, count, current_index, p2_zero_count
        )
        if current_index == 0:
            p1_zero_count += 1

    print(f"Part 1 Zero Count: {p1_zero_count}")
    print(f"Part 2 Zero Count: {p2_zero_count}")


if __name__ == "__main__":
    main()
