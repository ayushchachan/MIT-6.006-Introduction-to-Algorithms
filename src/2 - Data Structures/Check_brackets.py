
open_br = {"[": 1, "(": 2, "{": 3}

close_br = {"]": 1, ")": 2, "}": 3}

def check_brackets(S):
    stack = []
    
    for i in range(len(S)):
        c = S[i]
        if c in open_br:
            stack.append((c, i))            
        elif c in close_br:
            if not stack:
                return i
            c2 = stack[-1][0]
            if close_br[c] == open_br[c2]:
                stack.pop()
            else:
                return i
        else:
            continue
    
    if not stack:
        return -1
    else:
        return stack[-1][1]

if __name__ == "__main__":

    test_cases = [
        ("[]", "Success"),
        ("{}", "Success"),
        ("()", "Success"),
        ("([])", "Success"),
        ("{[()]}", "Success"),
        ("]", "1"),             # unmatched close
        ("())", "3"),           # wrong close
        ("([)]", "3"),          # mis-nesting
        ("([{}", "2"),          # unmatched open
        ("([{}])(", "7"),       # dangling open at end
        ("foo(bar);", "Success"),
        ("f(a,b)-g[c]", "Success"),
        ("(((((((((())))))))))", "Success"),
        ("(((((((((])))))))))", "10"),
        ("[aaaaaaa", "1"),
        ("()[]}", "5"),
        ("if (arr[i] > 0) { do(); }", "Success"),
        ("abc{def", "4"),
        ("The_quick_brown_fox", "Success"),
        ("(]", "2"),
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        got = check_brackets(inp)
        got_str = "Success" if got == -1 else str(got + 1)
        status = "OK" if got_str == expected else f"FAIL (got {got_str})"
        print(f"Test {i}: input={inp!r} expected={expected}, {status}")

