import re


def GetNumberFromUserInput(UserInput, Position):
    Number = ""
    MoreDigits = True
    while MoreDigits:
        if not (re.search("[0-9]", str(UserInput[Position])) is None):
            Number += UserInput[Position]
        else:
            MoreDigits = False
        Position += 1
        if Position == len(UserInput):
            MoreDigits = False
    if Number == "":
        return -1, Position
    else:
        return int(Number), Position
class InvalidBracketsException(Exception):
    "Invalid brackets"
    pass

def seperate_brackets(userinput):
    print(userinput)
    expression = []
    Brackets = {")": 1, "(": -1}
    Bracket_value = 0
    UserInputCopy = userinput
    for position, character in enumerate(UserInputCopy):
        Bracket_value += Brackets.get(character, 0)
        if Bracket_value < 0:
            # if character not in Brackets.keys():
            userinput = UserInputCopy[:-position]
            expression.append(character)
    
    print(userinput)
    
    if Bracket_value != 0:
        raise InvalidBracketsException()


    if expression == []:
        value = (ConvertToRPN("".join(userinput[1:])))
        return value
    expression = (seperate_brackets(expression[1:]))
    print(expression)
    
def ConvertToRPN(UserInput):
    Position = 0
    # Assigning dicitonary to precedence variable,
    # the higher the value for each operator,
    # the sooner the expression with that operator will be executed
    Precedence = {"+": 2, "-": 2, "*": 4, "/": 4}
    Operators = []
    # GetNumberFromUserInput() returns a tuplpe of two values, these can be assigned to to variables in one line
    Operand, Position = GetNumberFromUserInput(UserInput, Position)
    UserInputInRPN = []
    UserInputInRPN.append(str(Operand))
    # Append the last character in the user input to the operators list
    Operators.append(UserInput[Position - 1])
    while Position < len(UserInput):
        Operand, Position = GetNumberFromUserInput(UserInput, Position)
        UserInputInRPN.append(str(Operand))
        if Position < len(UserInput):
            CurrentOperator = UserInput[Position - 1]
            # Checking if the found operator being pushed onto the stack has lower or equal precedence as the operator as the top of the stack,
            # then the operator is popped off the stack and added to th output queue
            while (
                len(Operators) > 0
                and Precedence[Operators[-1]] > Precedence[CurrentOperator]
            ):
                UserInputInRPN.append(Operators[-1])
                Operators.pop()
            # Checking if the found operator has equal importance as the current operator
            if (
                len(Operators) > 0
                and Precedence[Operators[-1]] == Precedence[CurrentOperator]
            ):
                UserInputInRPN.append(Operators[-1])
                Operators.pop()
            Operators.append(CurrentOperator)
        else:
            # Pop the remaining operators and add to the output queue
            while len(Operators) > 0:
                UserInputInRPN.append(Operators[-1])
                Operators.pop()
    return UserInputInRPN

seperate_brackets("(3+(2*3))")