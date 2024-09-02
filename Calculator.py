print("Welcome to Python Calculator!")

def evaluate_basic_expression(expression):
    try:
        # Keeping in mind Operator precedence
        while '*' in expression or '/' in expression:
            for i in range(len(expression)):
                if expression[i] == '*':
                    left = float(expression[i-1])
                    right = float(expression[i+1])
                    result = left * right
                    expression = expression[:i-1] + [str(result)] + expression[i+2:]
                    break
                elif expression[i] == '/':
                    left = float(expression[i-1])
                    right = float(expression[i+1])
                    result = left / right
                    expression = expression[:i-1] + [str(result)] + expression[i+2:]
                    break

        result = float(expression[0])
        i = 1
        while i < len(expression):
            if expression[i] == '+':
                result += float(expression[i+1])
            elif expression[i] == '-':
                result -= float(expression[i+1])
            i += 2
        return result
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

#Function to replace the bracketed expressions with their calculated values
def replace_brackets(expression):
    while '(' in expression:
        start = expression.rfind('(')
        end = expression.find(')', start)
        sub_expr = expression[start+1:end]
        result = evaluate_basic_expression(sub_expr.split())
        if result is not None:
            expression = expression[:start] + str(result) + expression[end+1:]
        else:
            return None
    return expression

# user input
expression = input("Enter the expression to calculate: ")

# Tokenize the expression(seperate numbers from operators and paranthesis)
tokens = []
num = ''
for char in expression:
    if char.isdigit() or char == '.':
        num += char
    else:
        if num:
            tokens.append(num)
            num = ''
        tokens.append(char)
if num:
    tokens.append(num)

expression = replace_brackets(tokens)
print(expression)
if expression is not None:
    result = evaluate_basic_expression(expression)
    if result is not None:
        print("Result:", result)
else:
    print("Error in expression.")
