''' 
Con este código tuve que interiorizarme con los conceptos de programación dinámica, para optimizar la recursividad del código
y evitar que consuma tiempos excesivos realizando cálculos repetidos. 
Gran parte de lo que entendí fue gracias a este video: https://www.youtube.com/watch?v=NFJ3m9a1oJQ
Parte del código fue generado con la ayuda de chat.openai.com
'''

def stairs(last_step_height, bricks_left, memo={}):
# CASOS BASE:
    # si no quedan ladrillos, se terminó una escalera válida:
    if bricks_left == 0:
        return 1

    # si los ladrillos restantes no alcanzan para formar un nuevo escalón más alto que el anterior, no se puede formar una escalera válida:
    if bricks_left < last_step_height:
        return 0
    
# MEMORIZACIÓN:
    # Verificar si la combinación ya está en la memoria para ahorrar tiempo de análisis:
    if (last_step_height, bricks_left) in memo:
        return memo[(last_step_height, bricks_left)]

# OPCIONES PARA ARMAR ESCALERAS:
    # Opción 1: se agrega un nuevo escalón 1 ladrillo más alto que el anterior a la escalera actual:
    op_1 = stairs(last_step_height + 1, bricks_left - last_step_height)

    # Opción 2: se aumenta la altura del último escalón:
    op_2 = stairs(last_step_height + 1, bricks_left)

    # Calcular el resultado
    valid_stairs = op_1 + op_2

    # almacenar la escalera en la memoria para evitar llamadas recursivas innecesarias
    memo[(last_step_height, bricks_left)] = valid_stairs
    return valid_stairs

def solution(n):
    # n debe estar entre 3 y 200:
    if n < 3 or n > 200:
        return "Please enter a number of bricks_left between 3 and 200"
    else:
        # Cantidad total de escaleras válidas, descontando la escalera formada por un solo escalón de altura 1:
        return stairs(1, n) - 1

print(solution(200))

assert(solution(3) == 1)
assert(solution(5) == 2)
assert(solution(200) == 487067745)
