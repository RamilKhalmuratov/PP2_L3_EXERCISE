from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print("".join(perm))

user_input = input("String: ")
print_permutations(user_input)
