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




