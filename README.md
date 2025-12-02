# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Structure

``` text
.
├── pyproject.toml  # uv project configuration
├── day-N/
│   ├── input.txt   # my specific input for the challenge
│   └── main.py
└── README.md
```

## Setup

```bash
# Install dependencies (if any are added)
uv sync
```

## Running Solutions

```bash
# Run with uv
uv run day-N/main.py day-N/input.txt

# Or use python directly
python3 day-N/main.py day-N/input.txt
```
