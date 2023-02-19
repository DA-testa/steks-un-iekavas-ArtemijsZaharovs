#python3
#221RDC035, Artemijs Zaharovs, 18.gr.
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i))

        if next_char in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1][0], next_char):
                return i + 1
            else:
                opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[-1][1] + 1

def main():
    text = input().strip()
    if text == 'I':
        text = input().strip()
    elif text == 'F':
        file_path = input().strip()
        with open(file_path) as f:
            text = f.read()

    mismatch = find_mismatch(text)
    if not mismatch:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
