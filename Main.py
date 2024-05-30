# COMPLEX CALCULATOR USING REVERSE POLISH NOTATION - Jared Wensley

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '%': 3,
}


def space_expression(expression):
    result = []

    for char in expression:
        if char.isdigit():
            # If the character is a digit, append it to the current number string.
            if result and result[-1][-1].isdigit():
                result[-1] += char  # Append to the last number in the result list.
            else:
                result.append(char)  # Start a new number string.
        else:
            # If the character is not a digit, it's an operator or other character,
            # append it separately, ensuring spaces around it.
            result.append(' ' + char + ' ')

    return ''.join(result).strip()


# hold the order of operations
def get_precedence(op):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '%': 3,
    }
    # if the operator is not in dictionary then zero is returned
    return precedence.get(op, 0)


def infix_to_postfix(expression):
    output = []
    operators = []
    expression = space_expression(expression)

    # Loops through all characterts and format into postfix expression
    for token in expression.split():

        if not token.isnumeric() and token not in precedence:  # FORMAT CHECK, Make sure each charater is valid
            print("Error, incorrect charater found."
                  " Only use numbers and the following symbols '"
                  "+, -, *, /, %, ^'")
            return ""

        if token.isnumeric():
            #print("Push digit to output stack:", token)
            output.append(token)
        elif token == '(':
            operators.append(token)

        elif token == ')':
            while operators and operators[-1] != '(':
                # pop items from the operators stack and push them into the output stack until left parenthesis is found
                output.append(operators.pop())
            operators.pop()  # pop the left parenthesis
        else:
            # if the next operator is appended to the output stack if it has a higher precendence then the operator on the top of the stack
            while operators and get_precedence(operators[-1]) >= get_precedence(token):
                output.append(operators.pop())
            operators.append(token)
            #print("Output Stack", output)
            #print("Operators stack", operators)

    while operators:
        output.append(operators.pop())

    #print(output)
    return ' '.join(output)


def evaluate_postfix(expression):
    #create a list that contains the stack
    stack = []

    # Need spaces inbetween expressions, so we add spaces if the user did not entered spaces.
    expression = space_expression(expression)

    for token in expression.split():
        if token.isnumeric():  # used to be .isdigit(). CHECK IF THIS WORKS
            #print("Push on stack:", token)
            stack.append(int(token))
        # pop the last two digits from the stack to use in an operation to then put back onto the stack
        else:

            # do not pop the first operand yet, used to determine if a negative is on the first number.
            if stack:
                b = stack[-1]
            else:
                print("The formatting seems incorrect, maybe an extra symbol? Try again")
                return ""

            # if a digit has a negative token and does not have 2 operands to performs the action
            # Set that digit to negative and append to stack
            if len(stack) < 2 and token == '-':
                b = -abs(b)
                stack.pop()
                stack.append(b)
                continue

            # pop the 'b' variable from the stack and then assign and pop the next operand.
            # try:
            stack.pop()
            a = stack.pop()
            # except:
            #    print("The formatting sms incorrect, maybe an extra symbol? Try again")
            #     return ""

            # Use to format
            if token == '+':
                stack.append(a + b)

                # print("add and push result on stack:", a, b)

            elif token == '-':
                # print("subtract and push result on stack", a, b)
                stack.append(a - b)
            elif token == '*':
                # print("multiply and push result on stack", a, b)
                stack.append(a * b)
            elif token == '/':
                # print("divide and push result on stack", a, b)
                stack.append(a / b)
            elif token == '^':
                # print("assign power and push result on stack", a, b)
                stack.append(a ** b)
            elif token == '%':
                # print("find modulus and push result on stack", a, b)
                stack.append(a % b)
            else:
                print("continue was called")
        # print("Stack: ", stack)

    return stack.pop()


print("Complex Calculator, "
      "example '(1+2)-3/2+5^2*3'\n"
      "Type 'quit' to end the program")
while True:

    expression = input("Calculate: ")
    if expression.lower() == "quit":
        break
    expression = infix_to_postfix(expression)
    if expression == "":
        continue

    result = evaluate_postfix(expression)
    if result == "":
        continue
    print("result: ", result)
    print("")
