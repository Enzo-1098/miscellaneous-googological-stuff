import re

def PrSS(tree, n):
    if tree[-1] == 0: return tree[:-1]
    root_pos = len(tree) - tree[::-1].index(tree[-1] - 1) - 1
    return tree[:root_pos] + tree[root_pos:-1] * n
    

def ABBN(string, n):
    if not isinstance(string, str): return "Input is not string."
    char_check = re.compile(r'[^()]').search
    if bool(char_check(string)): return "String contains invalid characters."
    tree = []
    level = 0
    for char in string:
        if char == "(":
            tree += [level]
            level += 1
        elif char == ")":
            level -= 1
            if level < 0: return "Invalid parentheses."
    if level != 0: return "Imbalanced parentheses."
    new_tree = PrSS(tree, n) + [0]
    new_string = ""
    level = -1
    for i in new_tree:
        new_string += ")" * (level - i + 1) + "("
        level = i
    return new_string[:-1]