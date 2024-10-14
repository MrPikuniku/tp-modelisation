# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:19:22 2024

@author: ms284034
"""

class Noeud:    
    def __init__(self, nom, voisins=[],couts=[]):
        self.nom = nom
        self.voisins = voisins
        self.marque = False
    def afficheNoeud(self):
        print(self.nom)
        
    def marqueNoeud(self):
        self.marque = True

class Graphe:
    def __init__(self, noeud):
        self.noeud = noeud
        
    def vol_d_oiseau(self, dep, arr):
        p = 2



arad = Noeud("Arad")

bucharest = Noeud("Bucharest")
craiova = Noeud("Craiova")
dobreta = Noeud("Dobreta")


lugoj = Noeud("Lugoj")
mehadia = Noeud("Mehadia")
timisoara = Noeud("Timisoara")




h = { arad:366, bucharest: 0, craiova: 160, "Dobreta": 262, "Eforie":161, "Fagaras":176, "Giurgiu": 77, "Hirsova": 151, 
     "Lasi":226, "Lugoj":244, "Mehadia": 241, "Nemt": 234, "Oradea":380, "Pitesti":100, "Riminicu":193, "Sibiu": 253, 
     "Timisoara":329, "Urziceni":80, "Valsui":199, "Zerind": 374}






