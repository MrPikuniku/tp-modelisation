# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:19:22 2024

@author: ms284034
"""


class Noeud:    
    def __init__(self, nom, voisins=[],couts=[]):
        self.nom = nom
        self.voisins = voisins
        self.couts = couts
        self.marque = False
    def afficheNoeud(self):
        print(self.nom)
        
    def marqueNoeud(self):
        self.marque = True
        
    def rech_glout(self, arr, estimations):
        noeud = self
        parcours = [self.nom]
        while noeud != arr:
            mini_noeud = noeud.voisins[0]
            mini_estimation = estimations[noeud.voisins[0].nom]
            
            # Comparer les estimations des autres voisins
            for i in range(1, len(noeud.voisins)):
                if estimations[noeud.voisins[i].nom] < mini_estimation:
                    mini_estimation = estimations[noeud.voisins[i].nom]
                    mini_noeud = noeud.voisins[i]
            noeud = mini_noeud
            parcours.append(noeud.nom)
        return parcours
        


arad = Noeud("Arad")
craiova = Noeud("Craiova")
bucharest = Noeud("Bucharest")
dobreta = Noeud("Dobreta")
eforie = Noeud("Ephorie")
fagaras = Noeud("Fagaras")
giurgiu = Noeud("Giurgiu")
hirsova = Noeud("Hirsova")
lasi = Noeud("Lasi")
lugoj = Noeud("Lugoj")
mehadia = Noeud("Mehadia")
neamt = Noeud("Neamt")
oradea = Noeud("Oradea")
pitesti = Noeud("Pitesti")
rimnicu = Noeud("Rimnicu Vilcea")
sibiu = Noeud("Sibiu")
timisoara = Noeud("Timisoara")
urziceni = Noeud("Urziceni")
vaslui = Noeud("Vaslui")
zerind = Noeud("Zerind")

arad.voisins = [zerind, timisoara, sibiu]
arad.couts = [75, 118, 140]

craiova.voisins = [dobreta, rimnicu, pitesti]
craiova.couts = [120, 146, 138]

zerind.voisins = [arad, oradea]
zerind.couts = [75, 71]

timisoara.voisins = [arad, lugoj]
timisoara.couts = [118, 111]

lugoj.voisins = [timisoara, mehadia]
lugoj.couts = [111, 70]

mehadia.voisins = [lugoj, dobreta]
mehadia.couts = [70, 75]

dobreta.voisins = [mehadia, craiova]
dobreta.couts = [75, 120]

oradea.voisins = [zerind, sibiu]
oradea.couts = [71, 151]

sibiu.voisins = [arad, oradea, fagaras, rimnicu]
sibiu.couts = [140, 151, 99, 80]

fagaras.voisins = [sibiu, bucharest]
fagaras.couts = [99, 211]

rimnicu.voisins = [sibiu, craiova, pitesti]
rimnicu.couts = [80, 146, 97]

pitesti.voisins = [rimnicu, craiova, bucharest]
pitesti.couts = [97, 138, 101]

urziceni.voisins = [bucharest, hirsova, vaslui]
urziceni.couts = [85, 98, 142]

hirsova.voisins = [urziceni, eforie]
hirsova.couts = [98, 86]

eforie.voisins = [hirsova]
eforie.couts = [86]

vaslui.voisins = [urziceni, lasi]
vaslui.couts = [142, 92]

lasi.voisins = [vaslui, neamt]
lasi.couts = [92, 87]

neamt.voisins = [lasi]
neamt.couts = [87]

giurgiu.voisins = [bucharest]
giurgiu.couts = [90]

bucharest.voisins = [fagaras, pitesti, giurgiu, urziceni]
bucharest.couts = [211, 101, 90, 85]




h = { "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242, "Ephorie": 161,
    "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Lasi": 226, "Lugoj": 244,
    "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
    "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374}


parcou = lugoj.rech_glout(bucharest,h)

print(parcou)


a = Noeud("A")
b = Noeud("B")
c = Noeud("C")
d = Noeud("D")
e = Noeud("E")
f = Noeud("F")
g = Noeud("G")
h = Noeud("H")
i = Noeud("I")

a = Noeud("A", [c, d], [5, 5])
c = Noeud("C", [d, f, b, h], [6, 2, 3, 3])
d = Noeud("D", [e], [2])
e = Noeud("E", [b], [5])
b = Noeud("B", [g], [4])
g = Noeud("G", [i], [3])
f = Noeud("F", [b], [3])
h = Noeud("H", [i], [4])
i = Noeud("I")   
