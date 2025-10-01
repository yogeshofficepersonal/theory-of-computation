def optimize_code(statements):
    optimized = []
    env = {}

    for stmt in statements:
        var, expr = stmt.split("=")
        var, expr = var.strip(), expr.strip()

       
        if "*" in expr:
            left, right = expr.split("*")
            left, right = left.strip(), right.strip()
            if left.isdigit() and right.isdigit():
                expr = str(int(left) * int(right))
            elif right == "1":
                expr = left
            elif left == "1":
                expr = right

        if "+" in expr:
            left, right = expr.split("+")
            left, right = left.strip(), right.strip()
            if left.isdigit() and right.isdigit():
                expr = str(int(left) + int(right))
            elif right == "0":
                expr = left
            elif left == "0":
                expr = right

        
        if expr in env:
            expr = env[expr]

        env[var] = expr
        optimized.append(f"{var} = {expr}")

    return optimized



input_code = [
    "x = 2 * 8",
    "y = x * 1",
    "z = y + 0"
]

optimized_code = optimize_code(input_code)

print("Optimized Code:")
for line in optimized_code:
    print(line)