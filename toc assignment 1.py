import re

def generate_stack_code(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    op_map = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}

    tokens = re.findall(r'(\w+|[\+\-\*\/\(\)])', expression)
    
    output_queue = []
    operator_stack = []

    for token in tokens:
        if token.isalnum():
            output_queue.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        output_queue.append(operator_stack.pop())

    assembly_code = []
    for token in output_queue:
        if token in op_map:
            assembly_code.append(op_map[token])
        else:
            assembly_code.append(f"PUSH {token}")
    
    return "\n".join(assembly_code)


input_expression = "(a+b)*c"
generated_code = generate_stack_code(input_expression)

print("\n--- Stack Machine Code Generator ---")
print(f"Input: {input_expression}")
print("\nOutput:")
print(generated_code)