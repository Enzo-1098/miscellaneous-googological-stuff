def prettify(postfix):
    func_form = ""
    stack = []
    for char in postfix[::-1]:
        if char == "C":
            func_form += "C("
            stack += [True]
            continue
        if char == "0":
            func_form += "0"
            while not stack[-1]:
                func_form += ")"
                stack.pop()
                if not stack:
                    break
            if stack:
                func_form += ","
                stack[-1] = False
    return func_form

print(prettify("00C00CC00C00CCC"))