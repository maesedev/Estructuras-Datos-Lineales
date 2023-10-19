def infix_to_postfix(expression):
    POWER_ORDER = {'+': 1,'-': 1,'*': 2,'/': 2,'^': 3,'(':0,')':0}
    STACK = []
    OUTPUT = []
    expression = '(' + expression + ')'

    for c in expression:
        if c.isalpha() or c.isdigit():
            OUTPUT.append(c)
        elif c == '(':
            STACK.append(c)
        elif c == ')':
            while not (STACK[-1] == '('):
                OUTPUT.append(STACK.pop())
            STACK.pop()
        else:
            while STACK and POWER_ORDER[c] <= POWER_ORDER[STACK[-1]]:
                OUTPUT.append(STACK.pop())
            STACK.append(c)
    return ''.join(OUTPUT)


infix_expression = 'Z*X*Y+(1+2)'
INFIJA = "a+b*c-d/e"

postfix_expression = infix_to_postfix(infix_expression)

print('Expresión infija:', infix_expression)
print('Expresión postfija:', postfix_expression)
