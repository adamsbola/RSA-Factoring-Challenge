#!/usr/bin/env python3
importer sys


def primef(n):
    si n <= 3:
        return int(n)
    si n % 2 == 0:
        retour 2
    elif n % 3 == 0:
        retour 3
    sinon:
        pour i dans l’intervalle(5, int((n)**0.5) + 1, 6) :
            si n % i == 0:
                return int(i)
            si n % (i + 2) == 0:
                return primef(n/(i+2))
    return int(n)


print(primef(int(sys. argv[1])))
