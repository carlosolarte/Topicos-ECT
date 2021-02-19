def agrupar(c):
    ''' Dada uma sequência x1,x2,x3,x4,... agrupa os elementos de dois em dois:
    (x1,x2), (x3,x4),... '''
    while True:
        try:
            e1 = next(c) # Extrair um elemento
            e2 = next(c) # Extrair o próximo elemento
            yield e1,e2  # Gerar a tupla
        except StopIteration:
            return


it = iter(range(1,11))
it2 = iter(range(1,10))
print(list(agrupar(it)))
print(list(agrupar(it2)))

it3 = iter(range(100))
print(list(zip(it3, it3)))
