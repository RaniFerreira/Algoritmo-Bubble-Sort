
def bubble_sorte(lista):
    n = len(lista)
        
    for i  in range(n - 1):
        for j in range(n - i - 1):
            if(lista[j] > lista[j + 1]):
                
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
    
    
numeros = [7,2,3,5,0,8]
print("Lista original:", numeros)
print("Lista ordenada:",bubble_sorte(numeros))
    