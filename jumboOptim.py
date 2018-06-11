# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import csv

def coupage_verticale(jumbo,absc,type1,type2):
    #creation des 2 listes
    plate1 = [0,0,0,0,0,0,0,0,0]
    plate2 = [0,0,0,0,0,0,0,0,0]
    #plate id
    plate1[0] = jumbo[0]
    plate2[0] = jumbo[0]
    #node id
    plate1[1] = jumbo[1] + 1
    plate2[1] = jumbo[1] + 2
    # X
    plate1[2] = 0
    plate2[2] = absc
    # Y
    plate1[3] = 0
    plate2[3] = 0
    # Weight
    plate1[4] = absc
    plate2[4] = jumbo[4] - absc
    # height
    plate1[5] = jumbo[5]
    plate2[5] = jumbo[5]
    #Type
    plate1[6] = type1
    plate2[6] = type2
    #cut
    plate1[7] = jumbo[7] + 1
    plate2[7] = jumbo[7] + 1
    #parent
    plate1[8] = jumbo[1]
    plate2[8] = jumbo[1]
    return plate1,plate2

def coupage_horizontale(jumbo,ordo,type1,type2):
    #cretion des 2 listes
    plate1 = [0,0,0,0,0,0,0,0,0]
    plate2 = [0,0,0,0,0,0,0,0,0]
    #plate id
    plate1[0] = jumbo[0]
    plate2[0] = jumbo[0]
    #node id
    plate1[1] = jumbo[1] + 1
    plate2[1] = jumbo[1] + 2
    # X
    plate1[2] = 0
    plate2[2] = 0
    # Y
    plate1[3] = 0
    plate2[3] = ordo
    # Widht
    plate1[4] = jumbo[4]
    plate2[4] = jumbo[4]
    # height
    plate1[5] = ordo
    plate2[5] = jumbo[5] - ordo
    #Type
    plate1[6] = type1
    plate2[6] = type2
    #cut
    plate1[7] = jumbo[7] + 1
    plate2[7] = jumbo[7] + 1
    #parent
    plate1[8] = jumbo[1]
    plate2[8] = jumbo[1]
    return plate1,plate2

def init_jumbo():
    tab = [[0,0,0,0,6000,3210,-2,0,-1]]
    for i in range (100):
        tab.append([0,0,0,0,6000,3210,-2,0,-1])
    return tab

def max_double(items,Maxprecedent):
    indice = 0
    valeur = 0
    n= len(items)
    for i in range(n):
        if((items[i][1] > valeur or items[i][2] > valeur) and (items[i][1] < Maxprecedent or items[i][2] < Maxprecedent)):
            indice = i
            if(items[i][1] > items[i][2]):
                valeur = items[i][1]       
            else:
                valeur = items[i][2]
    Maxprecedent = valeur
    return indice
    

def init_items(name):
    global items
    items = []
    name += "_batch.csv"
    print(name)
    with open(name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            item = []
            for el in row:
                item.append(el)
            item = item[0].split(";")
            items.append(item)
        items.pop(0)
#        for item in items:
#            for data in items:
#                for i in data:
#                    i = int(i)
    print(items)
    
def save(allNodes, name):
    name += "_solution.csv"
    with open(name, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(allNodes)
       
def main():
    global items
    jumbos = []
    maxPrecedent = 6000
    init_items("A1")
    jumbos = init_jumbo()
    max_double(items, maxPrecedent)
    #Init nodes
    k = 0
    nodeactuel = jumbos[k]
    allNodes = [jumbos[k]] #table that has all the nodes for saving
    
    while (max_double < nodeactuel[4]): 
        #add nodes to the save
        allNodes.append(coupage_verticale(jumbos[0], max_double, -2, )[0])
        allNodes.append(coupage_verticale(jumbos[0], max_double, -2, )[1])
        #
        k += 2
        nodeactuel[allNodes[k]]
    
main()


            
