'''
La primera versión de este código la escribí sin ayuda, pero no pasaba uno de los test escondidos del desafío.
Por descarte, entendí que el problema estaba en el tiempo de ejecución, que era el doble de lo que es el actual.
Buscando en internet encontré que lo mejor era encararlo como un problema de programación dinámica. 
Siendo que la condición para obtener un triple mágico (x, y, z) es que "y % x = 0" y "z % y = 0"; y que por carácter
transitivo, "z % x = 0", muchos de los cálculos que estaba haciendo mi código original, eran repetidos e innecesarios.

Por otro lado, el visual studio me sugirió que en lugar de usar range() en el for loop, usara enumerate(), lo cual 
también contribuyó a disminuir levemente el tiempo de ejecución del código.
'''

def check_list(lst):
    # La lista tiene entre 2 y 2000 elementos
    if len(lst) < 2 or len(lst) > 2000:
        return []
    
    # Todos los elementos de la lista son números entre 1 y 999999
    for num in lst:
        if num < 1 or num > 999999:
            return []
    return lst

def solution(l):
    # Confirmar que la lista que se pasa en la función cumpla con los requisitos del problema
    l = check_list(l)
    n = len(l)

    # Crear una lista para almacenar la cantidad de veces en que obtengo un par de números divisibles entre sí
    doubles = [0] * n
    
    # Inicializar el contador de triples mágicos
    triples = 0

    # Iterar por la lista en busca de los pares divisibles entre sí
    for i, li in enumerate(l[1:], start=1):
        for j, lj in enumerate(l[:i]):
            if li % lj == 0:
                # Actualizar la lista de dobles mágicos
                doubles[i] += 1
                # Los dobles mágicos que se sumaron cuando j actual se evaluó como i, también son triples mágicos
                triples += doubles[j]

    return triples
 

# CHEQUEO DEL CÓDIGO
import timeit
import random


def generate_list():
    lst = [1, 2, 4]
    while len(lst) < 2000:
        num = random.randint(1, 999999)
        lst.append(num)
        
# Obtener una lista de 2000 elementos, donde exista al menos 1 triple mágico
l = generate_list()

# Chequear el tiempo de ejecución del código
time = timeit.timeit(lambda: solution(l), number=1)
print(solution(l)," - Tiempo de ejecución de solution1:", time)


# Confirmar casos conocidos
assert(solution([7, 17, 31]) == 0)
assert(solution([1, 1, 1]) == 1)
assert(solution([1, 2, 3, 4, 5, 6]) == 3)
assert(solution([3, 6, 12, 24]) == 4)
assert(solution([1, 1, 1, 1]) == 4)
assert(solution([]) == 0)
