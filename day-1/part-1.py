def read_file(file_path):
    """Read directions from input file."""
    directions = []
    with open(file_path, "r") as f:
        for line in f.read().splitlines():
            directions.append((line[0], int(line[1:], 10)))
    return directions


def index_wrapping(index):
    """Wrap index around a circular array of size 100."""
    if index == -1:
        return 99
    if index == 100:
        return 0
    return index


def move(direction, count, index):
    """Move along circular array and return final index."""
    movement = 1
    if direction == "L":
        movement = -1

    for i in range(count):
        index += movement
        index = index_wrapping(index)
    return index


def main():
    zero_count = 0
    current_index = 50
    directions = read_file("input.txt")

    for direction in directions:
        current_index = move(direction[0], direction[1], current_index)
        if current_index == 0:
            zero_count += 1

    print(f"Zero Count: {zero_count}")


if __name__ == "__main__":
    main()
