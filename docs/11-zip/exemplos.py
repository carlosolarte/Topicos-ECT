
# Unzip

# Uma implementação utilizando compreensão de listas

l = list(zip([1,2,3], "alo"))

def unzip1(l):
    return [ x[0] for x in l] , [ x[1] for x in l]

l1,l2 = unzip1(l)
print(l1,l2) # [1, 2, 3] ['a', 'l', 'o']

def unzip2(l):
    return [ x for x,_ in l] , [ y for _,y in l]

print(unzip2(l))

## Utilizando o próprio zip

def unzip3(l):
    return tuple(zip(*l))

print(unzip3(l)) # ((1, 2, 3), ('a', 'l', 'o'))

def unzip4(l):
    return tuple(map(list, zip(*l)))

print(unzip4(l))  # ([1, 2, 3], ['a', 'l', 'o'])


def unzip5(l):
    l1,l2 = [], []
    for x,y in l:
        l1.append(x)
        l2.append(y)

    return l1,l2

print(unzip5(l)) # ([1, 2, 3], ['a', 'l', 'o'])


# =================
# *args

# Note que podemos utilizar *arg para passar um número variável de
# parâmetros a uma função

def func1(*args):
    for a in args:
        print(f'Argument: {a}')

# Chamando a função com alguns parâmetros

func1(3,"alo")
func1("mundo",4,[1,2,3])

# De fato, podemos  utilizar tuplas!
t = (1,5,[1,2,3])
func1(*t)
