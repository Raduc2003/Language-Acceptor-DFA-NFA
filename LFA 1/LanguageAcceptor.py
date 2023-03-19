f = open("LFA 1/input.txt")
stari = {}
stari_finale = []
for line in f:
    line = line.split(" ")
    if len(line) == 1 or (line[1][0] == 'q' and line[1][1:].isdigit()):
        stari_finale=line
    else:
        if line[0] not in stari.keys():
            stari.setdefault(line[0], {})
        if line[1] not in stari[line[0]].keys():
            stari[line[0]][line[1]] = []
            stari[line[0]][line[1]].append(line[2].strip())
        else:
            stari[line[0]][line[1]].append(line[2].strip())
print(stari)

def tranzitie(stare, litera):
    try:
        noile_stari = stari[stare][litera]
        return noile_stari
    except:
        return []

def inchidere(stari):
    inchidere = set(stari)
    stack = list(stari)
    while stack:
        stare = stack.pop()
        for urmatoarea_stare in tranzitie(stare, 'eps'):
            if urmatoarea_stare not in inchidere:
                inchidere.add(urmatoarea_stare)
                stack.append(urmatoarea_stare)
    return inchidere
# acceptor
print(stari_finale)
cuv = input()
drum = []
stari_curente = inchidere({'q0'})
for litera in cuv:
    noile_stari = set()
    for stare in stari_curente:
        noile_stari = set(inchidere(tranzitie(stare, litera)))
    stari_curente = noile_stari
    if not stari_curente:
        print("neacceptat")
        break;
    drum.extend(stari_curente) # append the current states to the drum list
if set(stari_curente) & set(stari_finale):
    print("acceptat")
    print("->".join(drum)) # join the elements of the drum list with "->" separator
else:
    print("neacceptat")
