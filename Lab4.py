import numpy as np
from csv import reader
# Здравствуйте! Есть доказательство для набора из 7, второй части доп задания нету

class Item:
    def __init__(self, name, weight, value) -> None:
        self.name = name
        self.weight = weight
        self.value = value



def research(items, inventar):
    
        
         
    matric = np.array([[0]*(inventar + 1)]*(len(items)+1))
    azbuka = [[""]*9 for _ in range(len(items)+1)]
    
    
    for i in range(1, len(items)+1):
        for j in range(1, inventar+1):
            
            if j - items[i-1].weight >= 0:
                matric[i, j] = max(matric[i-1, j], items[i-1].value + matric[i-1, j - items[i-1].weight])

                if matric[i-1, j] < items[i-1].value + matric[i-1, j - items[i-1].weight]:
                    azbuka[i][j] = azbuka[i-1][j-items[i-1].weight] + items[i-1].name*items[i-1].weight

                else:
                    azbuka[i][j] = azbuka[i-1][j]
            else:
                matric[i, j] = matric[i-1, j]
                azbuka[i][j] = azbuka[i-1][j]
    if 15 + matric[-1, -1] - (205 - matric[-1, -1]) > 0: # очки персонажа + очки за предметы - (сумма всех очков предметов - очки за предметы)

        print(matric)
        b = []
        for x in azbuka[-1][-1]:
            b.append([x])
        print(*b[:4])
        print(*b[4:])

    else:
        print("Такого набора нет")
    


items = []

with open("predmets.csv", "r") as csvfile: # создание списка предметов. Tабличку скопировал с сайта, в екселе в csv перевел
        table = reader(csvfile, delimiter=";")
        for row in table:

            items.append(Item(row[1], int(row[2][0]), int(row[3])))

research(items, 8)
