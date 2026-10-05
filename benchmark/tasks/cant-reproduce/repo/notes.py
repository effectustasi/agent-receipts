import sys


def load_notes(path):
    with open(path, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


if __name__ == "__main__":
    for note in load_notes(sys.argv[1]):
        print("-", note)
