# -*- coding: utf-8 -*-

from csv import reader
import math
from matplotlib import pyplot as plt

def takeAverage(el):
    return el['average']

with open('data.csv', 'rb') as csvFile:
    csvReader = reader(csvFile, delimiter=';', quotechar='|')
  
    students = []
    moda = {}
    sum = 0
    
    for row in csvReader:
        average = ( float(row[1]) + float(row[2]) ) / 2
        sum += average
        students.append({ 
            'id': row[0], 
            'average': average 
        })
    
    students.sort(key=takeAverage)
    
    for row in students:
        if row['average'] in moda:
           moda[row['average']] += 1
        else:
            moda[row['average']] = 0
        
    theModa = { 'key': -1, 'value': -1};
        
    for key, value in moda.iteritems():
        if value > theModa['value']:
            theModa['value'] = value
            theModa['key'] = key
    
    # print students    
    print sum / len(students) 
    print students[int(math.floor(len(students) / 2)) - 1]['average']
    print theModa['key']
    
    
    # falta gerar o gráfico
    
    
    
