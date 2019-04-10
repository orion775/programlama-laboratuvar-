import random
def create_matrix(m:int, n:int):
    liste = []
    for i in range(m):
        liste.append([])
        for j in range(n):
            s = random.randint(-5, 5)
            #s = -1
            liste[i].append(s)
    return liste

def print_function(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end = ' ')
        print()

def convert_function_to_hash(matrix):
    
    dictionary = {}
    
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            dictionary[(i, j)] = matrix[i][j]
            #print(matrix[i][j], end = ' ')
        #print()
    return dictionary

def print_hash(hash_list):
    for key in hash_list:
        print(hash_list[key], end = ' ')
        
matrix = create_matrix(3, 2)
print_function(matrix)
print('\n\n')
print(convert_function_to_hash(matrix))
matris = convert_function_to_hash(matrix)
print('\n\n')
print_hash(matris)
