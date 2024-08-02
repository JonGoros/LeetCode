import pyperclip as pc

class colors:
    green = "\033[0;32m"
    red = "\033[0;31m"
    yellow = "\033[0;33m"
    reset = "\033[0m"

def check_solution(solution, test_cases):
    
    # Get the main function name
    func_name = ''
    for i in dir(solution):
        if i[:2] != '__':
            func_name = i
            break

    # Create a callable function of func_name within the Class
    func = getattr(solution, func_name)

    # Execute the Test Cases
    errors = False
    for i in range(len(test_cases)):

        result = func(test_cases[i]["input"])

        if result == test_cases[i]["output"]:
            print(f"{colors.green}Case {i + 1}: Correct{colors.reset}")
        else:
            print(f"{colors.red}Case {i + 1}: Incorrect")
            print(f"\tExpected: {test_cases[i]['output']}")
            print(f"\tReceived: {result}{colors.reset}")
            errors = True

    # Copy the code to the Clipboard
    if not errors:
        copy_to_clipboard()


def copy_to_clipboard():

    f = open("./main.py", "r")

    lines = f.readlines()

    code_start = 0
    code_end = 0
    start_found = False
    code_found = False

    for line in range(len(lines)):

        if not start_found:
            if lines[line] == '###################### START THE CODE HERE ######################\n':
                start_found = True
        elif not code_found:
            if lines[line] != '\n':
                code_found = True
                code_start = line
        else:
            if lines[line] == '########################## TEST CASES ###########################\n':
                break
            elif lines[line].strip() != '':
                code_end = line

    code = "".join(lines[code_start: code_end + 1])

    # Copy to the Clipboard
    pc.copy(code)

    print(f"{colors.yellow}Code copied to Clipboard{colors.reset}")
