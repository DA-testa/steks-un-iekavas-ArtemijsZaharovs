//221RDC035, Artemijs Zaharovs, 18.gr.
from collections import namedtuple


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    for i, char in enumerate(text):
        if char in "([{":
            stack.append(Bracket(char, i))
        elif char in ")]}":
            if not stack or not are_matching(stack[-1].char, char):
                return i
            stack.pop()
    return stack[-1].position if stack else None


def main():
    input_type = input("Enter input type (I for user input, F for file input): ")
    if input_type == "I":
        text = input("Enter text: ")
    elif input_type == "F":
        filename = input("Enter filename: ")
        with open(filename, "r") as f:
            text = f.read()
    else:
        print("Invalid input type.")
        return

    mismatch_pos = find_mismatch(text)
    if mismatch_pos is None:
        print("Success")
    else:
        print(f"Mismatch at position {mismatch_pos}")


if __name__ == "__main__":
    main()
