# Define the function signature with two parameters: problems and calculate.
def arithmetic_arranger(problems, show_answers=False):  
    # Check if the number of problems exceeds the limit (five).
    if len(problems) > 5:
        return "Error: Too many problems."

    # Validate each problem:
    valid_problems = []
    for problem in problems:
        # Split the problem into numbers and operator.
        parts = problem.split()
        if len(parts) != 3:
            return f'Error: Invalid format for {problem}'

        num1, op, num2 = parts

        # Ensure the operator is '+' or '-'.
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check numbers if digits.
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if numbers are more than 4 digits.
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Save numbers and operands.
        valid_problems.append((int(num1), op, int(num2)))

    # Calculate results if calculate=True.
    if show_answers:
        results = [str(a + b) if op == '+' else str(a - b) for a, op, b in valid_problems]

    # Format each problem with proper alignment and spacing.
    formatted_problems = []
    for i, (a, op, b) in enumerate(valid_problems):
        # Determine the maximum width for each problem.
        max_width = max(len(str(a)), len(str(b))) + 2

        first_line = (" " * (max_width - len(str(a)))) + str(a)
        second_line = op + (" " * (max_width - len(str(b)) - 1)) + str(b)

        # Add dashes below each problem.
        third_line = "-" * max_width

        if show_answers:
            fourth_line = " " * (max_width - len(results[i])) + results[i]

        formatted_problems.append([first_line, second_line, third_line])
        if show_answers:
            formatted_problems[-1].append(fourth_line)

    # Combine all problems horizontally.
    combined = "\n".join(["    ".join(line) for line in zip(*formatted_problems)])
    
    # Return the result as a string.
    return combined

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')