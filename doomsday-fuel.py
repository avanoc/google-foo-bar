''' 
NOTA: EL SISTEMA DE VERIFICACIÓN NO ME PERMITIÓ SUBIR EL CÓDIGO CON LAS NOTAS USANDO # NI \'''
Este código fue creado con la asistencia de chat.openai, siguiendo los lineamientos de 
https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md
habiendo consultado en Stack Overflow y después de quemarme las pestañas!
'''

from fractions import Fraction
import numpy as np

# Definir función gcd ya que math.gcd no está permitida
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Definir una función para calcular el múltiplo común menor (lcm)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Definir una función para crear una lista de lcm
def lcm_list(numbers):
    if not numbers:
        return 1
    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm(lcm_result, numbers[i])
    return lcm_result

# Definir una función para calcular el múltiplo común menor de varias fracciones
def get_lcd(fractions):
    denominators = [fraction.denominator for fraction in fractions]
    least_common_denominator = lcm_list(denominators)
    return least_common_denominator

# Definir la función para resolver el problema
def solution(m):
    
    # Para el caso en que el primer estado sea terminal
    if sum(m[0]) == 0:
        num_terminal_states = sum(1 for row in m if sum(row) == 0) + 1
        return [1] + [0] * (num_terminal_states - 2) + [1]
    
    # Para el caso en que sólo haya 1 estado
    if len(m) == 1 and len(m[0]) == 1:
        return [1, 1]

    # Separar estados terminales de estados no terminales
    terminal_states = []
    non_terminal_states = []
    for i, row in enumerate(m):
        if sum(row) == 0:
            terminal_states.append(i)
        else:
            non_terminal_states.append(i)

    num_non_terminal_states = len(non_terminal_states)
    num_states = len(m)

    # Crear matrices Q y R con probabilidades
    q_matrix = []
    r_matrix = []
    for n in range(num_non_terminal_states):
        q_row = []
        r_row = []
        i = non_terminal_states[n]
        for j in range(num_states):
            if j in non_terminal_states:
                if sum(m[i]) != 0:
                    q_row.append(Fraction(m[i][j], sum(m[i])))
                else:
                    q_row.append(Fraction(m[i][j], 1))
            else:
                if sum(m[i]) != 0:
                    r_row.append(Fraction(m[i][j], sum(m[i])))
                else:
                    r_row.append(Fraction(m[i][j], 1))
        q_matrix.append(q_row)
        r_matrix.append(r_row)
    
    # Crear matrix I
    i_matrix = np.identity(num_non_terminal_states)

    # Calcular matriz F
    inverse_matrix = i_matrix - q_matrix
    f_matrix = np.linalg.inv(inverse_matrix.astype(float))
    f_matrix = np.array([[Fraction(x).limit_denominator() for x in row] for row in f_matrix])

    # Calcular F x R
    f_x_r = np.matmul(f_matrix, r_matrix)

    # Extraer las nuevas probabilidades de los estados terminales
    probabilities = []
    lcd = get_lcd(f_x_r[0])
    for i in range(len(f_x_r[0])):
        probabilities.append(int(f_x_r[0][i].numerator * lcd // f_x_r[0][i].denominator))
    probabilities.append(lcd)

    return probabilities
