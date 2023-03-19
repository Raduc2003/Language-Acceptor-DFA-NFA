f= open("LFA 1\input.txt")
stari={}
stari_finale=[]
for line in f:
    line=line.split(" ")
    if len(line)==1 or(line[1][0]=='q' and line[1][1].isdigit()) :
        stari_finale=line
    else:
        if line[0] not in stari.keys():
            
            stari.setdefault(line[0],{})
            
            if line[1] not in stari[line[0]].keys():
                stari[line[0]][line[1]]=[]
                stari[line[0]][line[1]].append(line[2].strip())
            else:
                stari[line[0]][line[1]].append(line[2].strip())
        else:
            if line[1] not in stari[line[0]].keys():
                stari[line[0]][line[1]]=[]
                stari[line[0]][line[1]].append(line[2].strip())
            else:
                stari[line[0]][line[1]].append(line[2].strip())
# print(stari)
# print(stari['q0']['1'])
def tranzitie(stare,litera):
    try:
        noua_stare=stari[stare][litera]
        return noua_stare[0]
    except:
        return -1

# acceptor
tranzitie('q0','0')
print(stari_finale)
cuv=input()
drum=[]
stare='q0'
for litera in cuv:
    drum.append(stare)
    stare=tranzitie(stare,litera)
    if stare==-1:
        print("neacceptat")
        break;
if stare in stari_finale:
    print("acceptat")
    print(*drum,sep='->')

