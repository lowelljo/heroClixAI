#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from Heros import *

window = Tk()
window.title("HeroClixAI")

myCapHero = CaptainAmerica()
myIronManHero = IronMan()
myThorHero = Thor()
enemyCapHero = CaptainAmerica()
enemyIronManHero = IronMan()
enemyThorHero = Thor()
heroArray = [myCapHero, myIronManHero, myThorHero,
             enemyCapHero, enemyIronManHero, enemyThorHero]

def getMove():

    #check if cap is the closest
    
        #if not, move cap
    #check if iron man or thor is close enough to attack
        # if we are, attack, require dice value against defense, check


def updateState():
    myCapHero.location = capEntry.get()

    myIronManHero.location = ironManEntry.get()

    myThorHero.location = thorEntry.get()

    enemyCapHero.location = enemyCapEntry.get()

    enemyIronManHero.location = enemyIronManEntry.get()

    enemyThorHero.location = enemyThorEntry.get()

    if whosAttackingEntry.get():
        whosAttackingText = whosAttackingEntry.get()
    if whosDefendingEntry.get():
        whosBeingAttackedText = whosDefendingEntry.get()
    if whatWasRolledEntry.get():
        whatWasRolled = int(whatWasRolledEntry.get())


def bfs(graph, start, destination):
    beenTo = []
    queue = [[start]]

    if start == destination:
        return
    while queue:
        p = queue.pop(0)
        n = p[-1]

        if n not in beenTo:
            close = graph[n]
            for closest in close:
                np = list(p)
                np.append(closest)
                queue.append(np)

                if closest == destination:
                    print("Path:", *np)
                    return
            beenTo.append(n)
    print("No path exists")
    return


def forceValueToHero():
    whosValueToChange = valueToEntry.get()
    whatTheValueIs = int(valueEntry.get())


def getStatsOnHero():
    whosStats = int(statsEntry.get())
    messagebox.showinfo(heroArray[whosStats], str(heroArray[whosStats].placeInDial))


# labels
ourCap = Label(window, text="My Cap")
ourCap.grid(row=0, column=0)

ourIronMan = Label(window, text="My Iron Man")
ourIronMan.grid(row=1, column=0)

ourThor = Label(window, text="My Thor")
ourThor.grid(row=2, column=0)

enemyCap = Label(window, text="Enemy Cap")
enemyCap.grid(row=0, column=2)

enemyIronMan = Label(window, text="Enemy Iron Man")
enemyIronMan.grid(row=1, column=2)

enemyThor = Label(window, text="Enemy Thor")
enemyThor.grid(row=2, column=2)

whosAttacking = Label(window, text="Whos Attacking")
whosAttacking.grid(row=4, column=0)

whosDefending = Label(window, text="Whos Defending")
whosDefending.grid(row=4, column=2)

emptySpace = Label(window, text="")
emptySpace.grid(row=3, column=0)

emptySpace2 = Label(window, text="")
emptySpace2.grid(row=6, column=0)

whatsRolled = Label(window, text="Number Rolled")
whatsRolled.grid(row=5, column=0)

forceValue = Label(window, text="Force Value to")
forceValue.grid(row=7, column=0)

valueToForce = Label(window, text="Value: ")
valueToForce.grid(row=7, column=2)

getStatsOn = Label(window, text="Get Stats On")
getStatsOn.grid(row=9, column=0)

# Entries
capEntry = Entry(window)
capEntry.grid(row=0, column=1)

ironManEntry = Entry(window)
ironManEntry.grid(row=1, column=1)

thorEntry = Entry(window)
thorEntry.grid(row=2, column=1)

enemyCapEntry = Entry(window)
enemyCapEntry.grid(row=0, column=3)

enemyIronManEntry = Entry(window)
enemyIronManEntry.grid(row=1, column=3)

enemyThorEntry = Entry(window)
enemyThorEntry.grid(row=2, column=3)

whosDefendingEntry = Entry(window)
whosDefendingEntry.grid(row=4, column=1)

whosAttackingEntry = Entry(window)
whosAttackingEntry.grid(row=4, column=3)

whatWasRolledEntry = Entry(window)
whatWasRolledEntry.grid(row=5, column=1)

valueToEntry = Entry(window)
valueToEntry.grid(row=7, column=1)

valueEntry = Entry(window, )
valueEntry.grid(row=7, column=3)

statsEntry = Entry(window)
statsEntry.grid(row=9, column=1)

# Buttons
attackButton = Button(window, text="Update State", bg="gray", command=updateState)
attackButton.grid(row=5, column=2)

forceButton = Button(window, text="Force Value", bg="gray", command=forceValueToHero)
forceButton.grid(row=8, column=2)

getStatsButton = Button(window, text="Get Stats", bg="gray", command=getStatsOnHero)
getStatsButton.grid(row=9, column=2)

whatTheFuckThisThingIsHuge = {'A1': ['B1', 'A2', 'B2'], 'B1': ['A1', 'C1', 'A2', 'B2', 'C2'],
                              'C1': ['B1', 'D1', 'B2', 'C2', 'D2'], 'D1': ['C1', 'E1', 'C2', 'D2', 'E2'],
                              'E1': ['D1', 'F1', 'D2', 'E2', 'F2'], 'F1': ['E1', 'G1', 'E2', 'F2', 'G2'],
                              'G1': ['F1', 'H1', 'F2', 'G2', 'H2'], 'H1': ['G1', 'G2', 'H2'],
                              'I1': ['J1', 'I2', 'J2'], 'J1': ['I1', 'K1', 'I2', 'J2', 'K2'],
                              'K1': ['J1', 'L1', 'J2', 'K2', 'L2'], 'L1': ['K1', 'M1', 'K2', 'L2', 'M2'],
                              'M1': ['L1', 'N1', 'L2', 'M2', 'N2'], 'N1': ['M1', 'O1', 'M2', 'N2', 'O2'],
                              'O1': ['N1', 'P1', 'N2', 'O2', 'P2'], 'P1': ['O1', 'O2', 'P2'],
                              'A2': ['A1', 'B1', 'B2', 'B3', 'A3'],
                              'B2': ['A1', 'B1', 'C1', 'C2', 'C3', 'B3', 'A3', 'A2'],
                              'C2': ['B1', 'C1', 'D1', 'D2', 'D3', 'C3', 'B3', 'B2'],
                              'D2': ['C1', 'D1', 'E1', 'E2', 'D3', 'C3', 'C2'],
                              'E2': ['D1', 'E1', 'F1', 'F2', 'D3', 'D2'], 'F2': ['E1', 'F1', 'G1', 'E2'],
                              'G2': ['F1', 'G1', 'H1', 'H2', 'H3', 'G3', 'F3'],
                              'H2': ['G1', 'H1', 'H3', 'G3', 'G2'], 'I2': ['I1', 'J1', 'J2', 'J3', 'I3'],
                              'J2': ['I1', 'J1', 'K1' 'K3', 'J3', 'I3', 'I2'],
                              'K2': ['J1', 'K1', 'L1', 'L2'], 'L2': ['K1', 'L1', 'M1', 'M2', 'M3' 'K2'],
                              'M2': ['L1', 'M1', 'N1', 'N2', 'N3', 'M3', 'L2'],
                              'N2': ['M1', 'N1', 'O1', 'O2', 'O3', 'N3', 'M3', 'M2'],
                              'O2': ['N1', 'O1', 'P1', 'P2', 'P3', 'O3', 'N3', 'N2'],
                              'P2': ['O1', 'P1', 'P3', 'O3', 'O2'],
                              'A3': ['A2', 'B2', 'B3', 'B4', 'A4'],
                              'B3': ['A2', 'B2', 'C2', 'C3', 'C4', 'B4', 'A4', 'A3'],
                              'C3': ['B2', 'C2', 'D2', 'D3', 'D4', 'C4', 'B4', 'B3'],
                              'D3': ['C2', 'D2', 'E2', 'D4', 'C4', 'C3'], 'E3': ['F3', 'F4', 'E4'],
                              'F3': ['G2', 'G3', 'G4', 'F4', 'E4', 'E3'],
                              'G3': ['G2', 'H2', 'H3', 'H4', 'G4', 'F4', 'F3'], 'H3': ['G2', 'H2', 'H4', 'G4', 'G3'],
                              'I3': ['I2', 'J2', 'J3', 'J4', 'I4', 'H4'],
                              'J3': ['I2', 'J2', 'K3', 'K4', 'J4', 'I4', 'I3'],
                              'K3': ['J2', 'L3', 'L4', 'K4', 'J4', 'J3'], 'L3': ['L4', 'K4', 'K3'],
                              'M3': ['L2', 'M2', 'N2', 'N3', 'N4', 'M4'],
                              'N3': ['M2', 'N2', 'O2', 'O3', 'O4', 'N4', 'M4', 'M3'],
                              'O3': ['N2', 'O2', 'P2', 'P3', 'P4', 'O4', 'N4', 'N3'],
                              'P3': ['O2', 'P2', 'P4', 'O4', 'O3'], 'A4': ['A3', 'B3', 'B4', 'B5', 'A5'],
                              'B4': ['A3', 'B3', 'C3', 'C4', 'B5', 'A5', 'A4'],
                              'C4': ['B3', 'C3', 'D3', 'D4', 'B5', 'B4'],
                              'D4': ['C3', 'D3', 'C4'], 'E4': ['E3', 'F3', 'F4', 'F5', 'E5'],
                              'F4': ['E3', 'F3', 'G3', 'G4', 'F5', 'E5', 'E4'],
                              'G4': ['F3', 'G3', 'H3', 'H4', 'H5', 'F5', 'F4'],
                              'H4': ['G3', 'H3', 'I3', 'I4', 'I5', 'H5', 'G5', 'G4'],
                              'I4': ['H3', 'I3', 'J3', 'J4', 'J5', 'I5', 'H5', 'H4'],
                              'J4': ['I3', 'J3', 'K3', 'K4', 'K5', 'J5', 'I5', 'I4'],
                              'K4': ['J3', 'K3', 'L3', 'L4', 'J5', 'J4'], 'L4': ['K3', 'L3', 'L4'],
                              'M4': ['M3', 'N3', 'N4'], 'N4': ['M3', 'N3', 'O3', 'O4', 'O5', 'M4'],
                              'O4': ['N3', 'O3', 'P3', 'P4', 'P5', 'O5', 'N4'],
                              'P4': ['O3', 'P3', 'P5', 'O5', 'O4'], 'A5': ['A4', 'B4', 'B5', 'B6', 'A6'],
                              'B5': ['A4', 'B4', 'C4', 'B6', 'A6', 'A5'], 'C5': ['D5', 'D6', 'C6'],
                              'D5': ['D6', 'C6', 'C5'],
                              'E5': ['E4', 'F4', 'F5', 'F6', 'E6', 'D6'], 'F5': ['E4', 'F4', 'G4', 'F6', 'E6', 'E5'],
                              'G5': ['H4', 'H5', 'H6', 'G6'], 'H5': ['G4', 'H4', 'I4', 'I5', 'I6', 'H6', 'G6', 'G5'],
                              'I5': ['H4', 'I4', 'J4', 'J5', 'J5', 'J6', 'I6', 'H6', 'H5'],
                              'J5': ['I4', 'J4', 'K4', 'K5', 'K6', 'J6', 'I6', 'I5'],
                              'K5': ['J4', 'L5', 'L6', 'K6', 'J6', 'J5'],
                              'L5': ['M5', 'M6', 'L6', 'K6', 'K5'], 'M5': ['N5', 'N6', 'M6', 'L6', 'L5'],
                              'N5': ['N6', 'M6', 'M5'],
                              'O5': ['N4', 'O4', 'P4', 'P5', 'P6', 'O6'], 'P5': ['O4', 'P4', 'P6', 'O6', 'O5'],
                              'A6': ['A5', 'B5', 'B6', 'B7', 'A7'], 'B6': ['A5', 'B5', 'B7', 'A7', 'A6'],
                              'C6': ['C5', 'D5', 'D6', 'D7', 'C7'],
                              'D6': ['C5', 'D5', 'E5', 'E6', 'E7', 'D7', 'C7', 'C6'],
                              'E6': ['D5', 'E5', 'F5', 'F6', 'F7', 'F8', 'E7', 'D7', 'D6'],
                              'F6': ['E5', 'F5', 'F7', 'E7', 'E6'],
                              'G6': ['G5', 'H5', 'H6', 'H7', 'G7'], 'H6': ['G5', 'H5', 'I5', 'I6', 'G7', 'G6'],
                              'I6': ['H5', 'I5', 'J5', 'J6', 'H6'], 'J6': ['I5', 'J5', 'K5', 'K6', 'I6'],
                              'K6': ['J5', 'K5', 'L5', 'L6', 'J6'], 'L6': ['K5', 'L5', 'M5', 'M6', 'M7', 'K6'],
                              'M6': ['L5', 'M5', 'N5', 'N6', 'N7', 'M7', 'L6'],
                              'N6': ['M5', 'N5', 'O7', 'N7', 'M7', 'M6'],
                              'O6': ['O5', 'P5', 'P6', 'P7'], 'P6': ['O5', 'P5', 'P7', 'O7', 'O6'],
                              'A7': ['A6', 'B6', 'B7', 'B8', 'A8'], 'B7': ['A6', 'B6', 'B8', 'A8', 'A7'],
                              'C7': ['C6', 'D6', 'D7'], 'D7': ['C6', 'D6', 'E6', 'E7', 'E8', 'C7'],
                              'E7': ['D6', 'E6', 'F6', 'F7', 'F8', 'E8', 'D8', 'D7'],
                              'F7': ['E6', 'F6', 'F8', 'E8', 'E7'], 'G7': ['G6', 'H6', 'H7', 'H8', 'G8'],
                              'H7': ['G6', 'I7', 'I8', 'H8', 'G8', 'G7'], 'I7': ['J7', 'J8', 'I8', 'H8', 'H7'],
                              'J7': ['J8', 'I8', 'I7'], 'K7': ['L7', 'L8', 'K8'],
                              'L7': ['M6', 'M7', 'M8', 'L8', 'K8', 'K7'],
                              'M7': ['L6', 'M6', 'N6', 'N7', 'N8', 'M8', 'L8', 'L7'],
                              'N7': ['M6', 'N6', 'O7', 'O8', 'N8', 'M8', 'M7'],
                              'O7': ['N6', 'P6', 'P7', 'P8', 'O8', 'N8', 'N7'], 'P7': ['O6', 'P6', 'P8', 'O8', 'O7'],
                              'A8': ['A7', 'B7', 'B8', 'B8', 'A9'], 'B8': ['A7', 'B7', 'B9', 'A9', 'A8'],
                              'C8': ['D8', 'D9', 'C9'], 'D8': ['E7', 'E8', 'E9', 'D9', 'C9', 'C8'],
                              'E8': ['D7', 'E7', 'F7', 'F8', 'F9', 'E9', 'D9', 'D8'],
                              'F8': ['E7', 'F7', 'G9', 'F9', 'E9', 'E8'],
                              'G8': ['G7', 'H7', 'H8', 'H9', 'G9', 'F9'],
                              'H8': ['G7', 'H7', 'I7', 'I8', 'I9', 'H9', 'G9', 'G8'],
                              'I8': ['H7', 'I7', 'J7', 'J8', 'J9', 'I9', 'H9', 'H8'],
                              'J8': ['I7', 'J7', 'J9', 'I9', 'I8'], 'K8': ['K7', 'L7', 'L8', 'L9', 'K9'],
                              'L8': ['K7', 'L7', 'M7', 'M8', 'M9', 'L9', 'K9', 'K8'],
                              'M8': ['L7', 'M7', 'N7', 'N8', 'L9', 'L8'],
                              'N8': ['M7', 'N7', 'O7', 'O8', 'M8'], 'O8': ['N7', 'O7', 'P7', 'P8', 'N8'],
                              'P8': ['O7', 'P7', 'O8'], 'A9': ['A8', 'B8', 'B9'], 'B9': ['A8', 'B8', 'C9', 'A9'],
                              'C9': ['B8', 'C8', 'D8', 'D9', 'B9'], 'D9': ['C8', 'D8', 'E8', 'E9', 'E10', 'C9'],
                              'E9': ['D8', 'E8', 'F8', 'F9', 'F10', 'E10', 'D10', 'D9'],
                              'F9': ['E8', 'F8', 'G8', 'G9', 'G10' 'F10', 'E10', 'E9'],
                              'G9': ['F8', 'G8', 'H8', 'H9', 'H10', 'G10', 'F10', 'F9'],
                              'H9': ['G8', 'H8', 'I8', 'I9', 'I10', 'H10', 'G10', 'G9'],
                              'I9': ['H8', 'I8', 'J8', 'J9', 'J10', 'I10', 'H10', 'H9'],
                              'J9': ['I8', 'J8', 'K10', 'J10', 'I10', 'I9'], 'K9': ['K8', 'L8', 'L9', 'L10', 'K10'],
                              'L9': ['K8', 'L8', 'M8', 'M9', 'M10', 'L10', 'K10', 'K9'],
                              'M9': ['L8', 'N9', 'N10', 'M10', 'L10', 'L9'], 'N9': ['O9', 'O10', 'N10', 'M10', 'M9'],
                              'O9': ['P9', 'P10', 'O10', 'N10', 'N9'], 'P9': ['P10', 'O10', 'O9'],
                              'A10': ['B10', 'B11', 'A11'], 'B10': ['B11', 'A11', 'A10'], 'C10': ['D10', 'D11', 'C11'],
                              'D10': ['E9', 'E10', 'E11', 'D11', 'C11', 'C10'],
                              'E10': ['D9', 'E9', 'F9', 'F10', 'F11', 'E11', 'D11', 'D10'],
                              'F10': ['E9', 'F9', 'G9', 'F11', 'E11', 'E10'],
                              'G10': ['F9', 'G9', 'H9', 'H10'], 'H10': ['G9', 'H9', 'I9', 'I10', 'I11', 'G10'],
                              'I10': ['H9', 'I9', 'J9', 'J10', 'J11', 'I11', 'H11', 'H10'],
                              'J10': ['I9', 'J9', 'K9', 'K10', 'I11', 'I10'],
                              'K10': ['J9', 'K9', 'L9', 'L10', 'J10'], 'L10': ['K9', 'L9', 'M9', 'M10', 'K10'],
                              'M10': ['L9', 'M9', 'N9', 'N10', 'N11', 'M11', 'L11', 'L10'],
                              'N10': ['M9', 'N9', 'O9', 'O10', 'N11', 'M11', 'M10'],
                              'O10': ['N9', 'O9', 'P9', 'P10', 'P11', 'N11', 'N10'],
                              'P10': ['O9', 'P9', 'P11', 'O11', 'O10'],
                              'A11': ['A10', 'A12', 'B11'], 'B11': ['A11', 'B10', 'B12'], 'C11': ['C10', 'C12', 'D11'],
                              'D11': ['C11', 'D10', 'D12', 'E11'],
                              'E11': ['D11', 'E10', 'E12', 'F11'], 'F11': ['E11', 'F10', 'F12'], 'G11': ['G12', 'H11'],
                              'H11': ['G11', 'H12', 'I11'], 'I11': ['H11', 'I10', 'I12', 'J11'],
                              'J11': ['I11', 'J12', 'K11'], 'K11': ['J11', 'K12', 'L11'],
                              'L11': ['K11', 'L12', 'M11'], 'M11': ['L11', 'M10', 'M12', 'N11'],
                              'N11': ['M11', 'N10', 'N12'],
                              'O11': ['O12', 'P11'], 'P11': ['O1', 'P10', 'P12'], 'A12': ['A11', 'A13', 'B12'],
                              'B12': ['A12', 'B11', 'B13'], 'C12': ['C11', 'D12'], 'D12': ['C12', 'D11', 'D13'],
                              'E12': ['E11', 'E13', 'F12'], 'F12': ['E12', 'F11', 'F13', 'G12'],
                              'G12': ['F12', 'G11', 'G13', 'H12'],
                              'H12': ['G12', 'H11', 'H13', 'I12'], 'I12': ['H12', 'I11', 'I13', 'J12'],
                              'J12': ['I12', 'J11', 'J13', 'K12'], 'K12': ['J12', 'K11', 'L12'],
                              'L12': ['K12', 'L11', 'M12'], 'M12': ['L12', 'M11', 'N12'], 'N12': ['M12', 'N11'],
                              'O12': ['O11', 'O13', 'P12'], 'P12': ['O12', 'P11', 'P13'], 'A13': ['A12', 'A14', 'B13'],
                              'B13': ['A13', 'B12', 'B14', 'C13'], 'C13': ['B13', 'C14', 'D13'],
                              'D13': ['C13', 'D12', 'D14'],
                              'E13': ['E12', 'E14', 'F13'], 'F13': ['E13', 'F12', 'F14'], 'G13': ['G12', 'G14', 'H13'],
                              'H13': ['G13', 'H12', 'H14'], 'I13': ['I12', 'I14', 'J13'],
                              'J13': ['I13', 'J12', 'J14', 'K13'], 'K13': ['J13', 'K14'],
                              'L13': ['L14', 'M13'], 'M13': ['L13', 'M14', 'N13'], 'N13': ['M13', 'N14', 'O13'],
                              'O13': ['N13', 'O12', 'O14', 'P13'], 'P13': ['O13', 'P12', 'P14'],
                              'A14': ['A13', 'A15', 'B14'], 'B14': ['A14', 'B13', 'B15', 'C14'],
                              'C14': ['B14', 'C13', 'C15', 'D14'], 'D14': ['C14', 'D13', 'D15'],
                              'E14': ['E13', 'F14'], 'F14': ['E14', 'F13', 'F15'], 'G14': ['G13', 'G15', 'H14'],
                              'H14': ['G14', 'H13', 'H15'], 'I14': ['I12', 'J14'], 'J14': ['I14', 'J13', 'J15', 'K14'],
                              'K14': ['J14', 'K13', 'K15', 'L14'],
                              'L14': ['K14', 'L13', 'L15', 'M14'], 'M14': ['L14', 'M13', 'M15', 'N14'],
                              'N14': ['M14', 'N13', 'N15', 'O14'],
                              'O14': ['N14', 'O13', 'O15', 'P14'], 'P14': ['O14', 'P13', 'P15'],
                              'A15': ['A14', 'A16', 'B15'], 'B15': ['A15', 'B14', 'B16', 'C15'],
                              'C15': ['B15', 'C14', 'C16', 'D15'], 'D15': ['C15', 'D14', 'D16'],
                              'E15': ['E16', 'F15'], 'F15': ['E15', 'F16', 'G15'], 'G15': ['F15', 'G14', 'G16', 'H15'],
                              'H15': ['G15', 'H14', 'H16'], 'I15': ['I16', 'J15'], 'J15': ['I15', 'J14', 'J16', 'K15'],
                              'K15': ['J15', 'K14', 'K16'],
                              'L15': ['L14', 'L16', 'M15'], 'M15': ['L15', 'M14', 'M16', 'N15'],
                              'N15': ['M15', 'N14', 'N16', 'O15'],
                              'O15': ['N15', 'O14', 'O16', 'P15'], 'P15': ['O15', 'P14', 'P16'],
                              'A16': ['A15', 'B16'], 'B16': ['A16', 'B15', 'C16'], 'C16': ['B16', 'C15', 'D16'],
                              'D16': ['C16', 'D15', 'E16'],
                              'E16': ['D16', 'E15', 'F16'], 'F16': ['E16', 'F15', 'G16'], 'G16': ['F16', 'G15', 'H16'],
                              'H16': ['G16', 'H15'], 'I16': ['I15', 'J16'], 'J16': ['I16', 'J15', 'K16'],
                              'K16': ['J16', 'K15'],
                              'L16': ['L15', 'M16'], 'M16': ['L16', 'M15', 'N16'], 'N16': ['M16', 'N15', 'O16'],
                              'O16': ['N16', 'O15', 'P16'], 'P16': ['O16', 'P15']}

window.mainloop()
