class colors:
    green = "\033[0;32m"
    red = "\033[0;31m"
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
    for i in range(len(test_cases)):

        result = func(test_cases[i]["input"])

        if result == test_cases[i]["output"]:
            print(f"{colors.green}Case {i + 1}: Correct{colors.reset}")
        else:
            print(f"{colors.red}Case {i + 1}: Incorrect")
            print(f"\tExpected: {test_cases[i]['output']}")
            print(f"\tReceived: {result}{colors.reset}")
