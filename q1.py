# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""


from csv import reader
from matplotlib import pyplot as plt

with open('data.csv', 'rb') as csvFile:
    csvReader = reader(csvFile, delimiter=';', quotechar='|')
  
    v = []
    average = []
  
    for row in csvReader:
        v.append(row)
        average.append(( float(row[1]) + float(row[2])) / 2)
        
    print len(average)
    
    plt.bar(range(1,31), average)
    plt.title("Grafico de medias")
    plt.ylabel("Nota")
    plt.xlabel("Aluno")
    plt.show()
    
    
    
      
  
      
   