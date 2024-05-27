def arithmetic_arranger(problems, showResults=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_line = ''
    second_line = ''
    lines = ''
    sumx = ''
    string = ''
    
    for problem in problems:
        left, operator, right = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not left.isnumeric() or not right.isnumeric():
            return 'Error: Numbers must only contain digits.'

        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        sum = ''
        if operator == "+":
            sum = str(int(left) + int(right))
        else:
            sum = str(int(left) - int(right))

        length = max(len(left), len(right)) + 2
        top = str(left).rjust(length)
        bottom = operator + str(right).rjust(length - 1)
        line = '-' * length
        res = str(sum).rjust(length)

        if problem != problems[-1]:
            first_line += top + '    '
            second_line += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first_line += top
            second_line += bottom
            lines += line
            sumx += res

    if showResults:
        string = first_line + '\n' + second_line + '\n' + lines + '\n' + sumx
    else:
        string = first_line + '\n' + second_line + '\n' + lines

    return string
