# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import csv

def init(name):
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
            data = 0
            items.append(item)
        items.pop(0)
#        for item in items:
#            for data in items:
#                for i in data:
#                    i = int(i)
    print(items)
    
def save(cutJumbo, name):
    name += "_solution.csv"
    with open(name, 'w'):
        

init("A1")


            
