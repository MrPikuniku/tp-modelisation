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
        parcours = [self]
        while noeud != arr:
            mini_estimation = estimations[noeud.voisins[0].nom]
            mini_noeud = noeud.voisins[0]
            # Comparer les estimations des autres voisins
            for i in range(1, len(noeud.voisins)):
                if estimations[noeud.voisins[i].nom] < mini_estimation:
                    mini_estimation = estimations[noeud.voisins[i].nom]
                    mini_noeud = noeud.voisins[i]
            noeud = mini_noeud
            parcours.append(noeud)
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

arad = Noeud("Arad",[zerind,timisoara,sibiu],[75,118,140])
craiova = Noeud("Craiova", [dobreta, rimnicu, pitesti],[120,146,138])
zerind = Noeud("Zerind", [arad, oradea], [75, 71])
timisoara = Noeud("Timisoara", [arad, lugoj], [118, 111])
lugoj = Noeud("Lugoj", [timisoara, mehadia], [111, 70])
mehadia = Noeud("Mehadia", [lugoj, dobreta], [70, 75])
dobreta = Noeud("Dobreta", [mehadia, craiova], [75, 120])
oradea = Noeud("Oradea", [zerind, sibiu], [71, 151])
sibiu = Noeud("Sibiu", [arad, oradea, fagaras, rimnicu], [140, 151, 99, 80])
fagaras = Noeud("Fagaras", [sibiu, bucharest], [99, 211])
rimnicu = Noeud("Rimnicu Vilcea", [sibiu, craiova, pitesti], [80, 146, 97])
pitesti = Noeud("Pitesti", [rimnicu, craiova, bucharest], [97, 138, 101])
urziceni = Noeud("Urziceni", [bucharest, hirsova, vaslui], [85, 98, 142])
hirsova = Noeud("Hirsova", [urziceni, eforie], [98, 86])
eforie = Noeud("Ephorie", [hirsova], [86])
vaslui = Noeud("Vaslui", [urziceni, lasi], [142, 92])
lasi = Noeud("Lasi", [vaslui, neamt], [92, 87])
neamt = Noeud("Neamt", [lasi], [87])
giurgiu = Noeud("Giurgiu", [bucharest], [90])
bucharest = Noeud("Bucharest", [fagaras, pitesti, giurgiu, urziceni], [211, 101, 90, 85])




h = { "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242, "Ephorie": 161,
    "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Lasi": 226, "Lugoj": 244,
    "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
    "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374}


lugoj.rech_glout(bucharest,h)



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
