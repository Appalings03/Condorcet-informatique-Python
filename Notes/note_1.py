# exo 1
def comp_list(l1, l2):
    
    for x in l1:
        for y in l2:
            if x == y:
                return True
    return False

# exo 2
def remove_same(l):
    temp = l.copy()
    for i in range(len(l)):
        if l[i][0] == l[i][-1]:
            temp.remove(l[i])
    return temp

#exo 3

def new_key(d):
    value = 0
    for k in d:
        value += d[k]
    d[len(d)+1] = value
    return d

# exo 4


def mel_monge(ilist):
    try:
    
    expect ValueError as e
        print(f"{}")
    mlist = []
    temp = []
    for i in range(len(ilist)):
        if i == 0:
            mlist = ilist[0]
            continue
        elif i%2 == 0:
            continue
        else:
            continue

    return mlist

if __name__ == "__main__":
    # Exo 1
    a = [17, 15, 89, 1]
    b = [56, 94, 8496, 2]
    c = comp_list(a, b)
    print(c)
    # Exo 2
    mots=['er','f','5','abc','aba','xyz','1221']
    print(remove_same(mots))
    # Exo 3
    d={0: 1, 1: 10, 2: 20}
    print(len(d))
    print(new_key(d))
    # Exo 4
    