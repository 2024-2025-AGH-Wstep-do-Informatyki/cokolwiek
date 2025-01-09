def onp(expression):
    import re
    # Priorytety operatorów
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}

    # Funkcja sprawdzająca, czy token jest operatorem
    def is_operator(token):
        return token in precedence

    # Funkcja sprawdzająca, czy token jest liczbą
    def is_number(token):
        return re.match(r'^-?\d+$', token) is not None

    # Funkcja parsująca, uwzględniająca liczby ujemne
    def tokenize(expression):
        tokens = []
        current_number = ''
        for i, char in enumerate(expression):
            if char.isdigit() or (char == '-' and (i == 0 or expression[i - 1] in '()+-*/')):
                current_number += char
            else:
                if current_number:
                    tokens.append(current_number)
                    current_number = ''
                if char.strip():  # Ignoruj spacje
                    tokens.append(char)
        if current_number:
            tokens.append(current_number)
        return tokens

    tokens = tokenize(expression)
    output = []  # Wyjście w ONP
    operators = []  # Stos operatorów

    for token in tokens:
        if is_number(token):
            output.append(token)  # Liczby trafiają na wyjście
        elif token == '(':
            operators.append(token)  # Lewy nawias trafia na stos
        elif token == ')':
            # Dopóki nie znajdziesz lewego nawiasu, zdejmuj operatory na wyjście
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Usuń lewy nawias
        elif is_operator(token):
            # Zdejmuj operatory ze stosu, jeśli mają większy lub równy priorytet
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)  # Dodaj bieżący operator na stos

    # Zdejmij pozostałe operatory na wyjście
    while operators:
        output.append(operators.pop())

    return output