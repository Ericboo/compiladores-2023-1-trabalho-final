def translate_to_python(tree):
    node_type = tree[0]
    if node_type == 'program':
        declarations = tree[1]
        code = ''
        for declaration in declarations:
            code += translate_to_python(declaration) + '\n'
        return code
    elif node_type == 'funDecl':
        function_name = tree[1][1]
        parameters = tree[2]
        block = tree[3]
        code = f'def {function_name}({", ".join([param[1] for param in parameters])}):\n'
        code += translate_to_python(block)
        return code
    elif node_type == 'block':
        declarations = tree[1]
        code = ''
        for declaration in declarations:
            code += translate_to_python(declaration) + '\n'
        return code
    elif node_type == 'varDecl':
        variable_name = tree[1][1]
        value = translate_to_python(tree[2])
        return f'{variable_name} = {value}'
    elif node_type == 'ifStmt':
        condition = translate_to_python(tree[1])
        block = translate_to_python(tree[2])
        code = f'if {condition}:\n'
        code += block
        if len(tree) > 3:
            else_block = translate_to_python(tree[3][1])
            code += f'else:\n{else_block}'
        return code
    elif node_type == 'printStmt':
        expression = translate_to_python(tree[1])
        return f'print({expression})'
    elif node_type == 'returnStmt':
        if tree[1] is None:
            return 'return'
        else:
            expression = translate_to_python(tree[1])
            return f'return {expression}'
    elif node_type == 'whileStmt':
        condition = translate_to_python(tree[1])
        statement = translate_to_python(tree[2])
        code = f'while {condition}:\n'
        code += statement
        return code
    elif node_type == 'expressionStmt':
        expression = translate_to_python(tree[1])
        return expression
    elif node_type == 'assignment':
        variable = translate_to_python(tree[1])
        assignment = translate_to_python(tree[2])
        return f'{variable} = {assignment}'
    elif node_type == 'call':
        function = translate_to_python(tree[1])
        arguments = ', '.join([translate_to_python(arg) for arg in tree[2]])
        return f'{function}({arguments})'
    elif node_type == 'identifier':
        return tree[1][1]
    elif node_type == 'const':
        return tree[1][1]
    elif node_type == 'logicOr':
        left = translate_to_python(tree[2])
        right = translate_to_python(tree[3])
        return f'{left} or {right}'
    elif node_type == 'logicAnd':
        left = translate_to_python(tree[2])
        right = translate_to_python(tree[3])
        return f'{left} and {right}'
    elif node_type == 'logicNot':
        expression = translate_to_python(tree[2])
        return f'not {expression}'
    elif node_type == 'equality':
        left = translate_to_python(tree[2])
        right = translate_to_python(tree[3])
        operator = tree[1][1]
        return f'{left} {operator} {right}'
    elif node_type == 'comparison':
        left = translate_to_python(tree[2])
        right = translate_to_python(tree[3])
        operator = tree[1][1]
        return f'{left} {operator} {right}'
    elif node_type == 'addition':
        left = translate_to_python(tree[2])
        right = translate_to_python(tree[3])
        operator = tree[1][1]
        return f'{left} {operator} {right}'
    elif node_type == 'multiplicative':
        left = translate_to_python(tree[2])
        right = translate_to_python(tree[3])
        operator = tree[1][1]
        return f'{left} {operator} {right}'
    elif node_type == 'unary':
        expression = translate_to_python(tree[2])
        operator = tree[1][1]
        return f'{operator}{expression}'
    else:
        return ''
