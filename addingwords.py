import sys

numbers = {'+':'+', '=':'=', '-':'-'}

for line in sys.stdin.readlines():
    line = line.strip().split(' ')
    
    # Reset the dictionary:
    if line[0] == 'clear':
        numbers = {'+':'+', '=':'=', '-':'-'}
    # Update the dictionary:
    elif len(line) == 3 and line[0] != 'calc':
        numbers[line[1]] = line[2]
    # Calculate a statement:
    else:
        statement = ''
        equation = ''
        
        # Set statement & equation:
        for word in line[1:]:
            if numbers.get(word) == None:
                numbers[word] = 'unset'
            equation = equation + ' ' + numbers[word]
            statement = statement + ' ' + word
        statement = statement.strip()
        equation = equation.strip()
        equation = equation.replace('=','')
        
        # Try to evaluate the equation:
        try:
            num = str(eval(equation))
        except (RuntimeError, SyntaxError, NameError):
            num = 'ERROR'
        
        # Retrieve the key (word) for the num value:
        word = ''
        for value, key in numbers.items():
            if key == num:
                word = value
        
        # Print output based on whether or not retrieval worked:
        if word != '':
            print(statement,word)
        else:
            print(statement,'unknown')