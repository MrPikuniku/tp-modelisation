# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:27:33 2024

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
    
    def a_eto(self, arr, estimations):
        noeud = self
        parcours = [self.nom]
        dist_cumul = 0
        while noeud != arr:
            noeud_mini = noeud.voisins[0]
            fn = dist_cumul + estimations[noeud.voisins[0].nom]
            dist_actuelle = noeud.couts[0]
            for i in range(len(noeud.voisins)):
                if (fn > dist_cumul + estimations[noeud.voisins[i].nom]) and (noeud.voisins[i].nom not in parcours):
                    noeud_mini = noeud.voisins[i]
                    fn = dist_cumul + estimations[noeud.voisins[i].nom]
                    dist_actuelle = noeud.couts[i]
                if (i==len(noeud.voisins)-1):
                    dist_cumul = dist_cumul + dist_actuelle
                    noeud = noeud_mini
                    parcours.append(noeud.nom)
        return parcours    
    
        
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


a = Noeud("A")
b = Noeud("B")
c = Noeud("C")
d = Noeud("D")
e = Noeud("E")
f = Noeud("F")
g = Noeud("G")
h = Noeud("H")
i = Noeud("I")



a.voisins = [c, d]
a.couts = [5, 5]

c.voisins = [f, b, h]
c.couts = [2, 3, 3]

d.voisins = [c,e]
d.couts = [6,2]

e.voisins = [b]
e.couts = [5]

b.voisins = [g,i]
b.couts = [4,5]

g.voisins = [i]
g.couts = [3]

f.voisins = [g]
f.couts = [3]

h.voisins = [i]
h.couts = [4]







h1 = {
    "A": 10, "B": 5, "C": 5, "D": 10, "E": 10,
    "F": 3, "G": 3, "H": 3, "I": 0
}

h2 = {
    "A": 10, "B": 2, "C": 8, "D": 11, "E": 6,
    "F": 2, "G": 1, "H": 3, "I": 0
}

h3 = {
    "A": 10, "B": 2, "C": 6, "D": 11, "E": 9,
    "F": 6, "G": 3, "H": 4, "I": 0  
}


question1 = a.rech_glout(i, h) 

question3 = a.a_eto(i, h1)
question2 = a.rech_glout(i, h3 )
question4 = a.a_eto(i, h2)
question5 = a.a_eto(i, h3)

print("Question 2: ")
print(question2)

print("Question 3: ")
print(question3)

print("Question 4")







