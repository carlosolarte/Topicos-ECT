def meuzip(c1, c2):
    '''Dados dois interadores c1 e c2, gera tuplas da forma (x,y) onde x
    pertence a C1 e y a C2'''
       
    while True:
        try:
            e1,e2 = next(c1), next(c2)
            yield e1, e2
        except StopIteration:
            return

it = iter(range(10))
it2 = iter("alo mundo")

print(list(meuzip(it, it2)))


