import tkinter as tk
import graphviz

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
        noile_stari |= set(inchidere(tranzitie(stare, litera)))
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

# Create the GUI
window = tk.Tk()
window.title("DFA/NFA")
window.geometry("800x600")

# Create a canvas for displaying the image
canvas = tk.Canvas(window, width=800, height=500, bg="white")
canvas.pack(side=tk.TOP)

# Create a Graphviz graph
dot = graphviz.Digraph()
dot.graph_attr['rankdir'] = 'LR'
dot.node('start', '', shape='none')
for state in stari:
    if state in stari_finale:
        dot.node(state, state, shape='doublecircle')
    else:
        dot.node(state, state, shape='circle')
    for symbol in stari[state]:
        for next_state in stari[state][symbol]:
            dot.edge(state, next_state, label=symbol)

# Render the Graphviz graph to an image
import graphviz

# Create a Graphviz graph object
dot = graphviz.Digraph()

# Add nodes to the graph
for state in stari:
    shape = "circle"
    if state in stari_finale:
        shape = "doublecircle"
    dot.node(state, shape=shape)

# Add edges to the graph
for state in stari:
    for symbol in stari[state]:
        for next_state in stari[state][symbol]:
            dot.edge(state, next_state, label=symbol)

# Render the Graphviz graph to an image
dot.render("graph")

# Create an image object from the rendered image
img = tk.PhotoImage(file="graph.png")

# Create a canvas for displaying the image
canvas = tk.Canvas(window, width=800, height=500, bg="white")
canvas.pack(side=tk.TOP)

# Draw the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Create a label for displaying the accepted path
label = tk.Label(window, text="Accepted path: ", font=("Arial", 12))
label.pack(side=tk.BOTTOM)

# Function for updating the label with the accepted path
def update_label(path):
    label.config(text="Accepted path: " + "->".join(path))

# Main loop for the GUI
window.mainloop()
