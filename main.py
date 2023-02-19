# python3
from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]
def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
        opening_brackets_stack.append(Bracket(next_char, i+1))
        if next_char in ")]}":
               if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next_char):
                return i+1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position
    return "Success"
def main():
    choice = input().upper()
    text = input()
    mismatch = find_mismatch(text)
    if choice == "I":
        print(mismatch)
    else:
        if mismatch == "Success":
            print(mismatch)
        else:
            print("0")
if __name__ == "__main__":
    main()
