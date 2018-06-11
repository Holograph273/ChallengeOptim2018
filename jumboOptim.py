# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import csv

def coupage_verticale(jumbo,absc,type1,type2, cut):
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
    plate1[2] = jumbo[2]
    plate2[2] = jumbo[2] + absc
    # Y
    plate1[3] = 0
    plate2[3] = 0
    # Width
    plate1[4] = absc
    plate2[4] = jumbo[4] - absc
    # height
    plate1[5] = jumbo[5]
    plate2[5] = jumbo[5]
    #Type
    plate1[6] = type1
    plate2[6] = type2
    #cut
    plate1[7] = cut
    plate2[7] = cut
    #parent
    plate1[8] = jumbo[1]
    plate2[8] = jumbo[1]
    print(plate2[2], plate2[3], plate2[4], plate2[5])
    return plate1,plate2

def coupage_horizontale(jumbo,ordo,type1,type2, cut):
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
    plate1[7] = cut
    plate2[7] = cut
    #parent
    plate1[8] = jumbo[1]
    plate2[8] = jumbo[1]
    
    return plate1,plate2

def max_double(items,Maxprecedent):
    indice = 0
    valeur = 0
    n= len(items)
    for i in range(n):
        if((int(items[i][1]) > int(valeur) or int(items[i][2]) > int(valeur)) and (int(items[i][1]) < Maxprecedent or int(items[i][2]) < Maxprecedent)):
            indice = i
            if(int(items[i][1]) > int(items[i][2])):
                valeur = items[i][1]       
            else:
                valeur = items[i][2]
    Maxprecedent = valeur
    #print(Maxprecedent)
    return indice
  
def search_index(k, allNodes, level):   
    for i in range(k, len(allNodes)):
        if (allNodes[i][7] == level):
            return i

def init_jumbo():
    tab = [[0,0,0,0,6000,3210,-2,0,-1]]
    for i in range (100):
        tab.append([0,0,0,0,6000,3210,-2,0,-1])
    return tab

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
    for node in allNodes:
        sep = ";"
        sep.join(node)
    with open(name, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(allNodes)
       
def main():
    global items
    #Initialise all jumbos
    jumbos = []
    jumbos = init_jumbo()
    
    for i in range(1, 11):
        #Init items
        init_items("A" + str(i))
        
        #Init nodes
        maxPrecedent = 6000  
        nodeactuel = jumbos[i]
        allNodes = [jumbos[i]] #table that has all the nodes for saving
        
        maxi = max_double(items, maxPrecedent)
        
        #Cut Vertical 1
        k = 0
        while (maxi < nodeactuel[4]): #Check when no items fit
            #cut the nodes
            cutNodes = coupage_verticale(jumbos[i], maxi, -2, -2, 1)

            allNodes.append(cutNodes[0])
            allNodes.append(cutNodes[1])
            #
            k = search_index(k, allNodes, 1)
            nodeactuel = allNodes[k]
            
            #Calculate next max width (knowing we can rotate objects)
            maxi = max_double(items, maxPrecedent) 
        
        #Cut Horizontal 1
        k = 0
        while (maxi < nodeactuel[5]): #Check when no items fit
            #cut the nodes
            cutNodes = coupage_verticale(jumbos[i], maxi, -2, -2, 2)

            allNodes.append(cutNodes[0])
            allNodes.append(cutNodes[1])
            #
            k = search_index(k, allNodes, 2) #Search for the next node of level 2
            nodeactuel = allNodes[k]
            
            #Calculate next max width (knowing we can rotate objects)
            maxi = max_double(items, maxPrecedent) 
        
        #Cut Vertical 2
        k = 0
        while (maxi < nodeactuel[4]): #Check when no items fit
            #cut the nodes
            cutNodes = coupage_verticale(jumbos[i], maxi, -2, -2, 3)

            allNodes.append(cutNodes[0])
            allNodes.append(cutNodes[1])
            #
            k = search_index(k, allNodes, 3) #Search for the next node of level 3
            nodeactuel = allNodes[k]
            
            #Calculate next max width (knowing we can rotate objects)
            maxi = max_double(items, maxPrecedent) 
                
        
        allNodes.append(['ITEM_ID', 'LENGTH_ITEM', 'WIDTH_ITEM', 'STACK', 'SEQUENCE'], 0)
        save(allNodes, "A" + str(i))
    
main()


            
