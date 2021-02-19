def seqinf():
    '''Gera a sequência infinita 1,2,3,....'''
    i = 1
    while True:
        yield i
        i+=1

def primeiros(n, seq):
    '''Gerar os primeiros n elementos da sequência seq'''
    for i in range(n):
        try:
            v = next(seq)
            yield v
        except StopIteration:
            break

# Uma forma mais simples de implementar a função anterior
def primeirosv2(n, seq):
    '''Gerar os primeiros n elementos da sequência seq'''
    for (i,x) in enumerate(seq):
        if i>=n: break
        yield x

print(list(primeiros(10, seqinf())))
print(list(primeiros(5, seqinf())))
