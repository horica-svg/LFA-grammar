#format input:
#neterminali pe prima linie separati prin spatiu
#terminali pe a doua linie separati prin spatiu
#simbolul de start pe a treia linie
#productiile pe urmatoarele linii
#lambda scris ca "$"

def generare( cuv, n ):
    #print(cuv)
    if len(cuv) > n :
        mari = [x for x in cuv if x.upper() == x]
        for litera in mari:
            if '$' in d[litera]:
                generare(cuv.replace(litera, ''), n)
        return
    if len(cuv) == n and cuv.lower() == cuv:
        if cuv not in generate:
            print(cuv if cuv != "" else "$")
            #print(" cuvant bun")
        generate.append(cuv)
        return
    for litera in cuv:
        if litera == litera.upper():
            for var in d[litera]:
                generare(cuv.replace(litera, var if var != '$' else ''), n)



with open("input.txt", "r") as f:
    v = [x.split() for x in f.readlines()]
N = v[0]
T = v[1]
start = v[2][0]
stari = v[3::]
d = {}
generate = []
for stare in stari:
    d.update( { stare[0] : stare[1::] } )
n = int( input( 'n= ' ) )
generare( start, n )
cuvVerif = input("dati cuvantul: ")
if cuvVerif in generate:
    print("da")
else:
    print("nu")